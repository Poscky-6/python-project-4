from dataclasses import dataclass


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


if __name__ == "__main__":
    data = {"name": "laptop", "unit_price": 100.50, "quantity_on_hand": 30}

    validated_data = InventoryItem(**data)
    breakpoint()