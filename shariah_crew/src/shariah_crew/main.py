import warnings
from shariah_crew.crew import ShariahCrew

warnings.filterwarnings("ignore", category=SyntaxWarning)

if __name__ == "__main__":
    print("Running Shariah Crew...")
    try:
        result = ShariahCrew.kickoff()
        with open("shariah_report.md", "w", encoding="utf-8") as f:
            f.write(result)
        print("✅ Analysis complete! Results saved in shariah_report.md")
    except Exception as e:
        print(f"❌ Error running the crew: {e}")
