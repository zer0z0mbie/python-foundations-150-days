"""
Day 31 – Conditional State Memory

1) Task:
Create a program where:
- previous states continue affecting future decisions
- certain choices permanently change available options
- the program remembers important past events during execution

The goal is to make the program behave more like:
- a memory-driven system
instead of:
- isolated temporary decisions

2) What I Learnt:
While working on this exercise, I learnt that Boolean variables and conditional statements can be used to remember previous choices and affect future outcomes later in the program.

In this example, the user’s earlier decisions, such as taking a coat or checking their pockets, directly affect what happens later when it starts raining and when they need their mobile phone.

This exercise demonstrated how programs can remember important states instead of treating every decision separately.

3) Key Concepts:
- input/output
- conditional statements
- Boolean variables
- state tracking
- persistent states

4) Challenges:
The main challenges were organising the program and understanding how earlier choices could continue affecting events later in the program.

5) How I Overcame It:
To overcome these challenges, I broke down the program into smaller steps and used Boolean variables to store important decisions. Later, those states were checked using conditional statements.

6) Mistakes:
No mistakes made.

7) Improvements:
I would add loops to validate user input and add more choices to create additional outcomes.
"""

# State variables
coat_taken = False
pockets_checked = False

print("\nYou're about to leave home on a sunny Sunday.\n")

take_coat = input("Do you take your coat with you? (Y/N) ").lower()

if take_coat == "y":
    coat_taken = True
    print("You take your coat.\n")
else:
    print("You decide not to take your coat.\n")

check_pockets = input("Do you check your pockets? (Y/N) ").lower()

if check_pockets == "y":
    pockets_checked = True
    print(
        "You check your pockets and realise you forgot your mobile phone.\n"
        "You grab your mobile before leaving home."
    )
else:
    print("You decide not to check your pockets.")

print("\nYou leave home.")

print("\nA few hours later, it starts to rain.\n")

if coat_taken:
    print("You wear your coat and don't get wet.")
else:
    print("You get soaked!")

print("You reach your pockets to get your mobile and call a friend to give you a lift home.")

if pockets_checked:
    print(
        "You call a friend, who picks you up.\n"
        "You arrive home safe and sound."
    )
else:
    print(
        "You don't have your mobile with you, so you need to walk for almost an hour in the rain.\n"
        "You get a strong cold and spend the next week home."
    )
