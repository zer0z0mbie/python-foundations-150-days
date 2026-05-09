"""
Day 18 – Categorising Values by Range

1) Task:
Create a program that takes a value and places it into a specific category based on its range.

2) What I Learnt:
I learnt that comparison operators can be used to categorise values into different ranges and generate different outputs accordingly.

This exercise also reinforced the importance of defining boundaries carefully. If ranges are not structured correctly, values may overlap or fall into the wrong category, leading to logical errors. For example, choosing between < and <= determines whether boundary values are included or excluded from a range.

3) Key Concepts:
- Comparison operators
- Range-based conditions
- Chained comparisons
- Boundary values

4) Challenges:
At first, I found it slightly difficult to phrase the outputs for the elif conditions clearly. For example, when testing the value 10, I realised that the wording could become ambiguous depending on whether the range was inclusive or exclusive.

5) How I Overcame It:
To make the output clearer, I explicitly added the word "inclusive" to indicate that the maximum value was part of the range.

6) Mistakes:
No mistakes were made during this exercise.

7) Improvements:
A possible improvement would be to store the range boundaries in variables, which would make the conditions easier to adjust and maintain.
"""

number = int(input("Type a number: "))

if number <= 0:
    print(f"{number} is less than or equal to 0")
elif 1 <= number <= 10:
    print(f"{number} is between 1 and 10 (inclusive)")
elif 11 <= number <= 100:
    print(f"{number} is between 11 and 100 (inclusive)")
else:
    print(f"{number} is greater than 100")