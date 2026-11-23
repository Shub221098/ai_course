# 🐍 Python Phase 1 — Complete Revision Master Notes

> **Goal:** Python fundamentals strong enough for Backend + AI/GenAI development.

---

# 1. Python Basics

## Variables

Python mein variable actually object ko point karne wala **name/reference** hai.

```python
name = "Shubham"
age = 25
price = 99.50
is_active = True
```

Common types:

```python
str
int
float
bool
None
list
tuple
set
dict
```

Check type:

```python
print(type(age))
# <class 'int'>
```

### Important

Python dynamically typed hai:

```python
x = 10
x = "hello"
```

Valid hai.

---

# 2. Operators

## Arithmetic

```python
a = 10
b = 3

a + b    # 13
a - b    # 7
a * b    # 30
a / b    # 3.333...
a // b   # 3
a % b    # 1
a ** b   # 1000
```

## Comparison

```python
10 == 10   # True
10 != 5    # True
10 > 5     # True
10 < 5     # False
```

## Logical

```python
True and False   # False
True or False    # True
not True         # False
```

---

# 3. Conditions

```python
age = 20

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

Python indentation significant hai.

🔥 **Indentation = syntax ka part.**

---

# 4. Loops

## for

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

## while

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

## break

Loop immediately stop:

```python
for i in range(10):
    if i == 5:
        break
```

## continue

Current iteration skip:

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

---

# 5. Functions

```python
def add(a, b):
    return a + b
```

Call:

```python
result = add(10, 20)
print(result)
```

## Default argument

```python
def greet(name="Guest"):
    return f"Hello {name}"
```

## Keyword arguments

```python
greet(name="Shubham")
```

## `*args`

Multiple positional arguments:

```python
def total(*numbers):
    return sum(numbers)

total(10, 20, 30)
```

## `**kwargs`

Multiple keyword arguments:

```python
def user_info(**data):
    print(data)

user_info(name="Shubham", age=25)
```

---

# 6. Lambda

Small anonymous function:

```python
square = lambda x: x * x

print(square(5))
# 25
```

Usually simple transformations ke liye.

---

# 7. `map()`, `filter()`, `reduce()`

## map

Har item transform:

```python
numbers = [1, 2, 3]

result = list(map(lambda x: x * 2, numbers))

print(result)
# [2, 4, 6]
```

## filter

Condition satisfy karne wale items:

```python
numbers = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
# [2, 4]
```

## reduce

Multiple values ko gradually combine:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)

print(result)
# 10
```

---

# 8. First-Class Functions

Python functions ko variable ki tarah treat kar sakta hai.

```python
def greet():
    return "Hello"

func = greet

print(func())
```

Function ko argument bhi pass kar sakte hain:

```python
def execute(func):
    return func()

execute(greet)
```

---

# 9. Closures

Inner function outer function ke variable ko remember karta hai.

```python
def multiplier(x):

    def multiply(y):
        return x * y

    return multiply


double = multiplier(2)

print(double(5))
# 10
```

🔥 `multiply()` ne `x` ko remember kiya.

---

# 10. Decorators

Existing function ka behavior modify/extend karna.

```python
def logger(func):

    def wrapper():
        print("Function started")
        result = func()
        print("Function finished")
        return result

    return wrapper


@logger
def greet():
    print("Hello")


greet()
```

Backend mein useful:

```text
Authentication
Logging
Authorization
Timing
Caching
```

---

# 11. LIST

List ordered + mutable collection hai.

```python
users = ["A", "B", "C"]
```

Index:

```python
users[0]    # A
users[-1]   # C
```

Modify:

```python
users[0] = "Shubham"
```

## Common methods

```python
users.append("D")
users.insert(1, "X")
users.extend(["E", "F"])

users.remove("X")
users.pop()
del users[0]
```

## Slicing

```python
numbers = [0, 1, 2, 3, 4]

numbers[1:4]
# [1, 2, 3]

numbers[::-1]
# reverse
```

## Sorting

```python
numbers.sort()
```

Changes original list.

```python
sorted_numbers = sorted(numbers)
```

Creates sorted result.

## List comprehension

```python
squares = [x * x for x in range(5)]
```

Result:

```python
[0, 1, 4, 9, 16]
```

---

# 12. LIST REFERENCES

