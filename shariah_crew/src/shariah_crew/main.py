# import warnings
# import json
# warnings.filterwarnings("ignore", category=SyntaxWarning)

# from shariah_crew.crew import final_crew

# def run():
#     """Runs the CrewAI workflow"""
#     inputs = {'token_name': 'Solana'}
#     result = final_crew.kickoff(inputs=inputs)

#     # ✅ Extract structured output safely
#     def extract_text(output):
#         """Safely extract and parse JSON output from CrewAI result."""
#         if hasattr(output, "raw_output"):  # CrewOutput object
#             output_text = output.raw_output
#         elif isinstance(output, str):  # If already a string
#             output_text = output
#         elif isinstance(output, dict):  # If structured output
#             return output  # Directly return dict since it's already JSON
#         else:
#             output_text = str(output)  # Convert unknown types to string for safety

#         # Try parsing JSON if the output looks like JSON
#         try:
#             return json.loads(output_text)
#         except json.JSONDecodeError:
#             return {"text": output_text}  # Return raw text if it's not valid JSON

#     # ✅ Process and combine results properly
#     parsed_result = extract_text(result)

#     final_response = {
#         "IsHalal": parsed_result.get("IsHalal", False),  # Default to False if missing
#         "justification": parsed_result.get("justification", "No justification provided."),
#         "riskAssessment": parsed_result.get("riskAssessment", "No risk assessment provided.")
#     }

#     # ✅ Print as JSON (for API response)
#     print(json.dumps(final_response, indent=2))

# # ✅ Ensure script runs properly when executed
# if __name__ == "__main__":
#     run()


# ------------------------------------------


import json
import warnings
from fastapi import FastAPI
from pydantic import BaseModel
from shariah_crew.crew import final_crew

warnings.filterwarnings("ignore", category=SyntaxWarning)

app = FastAPI()

class TokenRequest(BaseModel):
    token_name: str

@app.post("/analyze")
def analyze_token(request: TokenRequest):
    """Runs CrewAI and returns a structured JSON response."""
    result = final_crew.kickoff(inputs={"token_name": request.token_name})
    
    # Extract JSON response
    try:
        response = json.loads(result.raw_output) if hasattr(result, "raw_output") else result
    except json.JSONDecodeError:
        response = {"text": str(result)}

    return {
        "IsHalal": response.get("IsHalal", False),
        "justification": response.get("justification", "No justification provided."),
        "riskAssessment": response.get("riskAssessment", "No risk assessment provided.")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
