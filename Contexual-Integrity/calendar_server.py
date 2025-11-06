import asyncio
import json
from datetime import datetime
from typing import Any, Sequence, List, Dict
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio
from contextual_integrity_filter import get_ci_filter

server = Server("calendar-server")
ci_filter = get_ci_filter()

# Load calendar data
with open('calendar_data.json', 'r') as f:
    CALENDAR_EVENTS = json.load(f)


def get_events_for_date(date: str) -> List[Dict]:
    """Get all events for a specific date"""
    return [e for e in CALENDAR_EVENTS if e["start"].startswith(date)]


def get_available_slots(date: str, events: List[Dict]) -> List[Dict]:
    """Calculate free time slots for a date"""
    day_start = datetime.fromisoformat(f"{date}T08:00:00")
    day_end = datetime.fromisoformat(f"{date}T23:00:00")
    
    # Get busy periods
    busy_periods = []
    for event in events:
        busy_periods.append({
            "start": datetime.fromisoformat(event["start"]),
            "end": datetime.fromisoformat(event["end"])
        })
    
    busy_periods.sort(key=lambda x: x["start"])
    
    # Calculate free slots
    available_slots = []
    current_time = day_start
    
    for busy in busy_periods:
        if current_time < busy["start"]:
            available_slots.append({
                "start": current_time.strftime("%H:%M"),
                "end": busy["start"].strftime("%H:%M")
            })
        current_time = max(current_time, busy["end"])
    
    if current_time < day_end:
        available_slots.append({
            "start": current_time.strftime("%H:%M"),
            "end": day_end.strftime("%H:%M")
        })
    
    return available_slots


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available calendar tools"""
    return [
        Tool(
            name="check_calendar",
            description="Check calendar and get information filtered by contextual integrity based on user's request",
            inputSchema={
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date to check (YYYY-MM-DD)"
                    },
                    "user_message": {
                        "type": "string",
                        "description": "The user's original message/request (used to determine context)"
                    },
                    "contextual_integrity_enabled": {
                        "type": "boolean",
                        "description": "Whether to apply contextual integrity filtering",
                        "default": True
                    }
                },
                "required": ["date", "user_message"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Any) -> Sequence[TextContent]:
    """Handle tool calls"""
    
    if name == "check_calendar":
        date = arguments["date"]
        user_message = arguments["user_message"]
        ci_enabled = arguments.get("contextual_integrity_enabled", True)
        
        # Step 1: Get calendar data (server's responsibility)
        events = get_events_for_date(date)
        
        if not ci_enabled:
            result = {
                "shared_data": events,
            }
        else:
            context_info = ci_filter.detect_context(user_message)
            requester_type = context_info["requester_type"]
            available_slots = get_available_slots(date, events)
            
            # Apply filter to decide what to share
            shared_data = ci_filter.apply_filter(events, available_slots, requester_type)
            
            result = {
                "shared_data": shared_data,
            }
        
        return [TextContent(
            type="text",
            text=json.dumps(result, indent=2)
        )]
    
    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    """Run the MCP server"""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())