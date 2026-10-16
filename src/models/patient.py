from sqlalchemy import Column, Integer, String, Date
from src.core.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    national_id = Column(String(20), unique=True, index=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True)  # Nullable por la inyección de defectos del seeder
    phone = Column(String(30), nullable=True)
    date_of_birth = Column(Date, nullable=True)