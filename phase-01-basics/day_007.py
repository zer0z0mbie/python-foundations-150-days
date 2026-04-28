"""
Day 7 – Changing Variable Values

1) Task:
Create a variable, then change its value, and output both the original and updated values.

2) What I Learnt:
In this exercise, I reinforced my knowledge of variables and how their values can be updated as a program executes. To solve the task, I revisited important concepts such as order of execution (Python code is read from top to bottom). This is particularly relevant here, as the original and updated values must be printed in the correct order.

3) Key Concepts:
- Variable assignment and reassignment
- Order of execution
- Logical flow

4) Challenges:
This was a straightforward exercise, so no challenges were encountered.

5) How I Overcame It:
No specific action was required, as no challenges were encountered.

6) Mistakes:
Although no mistakes were made during this task, a potential issue could occur if both print statements are placed after the value is updated. In that case, only the updated value would be displayed, which would result in a logical error.

7) Improvements:
For this exercise, I created an armour_set variable representing a video game item. A possible improvement would be to allow the user to update the armour_set using input, making the program more dynamic.
"""

armour_set = "Fire Breath of the Dragon Lord Set"

print(f"Original value - Armour set: {armour_set}")

armour_set = "Iced Tears of the Fallen Dragon Set"

print(f"Updated value - Armour set: {armour_set}")