Important memory concept:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
# [1, 2, 3, 4]
```

Because `a` and `b` same object ko reference kar rahe hain.

---

# 13. Tuple

Tuple ordered + immutable hai.

```python
user = ("Shubham", 25)
```

Indexing:

```python
user[0]
```

But:

```python
user[0] = "Rahul"
```

❌ Error.

## Tuple unpacking

```python
name, age = user
```

---

# 14. SET

Set unique values store karta hai.

```python
numbers = {1, 2, 3, 3}

print(numbers)
# {1, 2, 3}
```

No normal indexing:

```python
numbers[0]
```

❌

## Methods

```python
numbers.add(4)
numbers.remove(2)
numbers.discard(10)
```

## Set operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b        # union
a & b        # intersection
a - b        # difference
a ^ b        # symmetric difference
```

### Empty set trap

```python
{}
```

is an empty dictionary.

Empty set:

```python
set()
```

---

# 15. DICTIONARY

Key-value structure:

```python
user = {
    "name": "Shubham",
    "age": 25
}
```

Access:

```python
user["name"]
```

Safer:

```python
user.get("name")
```

## Add/update

```python
user["city"] = "Surat"
user["age"] = 26
```

## Remove

```python
user.pop("age")
del user["city"]
```

## Iterate

```python
for key, value in user.items():
    print(key, value)
```

Useful:

```python
user.keys()
user.values()
user.items()
```

## Dict comprehension

```python
squares = {x: x*x for x in range(5)}
```

---

# 16. Nested Data Structures

Real APIs mein common:

```python
user = {
    "name": "Shubham",
    "orders": [
        {
            "id": 1,
            "amount": 500
        },
        {
            "id": 2,
            "amount": 1000
        }
    ]
}
```

JSON/API response ka Python representation often isi type ka hota hai.

---

# 17. Mutable vs Immutable

## Mutable

Object change ho sakta hai:

```text
list
dict
set
```

Example:

```python
numbers = [1, 2]

numbers.append(3)
```

Same object change hua.

## Immutable

Object change nahi hota:

```text
int
float
str
bool
tuple
```

Example:

```python
x = 10
x = 20
```

Purana `10` object modify nahi hua; `x` naye object ko refer kar raha hai.

---

# 18. `==` vs `is`

## `==`

Values compare:

```python
[1, 2] == [1, 2]
# True
```

## `is`

Same object check:

```python
a = [1, 2]
b = [1, 2]

a is b
# False
```

🔥 Rule:

```text
== → same value?
is → same object?
```

`is` especially `None` ke saath:

```python
if value is None:
    ...
```

---

# 19. `id()`

Object identity dekhne ke liye:

```python
x = []
y = x

print(id(x))
print(id(y))
```

Same object hone par same `id`.

---

# 20. Shallow Copy vs Deep Copy

## Shallow copy

```python
import copy

a = [[1, 2], [3, 4]]

b = copy.copy(a)
```

Outer object copy hota hai, nested objects shared ho sakte hain.

## Deep copy

```python
b = copy.deepcopy(a)
```

Nested objects bhi recursively copy.

🔥 Nested mutable data ke liye difference important hai.

---

# 21. Function Arguments — Mutation vs Reassignment

Python arguments mein object reference/value binding concept use karta hai.

Example:

```python
def add_item(items):
    items.append("new")


data = []

add_item(data)

print(data)
# ["new"]
```

Function ne same mutable object modify kiya.

But:

```python
def change(items):
    items = ["new"]


data = ["old"]

change(data)

print(data)
# ["old"]
```

Yahan local `items` ko new object assign hua.

---

# 22. Mutable Default Argument Trap

❌ Avoid:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Default list function calls ke beech shared ho sakti hai.

✅ Correct:

```python
def add_item(item, items=None):

    if items is None:
        items = []

    items.append(item)

    return items
```

🔥 Interview favourite trap.

---

# 23. `None`

`None` means absence of value.

```python
result = None
```

Check:

```python
if result is None:
    print("No result")
```

Prefer:

```python
is None
```

instead of:

```python
== None
```

---

# 24. Truthy / Falsy

Falsy values include:

```python
False
None
0
0.0
""
[]
{}
set()
```

Example:

```python
items = []

if not items:
    print("Empty")
```

---

# 25. `and` / `or` Return Values

Python mein ye sirf True/False nahi return karte.

```python
result = "hello" or "world"

print(result)
# hello
```

```python
result = "" or "Guest"

print(result)
# Guest
```

Common default pattern:

```python
name = user_name or "Guest"
```

