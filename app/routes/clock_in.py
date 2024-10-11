from fastapi import APIRouter, HTTPException
from bson import ObjectId
from typing import List
from datetime import datetime
from app.database import clock_in_collection
from app.models.clock_in import ClockInModel, UpdateClockInModel

router = APIRouter()

@router.post("/clock-in", response_model=ClockInModel)
async def create_clock_in(clock_in: ClockInModel):
    clock_in_data = clock_in.dict()
    clock_in_data['insert_datetime'] = datetime.utcnow()  # Automatically add insert datetime
    new_clock_in = await clock_in_collection.insert_one(clock_in_data)
    return clock_in_data

@router.get("/clock-in", response_model=List[ClockInModel])
async def get_all_clock_in():
    clock_in_records = await clock_in_collection.find().to_list() 
    return clock_in_records


@router.get("/clock-in/{id}", response_model=ClockInModel)
async def get_clock_in(id: str):
    clock_in_record = await clock_in_collection.find_one({"_id": ObjectId(id)})
    if clock_in_record:
        return clock_in_record
    raise HTTPException(status_code=404, detail="Clock-In record not found")

@router.get("/clock-in/filter", response_model=List[ClockInModel])
async def filter_clock_ins(email: str = None, location: str = None, insert_datetime: datetime = None):
    filters = {}
    if email:
        filters["email"] = email
    if location:
        filters["location"] = location
    if insert_datetime:
        filters["insert_datetime"] = {"$gt": insert_datetime}
    
    clock_ins = await clock_in_collection.find(filters).to_list(100)
    return clock_ins

@router.put("/clock-in/{id}")
async def update_clock_in(id: str, clock_in: UpdateClockInModel):
    updated_clock_in = await clock_in_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": clock_in.dict(exclude_unset=True)}
    )
    if updated_clock_in.matched_count == 0:
        raise HTTPException(status_code=404, detail="Clock-In record not found")
    return {"message": "Clock-In record updated"}

@router.delete("/clock-in/{id}")
async def delete_clock_in(id: str):
    deleted_clock_in = await clock_in_collection.delete_one({"_id": ObjectId(id)})
    if deleted_clock_in.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Clock-In record not found")
    return {"message": "Clock-In record deleted"}
