"""
Day 38 – Conditional State Combinations

1. Task:
Create a program where:
- multiple states combine to produce different outcomes
- the same state may lead to different results depending on other active states
- outcomes depend on combinations of conditions rather than individual conditions alone

The goal is to make the program behave more like:
- a conditional state combination system
instead of:
- independent state checks

2. What I Learnt:
I learnt how outcomes can depend on combinations of states rather than individual conditions.

In this example, having fuel and checking the GPS create different results depending on which states are active. Only when both states are active does the player successfully reach the destination.

The same state can also lead to different outcomes depending on the other active state. For example, having fuel leads to reaching the destination when GPS is available, but leads to getting lost when GPS is unavailable.

This exercise helped me understand how multiple conditions can interact together to determine an outcome rather than relying on a single state alone.

3. Key Concepts:
- input/output
- conditional statements
- Boolean variables
- state tracking
- logical operators
- conditional state combinations

4. Challenges:
No particular challenges were faced.

5. How I Overcame It:
Not applicable.

6. Mistakes:
A potential mistake would be checking states individually instead of evaluating their combinations, which would defeat the purpose of the exercise.

7. Improvements:
I would add input validation and introduce additional states such as weather or vehicle condition to create more possible outcomes.
"""

fuel = False
gps = False

print("You're preparing for a road trip.")

refill_tank = input("Do you refill the tank? (Y/N) ").lower()

if refill_tank == "y":
    fuel = True

print("You're on the road...")

check_gps = input("Do you check the GPS? (Y/N) ").lower()

if check_gps == "y":
    gps = True

if fuel and gps:
    print("You reach your destination.")

if fuel and not gps:
    print("You get lost.")

if not fuel and gps:
    print("You're stranded.")

if not fuel and not gps:
    print("You are lost, stranded, and in serious trouble.")
    