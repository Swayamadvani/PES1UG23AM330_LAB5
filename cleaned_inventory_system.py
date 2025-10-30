"""
Inventory Management System
----------------------------
A simple inventory tracker with add, remove, save, load,
and reporting functionalities.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def add_item(stock_data, item, quantity, logs):
    """
    Add an item to the inventory with quantity.
    """
    if not isinstance(item, str) or not isinstance(quantity, int):
        logger.warning(
            "Invalid types for item or quantity: %s, %s",
            type(item), type(quantity)
        )
        return

    stock_data[item] = stock_data.get(item, 0) + quantity
    logs.append(f"{datetime.now()}: Added {quantity} of {item}")
    logger.info("Added %d units of %s", quantity, item)


def remove_item(stock_data, item, quantity):
    """
    Remove quantity of an item from inventory.
    """
    if not isinstance(item, str) or not isinstance(quantity, int):
        logger.warning(
            "Invalid types for item or quantity: %s, %s",
            type(item), type(quantity)
        )
        return

    try:
        if item not in stock_data:
            logger.warning("Attempted to remove missing item: %s", item)
            return

        stock_data[item] -= quantity
        if stock_data[item] <= 0:
            del stock_data[item]
            logger.info("Removed %s completely", item)
        else:
            logger.info("Removed %d units of %s", quantity, item)

    except KeyError as error:
        logger.error("Error removing item: %s", error)


def get_quantity(stock_data, item):
    """
    Get the quantity of a given item.
    """
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """
    Load inventory data from JSON file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file_obj:
            data = json.load(file_obj)
            logger.info("Loaded data from %s", file_path)
            return data
    except FileNotFoundError:
        logger.warning("File not found: %s", file_path)
        return {}
    except json.JSONDecodeError as error:
        logger.error("Error decoding JSON: %s", error)
        return {}


def save_data(stock_data, file_path="inventory.json"):
    """
    Save inventory data to JSON file.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file_obj:
            json.dump(stock_data, file_obj, indent=4)
            logger.info("Saved data to %s", file_path)
    except OSError as error:
        logger.error("Error saving data: %s", error)


def print_data(stock_data):
    """
    Print the current inventory data.
    """
    logger.info("Printing inventory report")
    print("\n------ Inventory Report ------")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("------------------------------")


def check_low_items(stock_data, threshold=5):
    """
    Identify items with low stock below threshold.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """
    Demonstrate basic usage of inventory system.
    """
    logs = []
    stock_data = {}

    add_item(stock_data, "apple", 10, logs)
    add_item(stock_data, "banana", 5, logs)
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)
    print(f"Apple stock: {get_quantity(stock_data, 'apple')}")
    print(f"Low items: {check_low_items(stock_data)}")
    save_data(stock_data)
    loaded_data = load_data()
    print_data(loaded_data)


if __name__ == "__main__":
    main()
