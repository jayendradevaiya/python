from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock :bool = True


product_one = Product(id=1, name="Laptop",price=99.99,in_stock=True)

product_two =  Product(id=2, name="Mouse",price=99.99)

# product_three =  Product( name="Mouse") # give error