---

# 26. `*` and `**` Unpacking

## List unpacking

```python
numbers = [1, 2, 3]

print(*numbers)
```

Equivalent concept:

```text
1 2 3
```

## Dictionary unpacking

```python
data = {
    "name": "Shubham",
    "age": 25
}

print(**data)
```

`**` keyword arguments/dictionaries ke context mein use hota hai.

Also:

```python
new_user = {
    **data,
    "city": "Surat"
}
```

---

# 27. Memory / Object Model

Important mental model:

```text
Variable
   ↓
Reference/name
   ↓
Object in memory
```

Example:

```python
a = [1, 2]
b = a
```

Conceptually:

```text
a ─────┐
       ↓
    [1, 2]
       ↑
       └───── b
```

---

# 28. Class & Object

Class = blueprint.

Object = class ka instance.

```python
class User:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"


user = User("Shubham")

print(user.greet())
```

---

# 29. `self`

`self` current object ko refer karta hai.

```python
class User:

    def __init__(self, name):
        self.name = name
```

Different objects:

```python
u1 = User("A")
u2 = User("B")
```

Each object ka apna `name`.

---

# 30. Instance Variable vs Class Variable

```python
class User:

    company = "Karma"

    def __init__(self, name):
        self.name = name
```

```text
company → class variable
name    → instance variable
```

---

# 31. `@classmethod`

Class ko access karta hai.

```python
class User:

    def __init__(self, name):
        self.name = name

    @classmethod
    def guest(cls):
        return cls("Guest")
```

Call:

```python
user = User.guest()
```

Common use:

**Alternative constructors.**

---

# 32. `@staticmethod`

Class/object state ki requirement nahi.

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b
```

Call:

```python
Math.add(10, 20)
```

---

# 33. Inheritance

Parent → Child relationship.

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def bark(self):
        print("Woof")
```

```python
dog = Dog()

dog.speak()
dog.bark()
```

---

# 34. `super()`

Parent implementation access:

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)
```

🔥 `super()` directly "parent object" nahi hota; it follows the MRO.

---

# 35. Method Overriding

Child parent method ko redefine kar sakta hai.

```python
class Animal:

    def speak(self):
        print("Animal")


class Dog(Animal):

    def speak(self):
        print("Dog")
```

---

# 36. Types of Inheritance

Important names:

```text
Single
Multilevel
Multiple
Hierarchical
```

Multiple inheritance:

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

---

# 37. MRO — Method Resolution Order

Multiple inheritance mein Python decide karta hai method kahan se milega.

```python
print(C.__mro__)
```

MRO generally follows Python's C3 linearization.

🔥 Important:

```python
super()
```

MRO follow karta hai.

---

# 38. IS-A vs HAS-A vs USES-A

### IS-A

Inheritance:

```text
Dog IS-A Animal
```

### HAS-A

Composition/aggregation:

```text
Order HAS-A PaymentService
```

### USES-A

Dependency:

```text
Controller USES Service
```

Backend architecture mein composition/dependency injection frequently inheritance se better hota hai.

---

# 39. Polymorphism

Same interface, different behavior.

```python
class Dog:

    def speak(self):
        return "Woof"


class Cat:

    def speak(self):
        return "Meow"


animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```

Same:

```python
animal.speak()
```

Different behavior.

---

# 40. Duck Typing

Python mein object ka exact type important nahi; required behavior available hona important ho sakta hai.

```python
class Duck:

    def speak(self):
        return "Quack"


class Person:

    def speak(self):
        return "Hello"


def make_speak(obj):
    print(obj.speak())
```

Both work because both provide `speak()`.

Mental model:

```text
"If it behaves like what I need,
I can use it."
```

---

# 41. Encapsulation

Python mein:

### Public

```python
self.name
```

### Protected convention

```python
self._name
```

Means:

> internal use convention.

### Private/name mangling

```python
self.__password
```

Python internally name-mangles it.

🔥 Python mein `private` Java/C++ jaisa strict access-control mechanism nahi hai.

---

# 42. `@property`

Getter ko attribute jaisa use karna.

```python
class User:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

Use:

```python
user.age
```

Setter:

```python
@age.setter
def age(self, value):
    if value < 0:
        raise ValueError("Invalid age")

    self._age = value
```

---

# 43. Abstraction

Required interface define karna, implementation hide karna.

