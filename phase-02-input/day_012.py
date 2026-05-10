"""
Day 12 – Formatted Output (Multi-line & Readability)

1) Task:
Create a program that takes user input and displays the result in a well-structured, multi-line format.

2) What I Learnt:
While completing this exercise, I learnt that output can be structured in different ways. The method I found most direct was using a multi-line string, which is created with triple quotation marks. This allows a single print statement to display multiple lines, improving readability and reducing the need for multiple print statements (which can make the code easier to maintain if the text needs to be edited).

3) Key Concepts:
- Input and output
- Multi-line formatting
- Output readability

4) Challenges:
No significant challenges were encountered during this exercise.

5) How I Overcame It:
No specific action was required, as no challenges were encountered.

6) Mistakes:
No mistakes were made during this exercise.

7) Improvements:
A possible improvement would be to convert the input values to integers immediately when collecting them, which would avoid repeating the conversion during the calculation.
"""

name = input("What's your name? ")
current_age = input("How old are you? ")
retirement_age = input("When are you retiring? ")
retirement_countdown = int(retirement_age) - int(current_age)

print(f"""Welcome to the Retirement Countdown App, {name}.

You're {current_age} and you're retiring when you're {retirement_age}.
Countdown: {retirement_countdown} years to retire...""")