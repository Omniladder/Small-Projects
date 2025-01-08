from pydantic import BaseModel

class Person(BaseModel):
    name: str
    id: int
    email:str



alice = Person(name="alice",  id=12,  email="alice@gmail.com")

print(alice)