```python
from abc import ABC, abstractmethod


class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Concrete class:

```python
class RazorpayGateway(PaymentGateway):

    def pay(self, amount):
        return f"Paid {amount}"
```

Abstract class ka direct object nahi bana sakte if abstract methods remain unimplemented.

---

# 44. `Protocol`

Structural typing / interface-like design.

Concept:

```python
from typing import Protocol


class PaymentGateway(Protocol):

    def pay(self, amount: float) -> bool:
        ...
```

Jo class required method provide karti hai, wo compatible ho sakti hai without explicit inheritance.

---

# 45. Dunder / Magic Methods

Special methods double underscores se:

```python
__init__
__str__
__repr__
__len__
__eq__
__add__
__call__
__getitem__
```

## `__str__`

Human-readable representation:

```python
class User:

    def __str__(self):
        return "User object"
```

## `__repr__`

Developer/debug representation.

## `__len__`

```python
class Cart:

    def __len__(self):
        return 5
```

Then:

```python
len(cart)
```

## `__add__`

Custom `+` behavior.

---

# 46. `__new__` vs `__init__`

Object creation lifecycle:

```text
__new__()
   ↓
object created
   ↓
__init__()
   ↓
object initialized
```

`__new__` object create karta hai.

`__init__` created object initialize karta hai.

---

# 47. `__slots__`

```python
class User:

    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Object attributes ko restrict karne aur memory optimization ke liye useful ho sakta hai.

---

# 48. `@dataclass`

Data-heavy classes ke liye boilerplate reduce karta hai.

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
```

Automatically useful methods generate ho sakte hain, such as:

```text
__init__
__repr__
__eq__
```

---

# 49. Composition + Dependency Injection

Backend pattern:

```text
Controller
    ↓
Service
    ↓
Repository
    ↓
Database
```

Example:

```python
class OrderService:

    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def create_order(self, amount):
        return self.payment_gateway.pay(amount)
```

Gateway inject:

```python
gateway = RazorpayGateway()

service = OrderService(gateway)
```

🔥 Benefit:

Testing mein fake gateway inject kar sakte ho.

---

# 50. Exception Handling

Basic:

```python
try:
    value = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# 51. `else` and `finally`

```python
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Success")

finally:
    print("Always executes")
```

### Flow

```text
try
 ↓
error?
 ├── yes → except
 └── no  → else
 ↓
finally
```

---

# 52. Specific Exceptions

Prefer:

```python
except ValueError:
```

instead of blindly:

```python
except:
```

Can capture:

```python
except Exception as e:
    print(e)
```

🔥 Avoid bare `except` unless you have a very specific reason.

---

# 53. `raise`

Manually exception raise:

```python
age = -1

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

# 54. Custom Exception

```python
class InsufficientBalanceError(Exception):
    pass
```

Use:

```python
raise InsufficientBalanceError("Not enough balance")
```

---

# 55. Exception Chaining

```python
try:
    value = int("abc")

except ValueError as e:
    raise RuntimeError("Invalid user input") from e
```

`from e` preserves original cause.

Useful in backend layers.

---

# 56. Backend Error Mapping

Concept:

```text
Database error
      ↓
Repository
      ↓
Service-level exception
      ↓
API layer
      ↓
HTTP response
```

Example:

```text
ValidationError → 400
Authentication error → 401
Authorization error → 403
Not found → 404
Unexpected server error → 500
```

---

# 57. File Handling

Open:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

🔥 `with` automatically handles closing the file.

Modes:

```text
r → read
w → write
a → append
x → create
b → binary
```

---

# 58. File Reading

```python
file.read()
```

Whole content.

```python
file.readline()
```

One line.

```python
file.readlines()
```

Lines list.

---

# 59. `pathlib`

Modern path handling:

```python
from pathlib import Path

path = Path("data.txt")

print(path.exists())
print(path.name)
print(path.suffix)
```

Useful:

```python
Path("data").mkdir(exist_ok=True)
```

---

# 60. JSON

Python object → JSON:

```python
import json

data = {
    "name": "Shubham",
    "age": 25
}

json_string = json.dumps(data)
```

JSON → Python:

```python
data = json.loads(json_string)
```

File:

```python
json.dump(data, file)
```

Read file:

```python
data = json.load(file)
```

### Remember

```text
loads → string
load  → file

dumps → string
dump  → file
```

---

# 61. AI/RAG Connection — Files → AI

Basic RAG pipeline:

```text
Documents
   ↓
