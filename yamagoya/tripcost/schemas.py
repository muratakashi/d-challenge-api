from datetime import date, datetime

from pydantic import BaseModel


class TripCost(BaseModel):
    id : int
    start_date : date
    end_date : date
    employee_id : int
    purpose : str
    total_amount : int
    remarks : int
    created_at : datetime
    updated_at : datetime
