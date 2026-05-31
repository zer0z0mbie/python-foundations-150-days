"""
Day 36 – State Recovery Systems

1. Task:
Create a program where:
- negative states can be reversed
- recovery actions can remove or reduce problems
- the final outcome depends on both setbacks and recovery attempts

The goal is to make the program behave more like:
- a state recovery system
instead of:
- a one-way state progression system

2. What I Learnt:
While working on this exercise, I learnt that it is possible to create conditions that improve and recover negative states.

In this example, being bitten by a zombie causes the player to become infected. However, unlike previous exercises where negative states often led directly to a bad outcome, the player has an opportunity to recover by searching for medicine.

This exercise demonstrated how a program can reverse a negative state and change the final outcome based on recovery actions rather than only on the initial problem.

3. Key Concepts:

- input/output
- conditional statements
- Boolean variables
- state tracking
- recovery systems
- state reversal

4. Challenges:
No particular challenges were faced during this exercise.

5. How I Overcame It:
Not applicable.

6. Mistakes:
During the review process, I noticed a logical issue where the player could escape the zombie but the program would continue executing and eventually report death by infection. I corrected this by using sys.exit() to terminate the program immediately when the player successfully escaped.

7. Improvements:
I would add input validation to ensure that only valid options can be entered.

I could also expand the recovery system by introducing multiple medicines, failed recovery attempts, or partial recovery states instead of having only a fully cured or dead outcome.
"""

import sys

bitten = False
infected = False
medicine_found = False
infection_cured = False
died_by_infection = False

print("A zombie approaches you.")

action = input("Do you push the zombie? (Y/N) ").lower()

if action == "y":
    print("You push the zombie and escape.")
    sys.exit()
else:
    print("You're bitten.")
    bitten = True

if bitten:
    print("You get infected.")
    infected = True

if infected:
    search_for_medicine = input("Search for medicine? (Y/N) ").lower()

    if search_for_medicine == "y":
        print("You've found the medicine.")
        medicine_found = True

if medicine_found:
    infection_cured = True
else:
    died_by_infection = True

if infection_cured:
    print("You cured the infection.")

if died_by_infection:
    print("You died by infection.")
