import enum


class Direction(enum.Enum):
    NORTH = 1
    SOUTH = 2
    EAST = enum.auto()
    WEST = 4


def move(direction):
    if isinstance(direction, Direction):
        print("Moving", direction.name.lower(), f"({direction.value})")
    else:
        print("Invalid direction")


move(Direction.NORTH)
move(Direction.SOUTH)
move(Direction.EAST)
move(Direction.WEST)
move("UP")
