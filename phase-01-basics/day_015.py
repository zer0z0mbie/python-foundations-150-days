"""
Day 15 – Combining Conditions

1) Task:
Create a program that checks more than one condition at the same time before deciding the output.

2) What I Learnt:
I learnt that multiple conditions can be evaluated at the same time by combining logical operators in conditional statements. In this exercise, I created a short password validation program that checks whether a password meets the minimum requirements.

I also noticed that the same outcome can be achieved in different ways, such as using nested conditions or combining conditions with logical operators like "and" and "or" (which is the approach I used here).

This exercise reinforced the importance of logical accuracy, as the final output depends on all required conditions being evaluated correctly.

3) Key Concepts:
- Conditional statements
- Combining logical conditions
- Logical operators

4) Challenges:
No significant challenges were encountered during this exercise.

5) How I Overcame It:
No specific action was required, as no challenges were encountered.

6) Mistakes:
No mistakes were made during this exercise.

7) Improvements:
As this program simulates password validation, a possible improvement would be to strengthen the validation rules further (e.g. requiring numbers or uppercase letters) and to avoid displaying sensitive information directly.
"""

name = input("What's your name? ")

# Welcomes user
print(f"""
Welcome to the Password Validation app, {name}.
To comply with the minimum requirements, your password must contain at least 8 characters, including the '@' symbol.
""")

# Asks user to type his/her password
password = input("Please type your password for validation: ")

if len(password) >= 8 and "@" in password: # Checks if the password is compliant
    print("Your password complies with the minimum requirements.")
else: # If not compliant, informs the user it does not meet the requirements
    print("Your password does not comply with the minimum requirements.")