"""
Day 24 – Detecting Invalid Paths
1) Task:
Create a program where:
- some combinations of user choices are valid
- some combinations are impossible or invalid
- the program must detect and handle invalid paths correctly

The goal is to make the program behave more like:
- a controlled decision system
instead of:
- accepting every possible input combination

2) What I Learnt:
During this exercise, I learnt that if/else statements can be used to detect valid and invalid paths. I created a simple game that asks the player whether they can kill the dragon. I found it easier to filter out all the invalid paths using the else statement, as the if statement can focus on the valid path only.

During the development process, the concept of combining multiple paths from Day 23 was used. As a result, I was able to create different paths within the valid if condition, leading to deeper conditions.

3) Key Concepts:
- input/output
- valid/invalid paths
- conditions

4) Challenges:
No challenges were faced in this exercise, but I noticed that semantic errors can occur even when the correct usage of if/else statements is straightforward. Before implementing the logic correctly, it is important to verify whether the conditional flow itself makes sense.

5) How I Overcame It:
Not applicable.

6) Mistakes:
No potential mistakes were made at this stage.

7) Improvements:
Similarly to previous days, I believe an improvement would be adding input validation. I have deliberately not added it at this stage because the challenge difficulty increases gradually, and input validation will be covered in later days.
"""

print(" * * * Welcome to Medieval Tales * * *")
print()

name = input("What's your name, warrior? ")
print()

print(
    "The Red Dragon is destroying the village, {}.\n"
    "Can you kill it? Try your luck!".format(name)
)
print()

warrior_has_weapon = input("Do you have a weapon? (Y/N) ").lower()

if warrior_has_weapon == "y":
    warrior_has_armour = input("Do you have armour? (Y/N) ").lower()
    if warrior_has_armour == "y":
        print("You have a sword and armour, so you can kill the dragon!")
    else:
        print("You have a sword but don't have armour, so you may be able to kill the dragon!")
else:
    print("You don't have a weapon, so you can't kill the dragon!")