"""
Day 26 – Managing Multiple States Together

1) Task:
Create a program where:
- multiple states are tracked at the same time
- different state combinations produce different outcomes
- the program reacts differently depending on the overall system state

The goal is to make the program behave more like:
- a dynamic state system
instead of:
- isolated single-state checks

2) What I Learnt:
While working on this exercise, I learnt that multiple stages can be controlled using Boolean variables, which can lead to dynamic programs that execute different outcomes depending on pre-defined scenarios.

My three rubber ducks that I have on my desk helped me visualise this concept very well, as each of them has unique traits and colours (e.g., yellow, white, bearded, tattooed). As a result, different combinations of these traits return unique duckies.

Since two of the ducks share the same colour, deeper conditional checks are required to distinguish them, which makes the logic closer to real-world cases where multiple states may need to be combined together before reaching a final outcome.

I also noticed again how semantic errors can occur in this type of logic, so paying close attention to the conditional statements is crucial.

3) Key Concepts:
- conditionals
- multiple states
- input/output
- Boolean variables
- combined-state logic

4) Challenges:
No significant challenges were faced during this exercise.

5) How I Overcame It:
Not applicable.

6) Mistakes:
In the following condition:

if is_yellow and has_beard and is_irish:
    print("yellow, has a beard, and is Irish!")

I accidentally wrote "has tattoo" instead of "has a beard" in the output message, which caused an inconsistency between the condition being checked and the printed result.

7) Improvements:
I would improve the user input validation and expand the duck state system to support additional traits and combinations.
"""

# State variables
is_irish = False
is_dutch = False

is_white = False
is_yellow = False

has_tattoo = False
has_beard = False

print("\n🐤 🐤 🐤 Welcome to Ducky  🐤 🐤 🐤\n")

print(
    "What colour is your ducky?\n"
    "(1) White\n"
    "(2) Yellow"
)

ducky_colour = int(input("Choose an option: (1/2) "))
print()

if ducky_colour == 1:
    is_white = is_irish = True
elif ducky_colour == 2:
    print(
        "What's your ducky style?\n"
        "(1) Tattooed\n"
        "(2) Bearded"
    )

    ducky_style = int(input("Choose an option: (1/2) "))
    print()

    if ducky_style == 1:
        is_yellow = has_tattoo = is_dutch = True
    elif ducky_style == 2:
        is_yellow = has_beard = is_irish = True
    else:
        print("This ducky does not exist!!!")
else:
    print("This ducky does not exist!!!")

print("Your duck:", end=" ")

if is_white and is_irish:
    print("white and Irish!")

if is_yellow and has_tattoo and is_dutch:
    print("yellow, has tattoo, and is Dutch!")

if is_yellow and has_beard and is_irish:
    print("yellow, has a beard, and is Irish!")