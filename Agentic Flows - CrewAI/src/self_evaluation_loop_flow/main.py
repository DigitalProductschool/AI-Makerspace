from typing import Optional

from pydantic import BaseModel

from crewai.flow import Flow, listen, start, router, and_, or_

from .crews.shakespeare_crew.shakespeare_crew import ShakespeareCrew
from .crews.x_post_review_crew.x_post_review_crew import XPostReviewCrew

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

class ShakespeareXPostFlowState(BaseModel):
    user_prompt: str = ""
    x_post: str = ""
    feedback: Optional[str] = None
    valid: bool = False
    retry_count: int = 0
    is_inappropiate: bool = False


class ShakespeareXPostFlow(Flow[ShakespeareXPostFlowState]):

    @start()
    def entry(self):
        print("Welcome to the Shakespeare X Post Flow")
        self.state.user_prompt = "Write a tweet about summers."

    @router(entry)
    def guardrails(self):
        flagged = client.moderations.create(
            model="omni-moderation-latest",
            input=self.state.user_prompt,
        ).results[0].flagged
        if flagged:
            self.state.is_inappropiate = True
            return "inappropiate"
        return "safe"

    @listen("inappropiate")
    def inappropiate_exit(self):
        if self.state.is_inappropiate:
            print("As an AI model, I cannot generate content that violates my policies.")

    @router("safe")
    def gatekeeper(self):
        # To determine which crew to use
        # To determine if multi-agent is needed or single agent or maybe direct LLM inference

        # LLM as a judge
        # Keyword Matching
        # Train a classifier

        if 'tweet' in self.state.user_prompt:
            return "use_multi_agent"
        
        return "use_llm_diretly"
    
    @listen("use_llm_diretly")
    def answer_request(self):
        response = client.responses.create(
            model="gpt-4o",
            input=self.state.user_prompt,
        )

        print(response.output_text)
    
    @listen(or_("use_multi_agent", "retry"))
    def generate_shakespeare_x_post(self):
        result = ShakespeareCrew().crew().kickoff(inputs={"topic": self.state.user_prompt, "feedback": self.state.feedback})
        print("result", result.raw)
        self.state.x_post = result.raw

    @router(generate_shakespeare_x_post)
    def evaluate_x_post(self):
        if self.state.retry_count > 3:
            return "max_retry_exceeded"
        
        result = XPostReviewCrew().crew().kickoff(inputs={"x_post": self.state.x_post})
        self.state.valid = result["valid"]
        self.state.feedback = result["feedback"]

        print("valid", self.state.valid)
        print("feedback", self.state.feedback)

        self.state.retry_count += 1

        if self.state.valid:
            return "completed"  
        
        print("Retry")
        return "retry"

    @listen("completed")
    def crew_result(self):
        print("X post is valid")
        print("X post:", self.state.x_post)

    @listen("max_retry_exceeded")
    def max_retry_exceeded_exit(self):
        print("Max retry count exceeded")
        print("X post:", self.state.x_post)
        print("Feedback:", self.state.feedback)



def kickoff():
    shakespeare_flow = ShakespeareXPostFlow()
    shakespeare_flow.kickoff()


def plot():
    shakespeare_flow = ShakespeareXPostFlow()
    shakespeare_flow.plot()


if __name__ == "__main__":
    kickoff()
