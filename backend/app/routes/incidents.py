from fastapi import APIRouter

router = APIRouter()

fake_incidents = []


@router.get("/incidents")
def get_incidents():

    return {
        "status": "success",
        "total_incidents": len(fake_incidents),
        "data": fake_incidents
    }


@router.get("/incidents/high")
def get_high_severity_incidents():

    high_incidents = []

    for incident in fake_incidents:

        severity = incident["analysis"]["severity"]

        if severity.lower() == "high":

            high_incidents.append(incident)

    return {
        "status": "success",
        "total_high_incidents": len(high_incidents),
        "data": high_incidents
    }