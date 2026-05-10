"""
Day 10 – Working with Input and Numbers

1) Task:
Ask the user for input, convert it into a number, perform a calculation, and display the result.

2) What I Learnt:
I learnt that if we want to obtain an integer or float from user input, the value must be converted, as input() returns a string by default.

While completing this exercise, I noticed a few important behaviours:
- My intention was to create a short program that doubles the value. However, if the input is not converted to an integer, it is treated as a string and repeated (e.g. if the user enters 25, the result becomes 2525 instead of 50). This is a logical error that can occur if attention to data types is not applied.
- Using the input value directly in most arithmetic operations (except multiplication) results in a TypeError.

3) Key Concepts:
- Input and output
- Type conversion
- Basic arithmetic operations

4) Challenges:
No significant challenges were encountered during this exercise.

5) How I Overcame It:
No specific action was required, as no challenges were encountered.

6) Mistakes:
No mistakes were made during this exercise.

7) Improvements:
Although I wrote this program using multiple steps to clearly separate input, conversion, and calculation, it could be simplified by combining these steps into fewer lines (e.g. converting the input directly).
"""

favourite_number = input("What's your favourite number? ") # input
favourite_number_int = int(favourite_number) # conversion
favourite_number_doubled = favourite_number_int * 2 # calculation

print(f"Your favourite number doubled is {favourite_number_doubled}") # output