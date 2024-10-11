from fastapi import APIRouter, HTTPException
from bson import ObjectId
from datetime import date
from typing import List
from app.database import items_collection
from app.models.items import ItemModel, UpdateItemModel
from datetime import datetime

router = APIRouter()

@router.post("/items", response_model=ItemModel)
async def create_item(item: ItemModel):
    item_data = item.dict()
    item_data['expiry_date'] = datetime.combine(item.expiry_date, datetime.min.time())
    item_data['insert_date'] = datetime.utcnow()
    new_item = await items_collection.insert_one(item_data)
    return item_data

@router.get("/items/{id}", response_model=ItemModel)
async def get_item(id: str):
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.get("/items/filter", response_model=List[ItemModel])
async def filter_items(email: str = None, expiry_date: date = None, insert_date: date = None, quantity: int = None):
    filters = {}
    
    if email:
        filters["email"] = email
    
    if expiry_date:
        filters["expiry_date"] = {"$gt": datetime.combine(expiry_date, datetime.min.time())}
    
    if insert_date:
        filters["insert_date"] = {"$gt": datetime.combine(insert_date, datetime.min.time())}
    
    if quantity:
        filters["quantity"] = {"$gte": quantity}
    
    items = await items_collection.find(filters).to_list(100)
    return items

@router.get("/items/aggregate")
async def aggregate_items():
    pipeline = [{"$group": {"_id": "$email", "count": {"$sum": 1}}}]
    result = await items_collection.aggregate(pipeline).to_list(100)
    return result

@router.put("/items/{id}")
async def update_item(id: str, item: UpdateItemModel):
    updated_item = await items_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": item.dict(exclude_unset=True)}
    )
    if updated_item.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated"}

@router.delete("/items/{id}")
async def delete_item(id: str):
    deleted_item = await items_collection.delete_one({"_id": ObjectId(id)})
    if deleted_item.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
