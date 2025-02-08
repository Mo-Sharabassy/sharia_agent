from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# ✅ Tools for research
search_tool = SerperDevTool()
scraper_tool = ScrapeWebsiteTool()

# 🔹 Shariah Compliance Agent
shariah_analyst = Agent(
    role="Shariah Compliance Analyst",
    goal="Determine if {token_name} is compliant with Islamic finance principles.",
    backstory=(
        "An expert in Islamic finance with deep knowledge of Shariah compliance rules. "
        "Your job is to analyze the token's purpose, revenue model, affiliations, and ecosystem "
        "to assess its compliance with Islamic principles."
    ),
    tools=[search_tool, scraper_tool],
    memory=True
)

# 🔹 Risk Assessment Agent
risk_analyst = Agent(
    role="Crypto Risk Assessment Analyst",
    goal="Analyze {token_name}'s market history, trends, and investment risks.",
    backstory=(
        "A seasoned financial analyst specializing in crypto markets. "
        "You conduct in-depth research on token performance, social media sentiment, "
        "news articles, and financial reports to provide risk assessments."
    ),
    tools=[search_tool, scraper_tool],
    memory=True
)

# 🔹 Task: Check Shariah Compliance
check_compliance_task = Task(
    description=(
        "Research the token {token_name} and determine if it complies with Islamic finance principles. "
        "Analyze its revenue model, whether it involves interest-based lending (riba), gambling (maysir), "
        "or unethical industries (e.g., adult content, alcohol, weapons). "
        "Provide a True/False answer on compliance and explain the justification."
    ),
    expected_output="A JSON response with 'IsHalal' (boolean) and 'justification' (string).",
    agent=shariah_analyst,
)

# 🔹 Task: Assess Investment Risks
analyze_risk_task = Task(
    description=(
        "Conduct market research on {token_name}. "
        "Analyze its price history, social media mentions (Twitter), financial reports, and related news articles. "
        "Provide an assessment of whether investing in this token is advisable or risky, along with justification."
    ),
    expected_output="A JSON response with 'riskAssessment' (string).",
    agent=risk_analyst,
)

# 🔹 Crew Configuration
crew = Crew(
    agents=[shariah_analyst, risk_analyst],
    tasks=[check_compliance_task, analyze_risk_task],
    process=Process.sequential,  # ✅ First check compliance, then assess risk
    memory=True,
    verbose=True
)

# ✅ Start Execution
result = crew.kickoff(inputs={"token_name": "Solana"})  # Example input

# ✅ Extract string output from CrewOutput object
if isinstance(result, dict):  # CrewAI may return structured output
    output_text = "\n".join(str(value) for value in result.values())
elif isinstance(result, str):  # Some versions may return string directly
    output_text = result
else:
    raise TypeError(f"Unexpected CrewOutput format: {type(result)}")

# ✅ Process final output safely
final_response = {
    "IsHalal": "true" if "compliant" in output_text.lower() else "false",
    "justification": output_text.split("\n")[0],  # Extract first meaningful line
    "riskAssessment": output_text.split("\n")[1] if "\n" in output_text else "N/A"
}

print(final_response)
