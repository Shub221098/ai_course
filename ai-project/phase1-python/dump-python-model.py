from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int


product_data = {
    "name": "Laptop",
    "price": 50000,
    "quantity": 2
}

product = Product.model_validate(product_data)

print(product)
print(product.name)
print(type(product))

product_json = '{"name": "Laptop", "price": 50000, "quantity": 2}'
product = Product.model_validate_json(product_json)

print(product)
print(product.name)
print(type(product))