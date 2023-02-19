from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: float


external_data = {"count": 100, "size": 30.5}
foo = Foo(**external_data)

print(foo)

breakpoint()