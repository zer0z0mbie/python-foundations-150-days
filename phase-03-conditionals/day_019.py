"""
Day 19 – Nested Conditions

1) Task:
Create a program where one condition is checked inside another condition to produce more specific outcomes.

2) What I Learnt:
While completing this exercise, I learnt that nested conditionals can be used to generate more specific outcomes by performing additional checks only after an initial condition is satisfied.

I found this concept important because real-world systems often require layered validation and decision-making. For example, a video game subscription service may first verify if the user has a paid account and then check the account tier before determining which free games are available to the player.

3) Key Concepts:
- Nested conditionals
- Boolean variables
- Conditional logic

4) Challenges:
The main challenge was managing the logical flow of the conditions and ensuring the correct variables were being checked during validation.

5) How I Overcame It:
To overcome this challenge, I used Python Tutor to visualise how the variables changed throughout the execution of the program. This helped me identify incorrect logical checks and fix the conditional flow.

6) Mistakes:
At first, I made a few logical mistakes. I did not validate whether the user inputs were limited to "yes" or "no". In addition, instead of checking the Boolean variables gothic_lover and masochist, I mistakenly checked like_gothic and masochist directly in some conditions. This caused incorrect behaviour, but I identified and fixed the issue using Python Tutor.

7) Improvements:
A possible improvement would be to keep the program running until valid answers are provided, instead of terminating after invalid input.
"""

gothic_lover = False
masochist = False
valid_answers = ["yes", "no"]

print("Welcome to Bloodborne gameplay validation.")

like_gothic = input("Do you like gothic stuff? (Yes/No) ").lower()
like_to_suffer = input("Do you like to suffer? (Yes/No) ").lower()

if like_gothic == "yes":
    gothic_lover = True
if like_to_suffer == "yes":
    masochist = True

if like_gothic not in valid_answers or like_to_suffer not in valid_answers:
    print("Invalid answer. Yes or no only.")
else:
    if gothic_lover:
        if masochist:
            print("You like gothic stuff and like to suffer. You can play Bloodborne.")
        else:
            print("You like gothic stuff but don't like to suffer. You can't play Bloodborne.")
    elif masochist:
        print("You like to suffer but don't like gothic stuff. You can't play Bloodborne.")
    else:
         print("You don't like gothic stuff and don't like to suffer. You can't play Bloodborne.")