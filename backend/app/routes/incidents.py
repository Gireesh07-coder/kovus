from fastapi import APIRouter
from app.core.database import incidents_collection

router = APIRouter()


@router.get("/incidents")
def get_incidents():

    incidents = []

    for incident in incidents_collection.find():

        incident["_id"] = str(incident["_id"])

        incidents.append(incident)

    return {
        "status": "success",
        "total_incidents": len(incidents),
        "data": incidents
    }