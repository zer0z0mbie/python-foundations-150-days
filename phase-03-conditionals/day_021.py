"""
Day 21 – Combining Multiple Requirements

1) Task:
Create a program where:
- multiple conditions must be satisfied together
- different combinations produce different outcomes
- the logic simulates a small real-world requirement check

The goal is to make the program feel like a small rule-based system rather than a single isolated condition check.

2) What I Learnt:
I learnt that some requirements depend on others. For example, in this restaurant application, access to certain food and drink menus depends on conditions such as whether the user is 18 or older and what type of diet they follow. I also learnt how multiple conditions can work together to produce different outcomes.

3) Key Concepts:
- conditionals
- nested if statements
- Boolean variables
- logical validation
- combining multiple conditions

4) Challenges:
One challenge was organising the conditions correctly so the program displayed the correct menu combinations. It was also slightly confusing deciding when to use nested conditions instead of separate conditions.

5) How I Overcame It:
I overcame the challenge by breaking the logic into smaller steps:
- checking the user's age
- checking the user's diet
- combining both conditions to determine the correct menu output

6) Mistakes:
At the beginning, I made a mistake in the conditional logic and wrote =! instead of !=, which caused a logical error in the program.

7) Improvements:
- add user input validation
- handle invalid diet entries
"""

print("Welcome to the Restaurant App")

print()

is_vegetarian = False
is_carnivore = False
drinks_alcohol = False

age = int(input("How old are you? "))
diet = input("What's your diet? (Carnivore/Vegetarian) ").lower()

print()

if age >= 18:
    drinks_alcohol = True

if diet == "carnivore":
    is_carnivore = True
elif diet == "vegetarian":
    is_vegetarian = True

if not drinks_alcohol:
    print("Drinks Menu: Non-alcoholic")
    if is_carnivore:
        print("Food Menu: Grilled Meat")
    elif is_vegetarian:
        print("Food Menu: Vegetarian")
elif drinks_alcohol:
    print("Drinks Menu: Alcoholic & Non-alcoholic")
    if is_carnivore:
        print("Food Menu: Grilled Meat")
    elif is_vegetarian:
        print("Food Menu: Vegetarian")