Read files
   ↓
Extract text
   ↓
Chunk text
   ↓
Embeddings
   ↓
Vector Database
   ↓
Retrieve relevant chunks
   ↓
LLM
   ↓
Answer
```

File handling is therefore directly relevant to AI.

---

# 62. Modules

A `.py` file can be a module.

Example:

```text
math_utils.py
```

Contains:

```python
def add(a, b):
    return a + b
```

Another file:

```python
from math_utils import add

print(add(10, 20))
```

---

# 63. Packages

Package = organized collection of Python modules.

Typical AI project:

```text
ai_project/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   └── utils/
│
├── tests/
└── requirements.txt
```

---

# 64. Virtual Environment

Create:

```bash
python3 -m venv .venv
```

Activate on Linux:

```bash
source .venv/bin/activate
```

Deactivate:

```bash
deactivate
```

Purpose:

```text
Project A
   ↓
dependencies

Project B
   ↓
different dependencies
```

They don't interfere.

---

# 65. pip

Install:

```bash
pip install pydantic
```

Multiple:

```bash
pip install fastapi uvicorn
```

Remove:

```bash
pip uninstall package_name
```

---

# 66. requirements.txt

Export:

```bash
pip freeze > requirements.txt
```

Install:

```bash
pip install -r requirements.txt
```

Typical project:

```text
project/
├── .venv/
├── requirements.txt
├── .gitignore
└── app/
```

Don't commit `.venv`.

---

# 67. Type Hints

Type hint:

```python
name: str
age: int
```

Function:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Important:

🔥 Type hints **automatically runtime validation nahi karte**.

```python
def add(a: int, b: int):
    return a + b

add("10", "20")
```

Python itself type hint enforce nahi karta.

---

# 68. Collections Type Hints

```python
numbers: list[int]
```

```python
users: list[str]
```

```python
scores: dict[str, int]
```

---

# 69. Union / Optional

Modern Python:

```python
name: str | None
```

Means:

```textstr OR None
```

Example:

```python
def find_user() -> str | None:
    ...
```

---

# 70. `Any`

```python
from typing import Any

data: Any
```

Means essentially:

> Type checking ko specific restriction mat do.

Use carefully.

---

# 71. `TypedDict`

Dictionary ke expected structure ko describe karne ke liye:

```python
from typing import TypedDict


class User(TypedDict):
    name: str
    age: int
```

Again:

🔥 `TypedDict` runtime validation nahi karta.

---

# 72. Type Hints vs Pydantic

Very important:

```text
Type Hints
    ↓
Developer/tooling ko expected type batate hain

Pydantic
    ↓
Runtime validation
```

---

# 73. Pydantic

Install:

```bash
pip install pydantic
```

Basic model:

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
```

Create:

```python
user = User(
    name="Shubham",
    age=25
)
```

---

# 74. Required vs Default

Required:

```python
class User(BaseModel):
    name: str
```

Default:

```python
class User(BaseModel):
    name: str = "Guest"
```

---

# 75. Optional Pydantic Field

```python
class User(BaseModel):
    name: str
    nickname: str | None = None
```

---

# 76. `Field`

Validation constraints:

```python
from pydantic import BaseModel, Field


class Product(BaseModel):

    name: str = Field(min_length=3)

    price: float = Field(gt=0)

    quantity: int = Field(ge=1)
```

Examples:

```text
gt → greater than
ge → greater than or equal
lt → less than
le → less than or equal
```

---

# 77. `EmailStr`

```python
from pydantic import BaseModel, EmailStr


class User(BaseModel):

    name: str
    email: EmailStr
```

Invalid email → validation error.

---

# 78. Nested Pydantic Models

```python
class Item(BaseModel):
    name: str
    price: float


class Cart(BaseModel):
    customer: str
    items: list[Item]
```

Input:

```python
cart = Cart(
    customer="Shubham",
    items=[
        {
            "name": "Laptop",
            "price": 50000
        },
        {
            "name": "Mouse",
            "price": 1000
        }
    ]
)
```

---

# 79. Pydantic Serialization

Model → dictionary:

```python
cart.model_dump()
```

Model → JSON:

```python
cart.model_dump_json()
```

Dictionary → model:

```python
User.model_validate(data)
```

---

# 80. Validation Error Reading

Example:

```text
items.0.name
```

means:

```text
items
 ↓
index 0
 ↓
name
```

So first item ka `name`.

