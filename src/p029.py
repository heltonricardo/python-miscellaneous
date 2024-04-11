from dataclasses import dataclass, field, asdict, astuple


@dataclass
class Person:
    name: str = "Missing"                            # immutable
    age: int = 1                                     # immutable
    phones: list[str] = field(default_factory=list)  # mutable


if __name__ == "__main__":
    p1 = Person("John", 50)  # dataclass: __init__
    p2 = Person("Mary", 25)
    p3 = Person("John", 50)
    p4 = Person(phones=["123456789", "987654321"])

    print(p1)                # dataclass: __repr__
    print(p2)
    print(p3)
    print(p4)

    print(p1 == p2)          # dataclass: __eq__
    print(p1 == p3)

    print(asdict(p1))
    print(astuple(p1))
