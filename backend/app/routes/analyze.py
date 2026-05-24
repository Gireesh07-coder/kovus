from fastapi import APIRouter
from google import genai
from dotenv import load_dotenv
from app.models.billing import BillingData
from app.routes.incidents import fake_incidents

import os
import json
from datetime import datetime

load_dotenv()

router = APIRouter()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@router.post("/analyze")
def analyze(data: BillingData):

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
    {data.dict()}
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

        incident_data = {
            "input_data": data.dict(),
            "analysis": analysis_json,
            "created_at": datetime.utcnow().isoformat()
        }

        fake_incidents.append(incident_data)

        return {
            "status": "success",
            "analysis": analysis_json,
            "received_data": data.dict()
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e),
            "raw_analysis": response.text
        }