from database.database import Database
from dateutil.relativedelta import relativedelta
from datetime import (
    datetime,
    timedelta
)
from database.models import Dataset

class Aggregation(Database):
    async def aggregate_data(self, to_aggregation_input: dict) -> Dataset:
        list_salary = []
        list_date = []
        data_list = await self.find_data(to_aggregation_input)
        
        if not data_list:
            raise ValueError("Data not found")
        
        dt_from = datetime.fromisoformat(to_aggregation_input["dt_from"])
        dt_upto = datetime.fromisoformat(to_aggregation_input["dt_upto"])

        if to_aggregation_input["group_type"] == "month":
            step = relativedelta(months=1)
        elif to_aggregation_input["group_type"] == "day":
            step = timedelta(days=1)
        elif to_aggregation_input["group_type"] == "hour":
            step = timedelta(hours=1)
        else:
            raise ValueError("Invalid group_type")
        
        while dt_from <= dt_upto:
            list_date.append(dt_from.isoformat())
            total_salary = sum([item["value"] for item in data_list if self.check_date(item["dt"], dt_from, to_aggregation_input["group_type"])])
            list_salary.append(total_salary)
            dt_from += step
        
        return Dataset(list_salary, list_date)

    def check_date(self, item_dt, current_dt, group_type):
        if group_type == "month":
            return item_dt.year == current_dt.year and item_dt.month == current_dt.month
        elif group_type == "day":
            return item_dt.year == current_dt.year and item_dt.month == current_dt.month and item_dt.day == current_dt.day
        elif group_type == "hour":
            return item_dt.year == current_dt.year and item_dt.month == current_dt.month and item_dt.day == current_dt.day and item_dt.hour == current_dt.hour
        else:
            return False