```text
items.1.quantity
```

means second item ka quantity.

🔥 Traceback/validation error ko bottom-to-top read karna useful hai.

---

# 81. Debugging Basics

First inspect:

```python
print(variable)
print(type(variable))
```

Use:

```python
breakpoint()
```

Then debugger:

```text
breakpoint
   ↓
inspect variables
   ↓
step over
   ↓
step into
   ↓
call stack
```

---

# 82. Common Python Errors

### SyntaxError

Code syntax wrong.

### NameError

Variable/name doesn't exist.

### TypeError

Wrong type/operation.

### ValueError

Correct type but invalid value.

### KeyError

Dictionary key missing.

### IndexError

List index invalid.

### AttributeError

Object mein requested attribute/method nahi.

### FileNotFoundError

File path doesn't exist.

### Pydantic ValidationError

Input model rules satisfy nahi karta.

---

# 83. FastAPI + Pydantic

Install:

```bash
pip install fastapi uvicorn
```

Basic API:

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    email: EmailStr


@app.post("/users")
def create_user(user: User):

    return {
        "message": "User created successfully",
        "user": user.model_dump()
    }
```

Run:

```bash
uvicorn main:app --reload
```

Swagger:

```text
/docs
```

---

# 84. JSON Parsing vs Pydantic Validation

These are different stages.

```text
HTTP Request
     ↓
JSON parsing
     ↓
Pydantic validation
     ↓
FastAPI endpoint
```

Example error:

```text
json_invalid
Extra data
```

means JSON itself is invalid.

For example:

```json
{"name": "A"}{"name": "B"}
```

One body mein do JSON objects invalid hain.

Correct:

```json
{
  "name": "A"
}
```

---

# 85. Async/Await

Async function:

```python
async def get_user():
    ...
```

Coroutine function hai.

---

# 86. `await`

```python
result = await get_user()
```

Async operation ke result ka wait.

Mental model:

```text
await
 ↓
wait for async operation
 ↓
event loop can handle other async work
```

---

# 87. `asyncio.run()`

Async program start:

```python
import asyncio


async def main():
    print("Hello")


asyncio.run(main())
```

---

# 88. Sequential Async

```python
async def main():

    await task1()
    await task2()
```

Conceptually:

```text
task1
 ↓
finish
 ↓
task2
 ↓
finish
```

---

# 89. `asyncio.gather()`

Multiple independent async tasks:

```python
user, orders = await asyncio.gather(
    get_user(),
    get_orders()
)
```

If:

```text
user = 2 sec
orders = 1 sec
```

approximately:

```text
max(2, 1) = 2 sec
```

instead of:

```text
2 + 1 = 3 sec
```

---

# 90. Important `gather()` Rule

Three different concepts:

```text
Start order
Completion order
Result order
```

Example:

```python
user, orders, notifications = await asyncio.gather(
    get_user(),          # 2 sec
    get_orders(),        # 1 sec
    get_notifications()  # 1.5 sec
)
```

Completion:

```text
orders
   ↓
notifications
   ↓
user
```

But results:

```text
user
orders
notifications
```

because `gather()` returns results according to input order.

---

# 91. `asyncio.create_task()`

Schedule coroutine as a task:

```python
task = asyncio.create_task(get_user())

# do other async work

result = await task
```

Mental model:

```text
create_task()
     ↓
schedule task
     ↓
continue other work
     ↓
await task
     ↓
get result
```

Important:

`create_task()` requires a **running event loop**, so it is normally used inside an async context.

```python
async def main():

    task = asyncio.create_task(get_user())

    result = await task
```

Started by:

```python
asyncio.run(main())
```

---

# 92. `gather()` vs `create_task()`

### `gather()`

When you want multiple results together:

```python
results = await asyncio.gather(
    task1(),
    task2(),
    task3()
)
```

### `create_task()`

When you want to schedule a task now and await it later:

```python
task = asyncio.create_task(task1())

# other work

result = await task
```

---

# 93. Async Exception Handling

```python
try:

    results = await asyncio.gather(
        task1(),
        task2()
    )

except Exception as e:

    print(e)
```

---

# 94. `return_exceptions=True`

If individual errors ko result ke form mein handle karna ho:

```python
results = await asyncio.gather(
    task1(),
    task2(),
    task3(),
    return_exceptions=True
)
```

Then:

```python
for result in results:

    if isinstance(result, Exception):
        print("Failed:", result)
    else:
        print("Success:", result)
