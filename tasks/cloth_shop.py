from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class AvailabilityByColor:
    color: str
    size: str
    quantity: int


@dataclass_json
@dataclass
class ClothShop:
    id: int
    name: str
    type: str
    price: int
    availability: list[AvailabilityByColor]
