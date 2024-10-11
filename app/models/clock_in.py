from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Clock-In Pydantic Model for request/response
class ClockInModel(BaseModel):
    email: EmailStr
    location: str

class UpdateClockInModel(BaseModel):
    location: Optional[str]
