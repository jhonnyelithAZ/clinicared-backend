from pydantic import BaseModel
from typing import Optional
from datetime import date

class PatientBase(BaseModel):
    national_id: str
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True