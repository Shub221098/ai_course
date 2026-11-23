# from pydantic import BaseModel


# class Product(BaseModel):
#     name: str
#     price: float
#     quantity: int = 1
#     description: str | None = None

# product = Product(
#     name="Laptop",
#     price=50000
# )
# print(product)

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=18, le=100)
    email: EmailStr
    salary: float = Field(gt=0)


user = User(
    name="Shubham",
    age=25,
    email="shubham@gmail.com",
    salary=50000
)

print(user)

user2 = User(
    name="A",
    age=15,
    email="hello",
    salary=-500
)

print(user2)