"""
Day 30 – Persistent Progression Systems

1) Task:
Create a program where:
- progression through stages permanently affects later behaviour
- earlier choices continue influencing future outcomes
- the system remembers progression state across multiple decisions

The goal is to make the program behave more like:
- a persistent progression system
instead of:
- temporary isolated state changes

2) What I Learnt:
While working on this exercise, I learnt that with the implementation of conditional checks and Boolean variables, it is possible to track the state of the program in a way that later outcomes depend on previous inputs. The behaviour of the program depends on conditional checks to track the progression state.

In this example, the user is driving in their city and has the option to decide the direction (e.g., go straight, turn left, or turn right, depending on the route chosen). For each choice, the program records the state, which is represented by destinations (from destination_1 to destination_5), and at the end, the correct destination is displayed (e.g., "You arrived at destination X").

This exercise demonstrated how important progression systems are in applications and how important it is to record the stages correctly to ensure the proper outcome is produced.

3) Key Concepts:
- input/output
- conditional statements
- progression tracking
- Boolean variables
- persistent states

4) Challenges:
The main challenge was understanding how to ensure the program would close once an incorrect input was chosen, as loops are not being used at this stage of the challenge.

5) How I Overcame It:
To overcome this challenge, I imported the sys library and used the exit() function once an incorrect input was selected (e.g., choosing "a" while valid inputs are "s", "l", "r", or "p").

6) Mistakes:
No mistakes made.

7) Improvements:
I would add loops to repeatedly request valid input instead of terminating the program immediately after invalid entries.
"""

import sys

destination_1 = False
destination_2 = False
destination_3 = False
destination_4 = False
destination_5 = False

pull_over = False
out_of_gas = False

print("\nYou're driving in your city.\n")

print("Choose a direction:")

direction_1 = input("Straight, Right, or Pull Over? (S/R/P) ").lower()

if direction_1 == "s" or direction_1 == "r" or direction_1 == "p":
    if direction_1 == "r":
        destination_1 = True
    elif direction_1 == "s":
        print(
            "\nYou went straight.\n"
            "\nChoose a direction:"
        )

        direction_2 = input("Straight, Left, Right, or Pull Over? (S/L/R/P) ").lower()

        if direction_2 == "s" or direction_2 == "l" or direction_2 == "r" or direction_2 == "p":
            if direction_2 == "s":
                destination_2 = True
            elif direction_2 == "l":
                destination_3 = True
            elif direction_2 == "r":
                print(
                    "\nYou turned right.\n"
                    "\nChoose a direction:"
                )

                direction_3 = input("Straight, Left, Right, or Pull Over? (S/L/R/P) ").lower()

                if direction_3 == "s" or direction_3 == "l" or direction_3 == "r" or direction_3 == "p":
                    if direction_3 == "s":
                        out_of_gas = True
                    elif direction_3 == "l":
                        destination_4 = True
                    elif direction_3 == "r":
                        destination_5 = True
                    elif direction_3 == "p":
                        pull_over = True
                else:
                    print("\nDirection does not exist.")
                    sys.exit()
            elif direction_2 == "p":
                pull_over = True
        else:
            print("\nDirection does not exist.")
            sys.exit()
    elif direction_1 == "p":
        pull_over = True
else:
    print("\nDirection does not exist.")
    sys.exit()

if pull_over:
    print("\nYou've pulled over.")
elif out_of_gas:
    print("\nYou've run out of gas.")
else:
    print("\nYou've arrived at", end=" ")

    if destination_1:
        print("destination 1: City Centre.")

    if destination_2:
        print("destination 2: Venom Avenue.")

    if destination_3:
        print("destination 3: Peter Parking.")

    if destination_4:
        print("destination 4: Batman Road Upper.")

    if destination_5:
        print("destination 5: Dr. Octopus GP.")
