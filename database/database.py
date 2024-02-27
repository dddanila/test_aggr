import motor.motor_asyncio
from config.config import MONGOODB_URI
from datetime import datetime

class Database:
    def __init__(self, uri: str = MONGOODB_URI) -> None:
        self.client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.database = self.client.sample_db
        self.sample_collection = self.database.get_collection("sample_collection")
    
    async def find_data(self, input: dict) -> dict | bool:
        try:
            data = await self.sample_collection.find(
                {"dt": {
                    "$gte": datetime.fromisoformat(
                        input["dt_from"]),
                    "$lte": datetime.fromisoformat(
                        input["dt_upto"])}}).to_list(
                None)
        except ValueError:
            return False
        return data
    