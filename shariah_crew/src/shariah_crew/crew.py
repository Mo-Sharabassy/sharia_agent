# import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# # ✅ Ensure API key for SerperDevTool is set
# os.environ["SERPER_API_KEY"] = "your_api_key_here"

# 🔹 Agents

web3_researcher = Agent(
   role="Web3 Research Analyst",
   goal="Identify and list Web3 companies and their protocols.",
   backstory=(
   		'''
   		An expert in blockchain technologies, specializing in discovering and categorizing
   		Web3 companies based on their purpose, technology, and protocols.
   		'''
	),
	tools=[
   		SerperDevTool(),
   		ScrapeWebsiteTool()
	],
	verbose=True,
	memory=True
)

blockchain_educator = Agent(
   role="Blockchain Educator",
   goal="Provide educational introductions to Web3 companies and their protocols.",
   backstory=(
   		'''
   		A blockchain communicator skilled at simplifying complex technical concepts
    	to educate users on how Web3 protocols function and generate revenue.
   		'''
	),
	tools=[ScrapeWebsiteTool()],
	verbose=True,
	memory=True
)

compliance_analyst = Agent(
   role="Shariah & Ethics Compliance Analyst",
   goal="Assess whether Web3 companies comply with Shariah law and ethical investment standards.",
   backstory=(
   		'''
   		A financial ethics specialist with deep knowledge of Islamic finance principles,
    	capable of analyzing Web3 protocols to determine compliance with ethical guidelines.
   		'''
	),
	tools=[
   		ScrapeWebsiteTool(),
   		SerperDevTool()  # 🔹 Added for broader research capabilities
	],
	verbose=True,
	memory=True
)

# 🔹 Tasks

find_web3_companies_task = Task(
    description=(
        '''
        Conduct research to find Web3 companies that operate blockchain protocols.
        Identify their names, official websites, and key areas of operation.
        Your final report should contain at least 10 Web3 companies with their protocol details,
        formatted as Markdown.
        '''
    ),
    expected_output="A Markdown-formatted list of 10+ Web3 companies with official websites and main protocols.",
    agent=web3_researcher,
    output_file="web3_companies.md"  # ✅ Save output
)

get_protocol_introduction_task = Task(
    description=(
        '''
        For each Web3 company found, provide an educational introduction to its protocol.
        Explain how the protocol works, how the company profits, and its main use cases.
        Format the output as a structured Markdown section.
        '''
    ),
    expected_output="A Markdown-formatted document with introductions to at least 10 Web3 company protocols.",
    agent=blockchain_educator,
    output_file="protocol_introductions.md"  # ✅ Save output
)

analyze_compliance_task = Task(
    description=(
        '''
        Evaluate whether each Web3 company follows Shariah-compliant and ethical finance principles.
        Check if they profit from interest-based lending (riba), gambling (maysir), or unethical industries
        (e.g., adult content, alcohol, weapons). Format the output as a Markdown table with three columns:
        | Company Name | Compliance Status | Notes |
        '''
    ),
    expected_output="A Markdown table summarizing the compliance status of each Web3 company.",
    agent=compliance_analyst,
    output_file="compliance_analysis.md"  # ✅ Save output
)

# 🔹 Crew
crew = Crew(
    agents=[web3_researcher, blockchain_educator, compliance_analyst],
    tasks=[find_web3_companies_task, get_protocol_introduction_task, analyze_compliance_task],
    process=Process.sequential,
    memory=True  # ✅ Enable memory for better context retention
)

# ✅ Start the crew execution
result = crew.kickoff()

# ✅ Print or save the final output
print(result)
