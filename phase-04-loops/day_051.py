"""
Day 51 – Updating Records in Collections

1. Task:
Create a program where:
- multiple records are stored in a collection
- the user selects an existing record
- the selected record is updated with new information

The goal is to make the program behave more like:
- an update system
instead of:
- a read-only collection

2. What I Learnt:
While working on this exercise, I learnt how existing records in a collection can be updated rather than only added, removed, or displayed. In this example, the player selects an item from their inventory and replaces it with a new one. I also reinforced my understanding of input validation by ensuring that only items already present in the inventory could be replaced. This exercise helped me understand that updating existing data is another common operation performed on collections in real-world applications.

3. Key Concepts:
- lists
- updating collections
- input validation
- while loops
- list indexing
- .index() method

4. Challenges:
No particular challenges were faced during this exercise.

5. How I Overcame It:
Not applicable.

6. Mistakes:
No mistakes were made during this exercise. One potential mistake would be attempting to replace an item without first checking whether it exists in the collection, which could cause an error when using the .index() method.

7. Improvements:
I would allow the user to update multiple inventory items before exiting the program. I could also prevent duplicate items from being added to the inventory and display a confirmation message after each successful update.
"""

current_inventory = ["Iron Sword", "Wooden Shield", "Health Potion"]

# Displays the inventory
print("Inventory:")

for item in current_inventory:
    print(f"- {item}")

print()

# Prompts player to enter an item to replace
item_to_replace = input("Which item do you want to replace? ")

# Validates the input
while item_to_replace not in current_inventory:
    print(f"{item_to_replace} not in the inventory.")

    item_to_replace = input("Which item do you want to replace? ")

# Prompts player to enter a new item
new_item = input("New item: ")

# Gets the item to replace index and replace the items
item_to_replace_index = current_inventory.index(item_to_replace)
current_inventory[item_to_replace_index] = new_item

# Confirm replacement
print(f"\n'{item_to_replace}' was replaced with '{new_item}'.")

# Displays the updated inventory
print("\nUpdated Inventory:")

for item in current_inventory:
    print(f"- {item}")
