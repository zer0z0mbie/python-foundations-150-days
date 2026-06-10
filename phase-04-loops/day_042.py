"""
Day 42 – Sentinel-Controlled Loops

1) Task:
Create a program where:
- the loop continues until a special value is entered
- the user controls when the loop ends
- the program repeatedly processes input until the sentinel value is detected

The goal is to make the program behave more like:
- a sentinel-controlled system
instead of:
- a fixed repetition system

2) What I Learnt:
While working on this exercise, I learnt about sentinel values and how they can be used to control when a loop ends.

At first, I was unfamiliar with the term "sentinel" and thought it referred to something from a science-fiction setting rather than a programming concept. After researching the concept, I learnt that a sentinel value is a special input used to signal that a loop should end.

I then understood that sentinel values are particularly useful in situations where it is impossible to know in advance how many inputs a user will provide. For example, in a to-do list application, the user may continue adding items until they decide they are finished.

This exercise helped me understand how sentinel values can be used to give users control over when a loop stops running.

3) Key Concepts:
- while loops
- conditions
- sentinel values
- loop termination
- user-controlled input

4) Challenges:
No major challenges were faced during this exercise.

5) How I Overcame It:
Not applicable.

6) Mistakes:
One mistake I made was forgetting to place the following line inside the loop:

item_to_add = capwords(input("Add an item: "))

This caused the loop condition to never change, resulting in an infinite loop.

7) Improvements:
I would add a counter to track how many items were added and display the total once the loop ends.
"""

from string import capwords

sentinel = "Quit"

item_to_add = capwords(input("Add an item: "))

while item_to_add != sentinel:
    print(f"{item_to_add} added to the list.")
    item_to_add = capwords(input("Add an item: "))

print("All items added.")
