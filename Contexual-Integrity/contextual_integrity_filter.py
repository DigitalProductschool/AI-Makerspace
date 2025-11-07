from typing import Dict, List, Any


class ContextualIntegrityFilter:
    """
    Applies contextual integrity rules to calendar data
    Decides what to share based on requester context
    """
    
    def detect_context(self, user_message: str) -> Dict[str, Any]:
        """
        Detect requester context from user message using keyword matching
        """
        message_lower = user_message.lower()
        
        # Medical/healthcare keywords
        if any(word in message_lower for word in [
            "doctor", "appointment", "medical", "clinic", "hospital", "checkup", "physician"
        ]):
            return {
                "requester_type": "medical",
                "legitimate_need": "available time slots only",
                "reasoning": "Medical appointment - only needs availability"
            }
        
        # Restaurant/dining keywords
        if any(word in message_lower for word in [
            "restaurant", "table", "reservation", "lunch", "dinner", "brunch", "breakfast", "dine", "eat"
        ]):
            return {
                "requester_type": "restaurant",
                "legitimate_need": "reservation time and party size",
                "reasoning": "Restaurant reservation - needs time and party size only"
            }
        
        # Entertainment/movie keywords
        if any(word in message_lower for word in [
            "movie", "cinema", "film", "theater", "show", "ticket", "screening"
        ]):
            return {
                "requester_type": "entertainment",
                "legitimate_need": "movie time and party size",
                "reasoning": "Entertainment booking - needs time and party size"
            }
        
        # Work/employer keywords
        if any(word in message_lower for word in [
            "meeting", "work", "office", "schedule", "colleague", "business", "employer"
        ]):
            return {
                "requester_type": "work",
                "legitimate_need": "work conflicts only",
                "reasoning": "Work scheduling - only work conflicts relevant"
            }
        
        # Default: minimal sharing
        return {
            "requester_type": "unknown",
            "legitimate_need": "availability",
            "reasoning": "Unknown context - minimal sharing"
        }
    
    def apply_filter(
        self,
        events: List[Dict],
        available_slots: List[Dict],
        requester_type: str
    ) -> Dict[str, Any]:
        """
        Apply contextual integrity rules based on requester type
        
        Args:
            events: Full calendar events
            available_slots: Calculated free time slots
            requester_type: Type of requester (medical, restaurant, etc.)
        
        Returns:
            Filtered data appropriate for the context
        """
        
        # Medical/healthcare context - only availability
        if requester_type == "medical":
            return {
                "available_slots": available_slots,
                "note": "Medical context - only availability shared"
            }
        
        # Restaurant/dining context
        if requester_type == "restaurant":
            dining_events = [
                e for e in events 
                if any(word in e.get("location", "").lower() for word in ["restaurant", "cafe", "bistro"])
                or any(word in e.get("title", "").lower() for word in ["lunch", "dinner", "brunch", "breakfast"])
            ]
            
            if dining_events:
                event = dining_events[0]
                party_size = 1 + len(event.get("attendees", []))
                
                return {
                    "has_existing_plan": True,
                    "time": event["start"],
                    "party_size": party_size,
                    "note": "Restaurant context - time and party size shared (companions kept private)"
                }
            else:
                return {
                    "has_existing_plan": False,
                    "available_slots": available_slots,
                    "note": "No existing dining plan found"
                }
        
        # Entertainment/movie context
        if requester_type == "entertainment":
            entertainment_events = [
                e for e in events 
                if any(word in e.get("location", "").lower() for word in ["cinema", "theater", "theatre"])
                or any(word in e.get("title", "").lower() for word in ["movie", "film", "show", "concert"])
            ]
            
            if entertainment_events:
                event = entertainment_events[0]
                party_size = 1 + len(event.get("attendees", []))
                
                # Extract movie title if present
                title = event.get("title", "")
                movie_title = None
                if "-" in title:
                    parts = title.split("-")
                    if len(parts) > 1:
                        movie_title = parts[1].strip()
                
                response = {
                    "has_existing_plan": True,
                    "time": event["start"],
                    "party_size": party_size,
                    "note": "Entertainment context - time and party size shared (companions kept private)"
                }
                
                if movie_title:
                    response["movie_title"] = movie_title
                
                return response
            else:
                return {
                    "has_existing_plan": False,
                    "available_slots": available_slots,
                    "note": "No existing entertainment plan found"
                }
        
        # Work/employer context
        if requester_type == "work":
            work_events = [
                e for e in events 
                if any(word in e.get("title", "").lower() for word in ["meeting", "work", "call", "conference"])
            ]
            
            if work_events:
                work_conflicts = []
                for event in work_events:
                    work_conflicts.append({
                        "start": event["start"],
                        "end": event["end"],
                        "type": "meeting"
                    })
                return {
                    "work_conflicts": work_conflicts,
                    "note": "Work context - work schedule shared (personal plans kept private)"
                }
            else:
                return {
                    "available_slots": available_slots,
                    "note": "Work availability"
                }
        
        # Unknown context - minimal sharing
        return {
            "available_slots": available_slots,
            "note": f"Unknown context ({requester_type}) - only availability shared"
        }


# Singleton
_filter_instance = None

def get_ci_filter() -> ContextualIntegrityFilter:
    """Get or create the CI filter instance"""
    global _filter_instance
    if _filter_instance is None:
        _filter_instance = ContextualIntegrityFilter()
    return _filter_instance