```

---

# 95. Async HTTP — `httpx`

Install:

```bash
pip install httpx
```

Basic:

```python
import asyncio
import httpx


async def get_post():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            "https://jsonplaceholder.typicode.com/posts/1"
        )

        print(response.status_code)
        print(response.json())


asyncio.run(get_post())
```

Important:

```python
await client.get(...)
```

Network response ka wait async way mein.

---

# 96. Multiple Async HTTP Calls

```python
async def get_post(client, post_id):

    response = await client.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    )

    return response.json()


async def main():

    async with httpx.AsyncClient() as client:

        results = await asyncio.gather(
            get_post(client, 1),
            get_post(client, 2),
            get_post(client, 3)
        )

        print(results)
```

---

# 97. Async FastAPI

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()


async def get_user():
    await asyncio.sleep(2)
    return {"name": "Shubham"}


async def get_orders():
    await asyncio.sleep(1)
    return [{"id": 1}]


@app.get("/dashboard")
async def dashboard():

    user, orders = await asyncio.gather(
        get_user(),
        get_orders()
    )

    return {
        "user": user,
        "orders": orders
    }
```

---

# 98. Async ka Main Use

Best for I/O:

```text
HTTP APIs
Database
Redis
LLM APIs
Vector DB
Network
```

🔥 Async automatically CPU-heavy code ko parallel nahi banata.

---

# 99. AI/GenAI Connection

Future AI backend:

```text
User Request
     ↓
FastAPI
     ↓
┌───────────────┬────────────────┐
│ Vector Search │ User Context   │
└───────────────┴────────────────┘
          ↓
       Combine
          ↓
         LLM
          ↓
       Response
```

Independent network operations:

```python
results = await asyncio.gather(
    vector_search(),
    get_user_context()
)
```

This is where your Python async knowledge becomes directly useful in AI systems.

---

# 🔥 PHASE 1 — FINAL MENTAL MAP

```text
PYTHON
│
├── Basics
│   ├── Variables
│   ├── Types
│   ├── Conditions
│   └── Loops
│
├── Functions
│   ├── args / kwargs
│   ├── lambda
│   ├── map/filter/reduce
│   ├── closures
│   └── decorators
│
├── Data Structures
│   ├── List
│   ├── Tuple
│   ├── Set
│   └── Dictionary
│
├── Python Internals
│   ├── References
│   ├── id()
│   ├── is vs ==
│   ├── Mutable vs Immutable
│   ├── Copy / Deepcopy
│   ├── None
│   ├── Truthy/Falsy
│   └── * / **
│
├── OOP
│   ├── Class/Object
│   ├── Inheritance
│   ├── Polymorphism
│   ├── Duck Typing
│   ├── Encapsulation
│   ├── Abstraction
│   ├── Dunder Methods
│   ├── Composition
│   ├── Dependency Injection
│   ├── Dataclass
│   ├── Protocol
│   └── MRO
│
├── Exceptions
│   ├── try
│   ├── except
│   ├── else
│   ├── finally
│   ├── raise
│   └── custom exceptions
│
├── Files
│   ├── File handling
│   ├── pathlib
│   └── JSON
│
├── Environment
│   ├── Modules
│   ├── Packages
│   ├── venv
│   ├── pip
│   └── requirements.txt
│
├── Backend Foundation
│   ├── Type Hints
│   ├── Pydantic
│   ├── FastAPI
│   └── Debugging
│
└── Async Python
    ├── async def
    ├── await
    ├── asyncio.run()
    ├── gather()
    ├── create_task()
    ├── async exceptions
    ├── httpx
    └── FastAPI async endpoints
```

# 🎯 Phase 1 → Phase 2

Ab Phase 1 ka target:

> **"Python syntax yaad karna" nahi, balki Python mein backend/AI code samajhne aur likhne ki foundation banana.**

Next phase:

```text
Phase 2
   ↓
NumPy
   ↓
Pandas
   ↓
Data Handling
   ↓
Matplotlib / Visualization
   ↓
ML Fundamentals
   ↓
PyTorch
   ↓
Transformers
   ↓
Hugging Face
   ↓
Embeddings
   ↓
RAG
   ↓
Agents
```

**Phase 1 complete ✅**

Is note ko apna **quick-revision master sheet** samajh. Jab bhi Phase 1 revise karna ho, especially 🔥 marked concepts ko pehle dekhna.