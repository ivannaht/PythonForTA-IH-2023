""" task 1_3"""


def to_minutes(hours) -> float:
    """calculate minutes in hours"""
    return hours * 60


def to_hours(minutes) -> float:
    """calculate hours in minutes"""
    return round(minutes / 60, 4)


def is_whole_div(a, b) -> bool:
    """verify that a is a multiple of b"""
    return a % b == 0


print(f"to_minutes(1.5) = {to_minutes(1.5)}")
print(f"to_hours(12) = {to_hours(12)}")
print(f"to_hours(5) = {to_hours(5)}")
print(f"is_whole_div(2, 3) = {is_whole_div(2, 3)}")
print(f"is_whole_div(12, 3) = {is_whole_div(12, 3)}")
