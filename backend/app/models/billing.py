from pydantic import BaseModel

class BillingData(BaseModel):
    service: str
    monthly_cost: int
    cpu_utilization: int
    owner: str | None = None
    monitoring_enabled: bool