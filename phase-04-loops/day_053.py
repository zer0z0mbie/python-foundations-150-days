"""
Day 53 – Removing Records from Collections

1. Task:
Create a program where:
- multiple records are stored in a collection
- the user selects an existing record to remove
- the selected record is deleted from the collection
- the updated collection is displayed

The goal is to make the program behave more like:
- a record removal system
instead of:
- an update system

2. What I Learnt:
While working on this exercise, I learnt how records can be removed from a collection.
In this example, the player selects an item to discard from their inventory. Before removing the item, the program validates that it exists in the inventory, preventing invalid operations. This exercise reinforced my understanding of list manipulation and demonstrated that collections can be modified not only by adding or updating records, but also by removing them.

3. Key Concepts:
- lists
- removing records
- .remove() method
- input validation
- collection manipulation

4. Challenges:
No particular challenges were faced during this exercise.

5. How I Overcame It:
Not applicable.

6. Mistakes:
No mistakes were made during this exercise. One potential mistake would be attempting to remove an item that does not exist in the collection without validating the input first, which would cause an error when using the .remove() method.

7. Improvements:
I would allow the user to remove multiple items before exiting the program. I could also display the total number of remaining items after each successful removal.
"""

from string import capwords

inventory = [
    "Iron Sword",
    "Wooden Shield",
    "Gold Coin",
    "Health Potion",
    "Mana Potion"
]

# Displays the current inventory
print("Current Inventory:")

for item in inventory:
    print(f"- {item}")

# Prompts player to input an item to be discarded
discarded_item = capwords(input("\nWhich item do you want to discard? "))

if discarded_item not in inventory:
    print(f"'{discarded_item}' not in the inventory.")
else:
    inventory.remove(discarded_item)

    print(f"'{discarded_item}' removed.")

    # Updated inventory
    print("\nUpdated Inventory:")

    for item in inventory:
        print(f"- {item}")