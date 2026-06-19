"""
Day 47 – Loop-Based Data Collection Systems

1. Task:
Create a program where:
- information is collected across multiple loop iterations
- the user can enter multiple records or entries
- the program stores the collected data and displays a summary at the end

The goal is to make the program behave more like:
- a data collection system
instead of:
- a single-record system

2. What I Learnt:
While working on this exercise, I learnt that loops can be used alongside other tools such as lists and counters to collect data. To demonstrate this concept, I created a simple looting system that allows the player to loot three items from a Goblin. The selected items are stored in a list, and a summary of the collected data is displayed at the end of the program.

This exercise helped me understand how loops can repeatedly collect information while lists can be used to store that information for later use. It also reinforced my understanding of input validation and counters, as both concepts were required to manage the looting process correctly.

3. Key Concepts:
- while loops
- for loops
- lists
- data collection
- input validation
- counters
- data summaries

4. Challenges:
A challenge I faced was implementing the input validation because I wanted to ensure that the item selected by the player existed in the list of dropped items.

5. How I Overcame It:
To overcome this challenge, I added a while True loop. If the item selected by the player was not present in the list of dropped items, the program requested the input again.

Once the player entered a valid item, the loop reached the break statement and the program continued normally.

6. Mistakes:
One mistake I made was when displaying the number of items available to loot. Initially, the program always displayed the word “items” in the plural form, which resulted in a grammatical error when only one item remained. For example: 1 items.

To solve this issue, I added an if/else statement that displayed either “item” or “items” depending on the number of items remaining.

7. Improvements:
I would add a random monster generator so that different enemies can drop different loot tables. I could also allow the player to loot varying numbers of items depending on the enemy defeated.

Another improvement would be displaying the remaining dropped items after each successful loot.
"""

from string import capwords

# Lists of dropped and looted items
items_dropped = [
    "Shield",
    "Sword",
    "Golden Coins",
    "Health Potion",
    "Mana Potion",
    "Treasure Map"
]

items_looted = []

# Initialises counters
items_looted_counter = 0
items_to_loot_counter = 3
incorrect_attempts_counter = 0

print("You defeated a Goblin.\n")

while items_looted_counter < 3: # Maximum amount of lootable items: 3
    if items_to_loot_counter > 1:
        print(f"You can loot {items_to_loot_counter} items.") # Plural (2-3 items)
        print("Items available:")
    else:
        print(f"You can loot {items_to_loot_counter} item.") # Singular (1 item)
        print("Item available:")

    for item in items_dropped:
        print(f"* {item}")

    # Prompts player to choose an item
    item_looted = capwords(input("Choose an item > "))

    # Validates item
    while True:
        print()

        if item_looted not in items_dropped:
            # Updates incorrect attempts counter
            incorrect_attempts_counter += 1

            if item_looted in items_looted:
                print(f"{item_looted} already looted.")
            else:
                print(f"{item_looted} not dropped.")

            print("Please choose one of these items:")

            for item in items_dropped:
                print(f"* {item}")

            item_looted = capwords(input("Choose an item > "))

        else:
            break

    print(f"{item_looted} looted\n")

    # Updates counters
    items_looted_counter += 1
    items_to_loot_counter -= 1

    # Updates lists
    items_dropped.remove(item_looted)
    items_looted.append(item_looted)

# Prints game summary
print(
    "Game Summary:\n"
    f"Incorrect attempts: {incorrect_attempts_counter}\n"
    "Items looted:"
)

for item in items_looted:
    print(f"* {item}")
