from fastapi import APIRouter
from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

router = APIRouter()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@router.post("/analyze")
def analyze(data: dict):

    prompt = f"""
    Analyze this cloud infrastructure data.

    Return ONLY raw JSON.
    Do NOT use markdown.
    Do NOT use ```json.

    Return this exact format:

    {{
      "severity": "",
      "cloud_waste_detected": true,
      "estimated_savings": "",
      "recommendation": "",
      "reasoning": ""
    }}

    Infrastructure Data:
    {data}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    cleaned_response = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        analysis_json = json.loads(cleaned_response)

        return {
            "status": "success",
            "analysis": analysis_json,
            "received_data": data
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e),
            "raw_analysis": response.text
        }