from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional

class ItemModel(BaseModel):
    name: str
    email: EmailStr
    item_name: str
    quantity: int
    expiry_date: date  # It's okay to keep this as date, we'll convert it before saving
    insert_date: datetime = None  # This is added automatically, no need to pass it in the request

class UpdateItemModel(BaseModel):
    name: str = None
    email: EmailStr = None
    item_name: str = None
    quantity: int = None
    expiry_date: date = None
