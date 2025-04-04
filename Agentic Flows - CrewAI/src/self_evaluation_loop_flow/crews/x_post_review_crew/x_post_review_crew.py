from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from self_evaluation_loop_flow.tools.CharacterCounterTool import CharacterCounterTool

from typing import Optional
from pydantic import BaseModel


class XPostVerification(BaseModel):
    valid: bool
    feedback: Optional[str]

@CrewBase
class XPostReviewCrew():
    """XPostReviewCrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def x_post_verifier(self) -> Agent:
        return Agent(
            config=self.agents_config["x_post_verifier"],
            tools=[CharacterCounterTool()],
        )

    @task
    def verify_x_post(self) -> Task:
        return Task(
            config=self.tasks_config["verify_x_post"],
            output_pydantic=XPostVerification,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the XPostReviewCrew crew"""


        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
