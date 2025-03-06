import os

from textwrap import dedent
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools
from agno.tools.firecrawl import FirecrawlTools
from agno.playground import Playground, serve_playground_app

# Configurations
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
exa_api_key = os.getenv("EXA_API_KEY")
firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")

# Agent to search the web for rapid prototyping tools and technologies
deep_research_agent: Agent = Agent(
    name="Deep Research Agent",
    model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
    description=dedent("""\
        Expert at researching and recommending the best rapid prototyping tools and technologies to empower small, 
        agile product teams. Your expertise lies in quickly identifying solutions that integrate seamlessly into 
        existing codebases, minimizing setup overhead while maximizing functionality. Your users are engineers.
        Your credentials include: 
        - Advanced research methodology
        - Cross-disciplinary synthesis
        - Solution Architect
        - Technical Product Management
        - Technical Feasibility analysis
        - Technical writing excellence
        - Peer review experience
        - Citation management
        - Data interpretation
        - Technical communication
        - Research ethics
        - Emerging trends analysis\
    """),
    tools=[
        ExaTools(api_key=exa_api_key) if exa_api_key else None,
        FirecrawlTools(api_key=firecrawl_api_key) if firecrawl_api_key else None,
    ],
    instructions=dedent("""\
        1. **Research and Discovery**
           - Search for a diverse range of tools, frameworks, libraries, methods, approaches, academic papers, 
           tutorials, and example projects relevant to rapid prototyping.
           - Conduct 5 distinct searches.
           - Evaluate options based on factors such as ease of use, setup complexity, learning curve, integration 
           capabilities, and community support.

        2. **Comparative Analysis**
           - Provide a balanced assessment of each tool, listing both advantages and limitations.
           - Prioritize solutions that are well-documented, actively maintained, and offer strong community backing.
           - Present specific, actionable recommendations including links to official documentation, tutorials, and 
           example projects.
           - Ensure your analysis is concise, data-driven, and directly tied to the user's stated needs and constraints.
           - Cite your sources and mention any research limitations or potential biases.
           - Focus on practical, real-world solutions rather than purely theoretical approaches.

        3. **Write a detailed report**
           - Write down your findings in a nice, readable report with a format according to the user's needs.
           - End by asking follow-up questions to the user for further help in search.

        Iteratively modify the search by asking clarifying questions after presenting the response.
    """),
    markdown=True,
    reasoning=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    debug_mode=True,
    num_history_responses=10
)

# Agent to develop coding examples
coding_agent: Agent = Agent(
    name="Coding Agent",
    model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
    description=dedent("""\
    Expert at presenting code in a clear, readable format. Your expertise lies in writing smart end-to-end examples
    which communicate the functionality of the chosen tools to your users quickly. You are an expert DevRel and your
    users are engineers.
    Your credentials include: 
    - Advanced research methodology
    - Solution Architect
    - Technical Product Management
    - Technical Feasibility analysis
    - Excellent Engineer
    - Excellent in Developer Relations
    - Technical communication
    - Emerging trends analysis\
    """),
    tools=[
        ExaTools(api_key=exa_api_key) if exa_api_key else None,
        FirecrawlTools(api_key=firecrawl_api_key) if firecrawl_api_key else None,
    ],
    instructions=dedent("""\
        1. **Research and Discovery**
           - Search for coding examples, different methodologies, tutorials, git repositories, documentation, videos 
           and technical blogs about the tools and technologies of choice.
           - Conduct 5 distinct searches.
           - Evaluate options based on factors such as alignment with user's use-case, actively maintained, last update,
           ease of use.

        2. **Code Generation**
           - Generate an example end-to-end tutorial which must show the user how to get started with a particular tool,
           how to use it for their needs and where to find more resources for it. 

        3. **Code Presentation**
           - Present generated code in a clear, well-organised format. Use appropriate markdown code blocks with 
           language specification. Organize code presentation in a logical way (setup → core functionality → examples).
           - Highlight key parts of the code that require attention.
           - Include setup and usage instructions.
           - Explain architecture and design decisions

        4. **(Optional) API Step**
           - If it makes sense for the tool, then wrap the code written with a FastAPI or a Django backend which 
           allows ease of use for the user for integration into their codebase.
           - Ask the user if there's some specific stack they would prefer for integration.

        Focus on making the code easy to understand and implement. Maintain all the original code without 
        simplification.
    """),
    markdown=True,
    reasoning=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    debug_mode=True,
    num_history_responses=10
)

prototype_team = Agent(
    name="Junior Developer",
    model=OpenAIChat("gpt-4o"),
    team=[deep_research_agent, coding_agent],
    instructions=dedent("""\
        1. **Step 1: **Choice between Research and Coding**.
            - You must decide whether the user is asking for more research results, or asking how to get started 
            with any tool using code examples.
            - The user is most likely to go with research, at which point you must call the deep research agent first.

        2. **Step 2: Choice of Research**
            - If the choice turns out to be research, then take the user input and follow the instructions about
            'research and discovery', 'comparative analysis' and 'write a detailed report' specified in the 
            instructions for the deep research agent.
            - Display to the user the thorough technical report received from the deep research agent. Do not make
            changes to the report, show it as it is.
            - End by asking the user follow-up questions from the research agent what they'd like to do next.

        3. **Step 3: Choice of Code Example**
            - If the choice turns out to be code examples, then look at the user's response to see which tools they
            chose. If not clear, verify by asking questions.
            - Display the output of the coding agent as it is to the user, do not make any changes to it.
            - End by asking the user what they'd like to do next.
    """),
    show_tool_calls=True,
    markdown=True,
    reasoning=True,
    num_history_responses=10
)

app = Playground(agents=[prototype_team, deep_research_agent, coding_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("main:app", reload=True)
