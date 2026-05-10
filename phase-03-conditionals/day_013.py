"""
Day 13 – Conditional Output (First Decision-Making)

1) Task:
Create a program that takes user input and produces different outputs depending on the value provided.

2) What I Learnt:
In this exercise, I reinforced my understanding of conditional statements by creating a program that checks if a user can vote based on their age. This demonstrated that different inputs lead to different outputs.

Although the syntax is simple, I noticed that conditional logic can easily lead to errors if attention is not paid to detail. For example, the minimum voting age is 18, so the condition must be written as age >= 18. It is intuitive to write age > 18, which would incorrectly exclude users who are exactly 18 years old, even though the program would still run.

This highlighted the importance of thinking carefully about logical conditions when writing decision-based code.

3) Key Concepts:
- Conditions
- If/else statements
- Logical thinking

4) Challenges:
Although not technically difficult, I spent some time deciding on a simple and realistic example that could clearly demonstrate conditional logic.

5) How I Overcame It:
I chose to use an age verification scenario, as it is commonly used in real-world applications and clearly illustrates conditional behaviour.

6) Mistakes:
No significant mistakes were made during this exercise.

7) Improvements:
The minimum age value could be stored in a variable, making it easier to adjust for different scenarios (e.g. applications with varying age requirements).
"""

print("""
Welcome to the vote age verification application.
We will start your age verification now.
""")

name = input("What's your name? ")
age = int(input(f"Hi, {name}. How old are you? "))

print()

if age >= 18: # Verifies if the user can vote (minimum age = 18).
    print(f"You can vote, {name}.")
else: # If user is younger than 18:
    print(f"You cannot vote yet, {name}.")