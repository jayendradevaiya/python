from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street:str
    city : str
    zip_code : str

class User(BaseModel):
    id: int 
    name : str
    email : str
    is_active: bool = True
    CreatedAt: datetime
    address : Address
    tages : List[str] = []

    model_config = ConfigDict(
    json_encoders = {datetime: lambda v :v.strftime('%d-%m-%y %H:%M:%S')}
    )

user = User(
    id = 1,
    name = "Jayendra",
    email = "j@gmail.com",
    CreatedAt = datetime(2024, 3, 15, 14, 30),
    address = Address(
        street = "Something", 
        city = "ahmedabad",
        zip_code="012345"
    ),
    is_active = False,
    tages = ["premium","subscriber"]
)

python_dict = user.model_dump()
print(user)
print("=" * 30) 
print(python_dict)

json_str = user.model_dump_json()
print("=" *30)
print(json_str)