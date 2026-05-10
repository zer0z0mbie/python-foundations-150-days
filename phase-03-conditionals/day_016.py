"""
Day 16 – Negating Conditions

1) Task:
Create a program where the output depends on a condition not being true.

2) What I Learnt:
This exercise helped me better understand the "not" operator. By completing it, I observed that the operator inverts the Boolean value of a variable.

In this program, the user can only join the Toastie Club if they love avocados. If they do not meet this condition, the negated condition is triggered instead.

This reinforced the idea that negation is useful when a decision depends on something not being true.

3) Key Concepts:
- not operator
- Boolean values
- Conditional logic

4) Challenges:
I found it challenging to understand how the "not" operator works and how it changes the evaluation of a condition.

5) How I Overcame It:
To overcome this challenge, I used the website Python Tutor to visualise how the program executed step by step with different inputs.

6) Mistakes:
No mistakes were made during this exercise.

7) Improvements:
I would improve the input validation to ensure that only "like" or "love" are accepted, as currently any word other than "love" leads to the same outcome.
"""

print("Welcome to the Toastie Club")

avocado_lover = False # Initialises as False as we can't assume one loves avocados (although this is crazy)
like_avocado = input("Do you like or do you love avocados? Like/Love ").lower()

if like_avocado == "love": # Moment of truth: finds out if user likes avocado (we hope so)
    avocado_lover = True

# Output (join the club or not)
if not avocado_lover:
    print("You must love avocados to join the Toastie Club!")
else:
    print("Welcome to the club, avocado lover!!!")