"""
Day 41 – Loop-Controlled Menus

1. Task:
Create a program where:
- a menu is displayed repeatedly
- the user can choose different actions multiple times
- the program continues running until the user selects an exit option

The goal is to make the program behave more like:
- a menu-driven system
instead of:
- a single-action program

2. What I Learnt:
While working on this exercise, I reinforced my understanding of while loops and how they can be used to create menu-driven programs. Since it is unclear how many times a user may select certain options, loops allow the program to continue running until a specific exit condition is met.

I also learnt how a break statement can be used to control the flow of the program and terminate the loop when the user chooses to exit.

In addition, I applied exception handling because users may enter invalid data. This demonstrated how loops and exception handling often work together in interactive programs.

3. Key Concepts:
- while loops
- exception handling
- menu-driven systems
- exit conditions
- break statements

4. Challenges:
One challenge was deciding where to place the try/except block. Although I already have some experience with exception handling, I sometimes find it difficult to determine the best location for it, especially when multiple while loops are involved.

5. How I Overcame It:
To overcome this challenge, I used Python Tutor, reviewed previous exercises, and researched examples online.

6. Mistakes:
A minor issue involved the spacing of the printed output, as the text was initially displayed without enough separation between messages.

To improve readability, I added newline characters (\n) to create clearer spacing between outputs.

7. Improvements:
I would add a potion counter and only allow the player to use a potion if one is available in the inventory.
"""

while True:
    while True:
        print(
            "Battle Menu:\n"
            "(1) Attack\n"
            "(2) Use Potion\n"
            "(3) Flee"
        )
        option_chosen = input("Choose an option (1-3) ")

        try:
            option_chosen = int(option_chosen)
            break
        except ValueError:
            print("\nNumbers only.\n")

    if option_chosen == 1:
        print("\nYou attacked.\n")
    elif option_chosen == 2:
        print("\nYou used a potion.\n")
    elif option_chosen == 3:
        print("\nYou fled.\n")
        break
    else:
        print("\nInvalid option! Choose 1-3.\n")
        