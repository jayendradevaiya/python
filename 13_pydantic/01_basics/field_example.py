from pydantic import BaseModel
from typing import List,Dict,Optional

class Cart(BaseModel):
    user_id : int
    items:List[str]
    quantities : Dict[str, int]

class BlogPost(BaseModel):
    title:str
    contet:str
    image_url:Optional[str] = None

card_data = {
    "user_id":123,
    "items":["Laptop","Mouse","Keyboard"],
    "quantities":{"laptop":1,"Mouse":2,"Keybord":3}
}

cart = Cart(**card_data)
# print(cart)