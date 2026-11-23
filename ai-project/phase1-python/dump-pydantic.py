from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int


product = Product(
    name="Laptop",
    price=50000,
    quantity=2
)

print(product.model_dump())
print(product.model_dump_json())