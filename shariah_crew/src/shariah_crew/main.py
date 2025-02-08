import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

from shariah_crew.crew import crew

def run():
    """Runs the CrewAI workflow"""
    result = crew.kickoff(inputs={"token_name": "Bitcoin"})
    print(result)

if __name__ == "__main__":
    run()

