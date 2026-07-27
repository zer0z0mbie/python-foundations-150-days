"""
Day 52 – Summarising Collections

1. Task:
Create a program where:
- multiple records are stored in a collection
- the program processes every record
- summary information is calculated and displayed

The goal is to make the program behave more like:
- a reporting system
instead of:
- a record management system

2. What I Learnt:
While working on this exercise, I learnt how collections can be processed to produce summary information. In this example, I looped through an inventory and counted how many times each unique item appeared. I also used a second list to keep track of which items had already been counted, preventing duplicate results from being displayed. This exercise reinforced my understanding of loops, collections, and counting data to generate a simple report.

3. Key Concepts:
- lists
- for loops
- collection traversal
- data summarisation
- .count() method

4. Challenges:
No particular challenges were faced during this exercise.

5. How I Overcame It:
Not applicable.

6. Mistakes:
No mistakes were made during this exercise. One potential mistake would be counting every item without checking whether it had already been processed, causing duplicate results to be displayed.

7. Improvements:
I would display the total number of inventory items alongside the summary. I could also sort the summary alphabetically or by quantity before displaying the results.
"""

inventory = [
    "Gold Coin",
    "Health Potion",
    "Gold Coin",
    "Mana Potion",
    "Gold Coin",
    "Sword"
]

items_counted = []

for item in inventory:
    if item not in items_counted:
        print(f"{item}: {inventory.count(item)}")

        items_counted.append(item)
