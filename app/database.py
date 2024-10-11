from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"  # Use MongoDB Atlas connection string or localhost

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client['TestDB']

# Collections
items_collection = database.get_collection('Items')
clock_in_collection = database.get_collection('User_Clock_In_Records')
