from pydantic import BaseModel


class StatsRead(BaseModel):
    min: float
    max: float
    count: int
    sum: float
    median: float