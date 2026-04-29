"""
Day 8 – Multiple Calculations

1) Task:
Create variables and perform more than one calculation, then output the results.

2) What I Learnt:
While completing this exercise, I created multiple variables and used them together to perform different calculations, which reinforced my understanding of how variables interact. Although this is still an early stage of the project, one key takeaway is the importance of meaningful variable naming. This became more relevant as the number of variables increased.

3) Key Concepts:
- Working with multiple variables
- Basic arithmetic operations in Python
- Python operators
- Integers
- Floats
- f-strings

4) Challenges:
No significant challenges were encountered during this exercise.

5) How I Overcame It:
No specific action was required, as no challenges were encountered.

6) Mistakes:
Although no mistakes were made during this exercise, I recognised that using the division operator may result in a different data type (e.g. float instead of integer), depending on the context.

7) Improvements:
I noticed that the result of the division is a float due to the use of the true division operator ("/"). If the intention is to return an integer, the floor division operator ("//") could be used instead.
"""

# Number variables
number_1 = 100
number_2 = 25

# Calculation variables
addition = number_1 + number_2
subtraction = number_1 - number_2
multiplication = number_1 * number_2
division = number_1 / number_2

# Result outputs
print("Basic Calculations:")
print(f"Addition: {number_1} + {number_2} = {addition}")
print(f"Subtraction: {number_1} - {number_2} = {subtraction}")
print(f"Multiplication: {number_1} * {number_2} = {multiplication}")
print(f"Division: {number_1} / {number_2} = {division}")