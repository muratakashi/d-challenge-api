from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

from ..db.database import BASE


class TripCost(BASE):
    __tablename__ = "tripcost"
    
    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    employee_id = Column(Integer)
    purpose = Column(String)
    total_amount = Column(Integer)
    remarks = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

