from fastapi import APIRouter
from app.routes.incidents import fake_incidents

router = APIRouter()


@router.get("/stats")
def get_stats():

    total_incidents = len(fake_incidents)

    high_incidents = 0

    total_estimated_savings = 0

    for incident in fake_incidents:

        severity = incident["analysis"]["severity"]

        if severity.lower() == "high":
            high_incidents += 1

        savings_text = incident["analysis"]["estimated_savings"]

        digits = ""

        for char in savings_text:

            if char.isdigit():
                digits += char

        if digits:
            total_estimated_savings += int(digits)

    return {
        "status": "success",
        "stats": {
            "total_incidents": total_incidents,
            "high_severity_incidents": high_incidents,
            "total_estimated_savings": total_estimated_savings
        }
    }