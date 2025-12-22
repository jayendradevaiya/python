from typing import Optional
from pydantic import BaseModel,Field

class Emplooyee(BaseModel):
    id : int
    name : str = Field(
        ...,
        min_length = 3,
        min_length = 50,
        discription = "Employee Name",
        examples="Jayendra Devaiya"
    )
    department : Optional[str] = 'General'
    salary : float = Field(
        ...,
        ge=10000
    )


class User(BaseModel):
    email:str = Field(..., regex=r'')
    phone: str = Field(..., regex=r'')
    age : int = Field(...,
                      ge = 0,
                      le=150,
                      discrition ="Age in years",)
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        discrition ="Discount Percentage"
    )