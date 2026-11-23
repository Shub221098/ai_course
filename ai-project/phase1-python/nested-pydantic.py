# from pydantic import BaseModel


# class Address(BaseModel):
#     city: str
#     pincode: int


# class User(BaseModel):
#     name: str
#     age: int
#     address: Address

# user = User(
#     name="Shubham",
#     age=25,
#     address={
#         "city": "Surat",
#         "pincode": 395001
#     }
# )

# user2 = User(
#     name=10,
#     age="Shubham",
#     address={
#         "city": "Surat",
#         "pincode": "395001"
#     }
# )

# print(user)
# print(user.address.city)
# print("-"*10)
# print(user2)
# print(user2.address.city)


from pydantic import BaseModel


class Item(BaseModel):
    name: str
    quantity: int
    price: float


class Cart(BaseModel):
    customer: str
    items: list[Item]

cart = Cart(
    customer="Shubham",
    items=[
        {"name": "Laptop", "quantity": 1, "price": 50000},
        {"name": "Mouse", "quantity": 2, "price": 500}
    ]
)

print(cart)
print(cart.items)
print(cart.items[0].name)

cart2_data = {
    "customer": "Shubham",
    "items": [
        {
            "name": 1,
            "quantity": 2,
            "price": 1000
        }
    ]
}

breakpoint()

cart2 = Cart(**cart2_data)
