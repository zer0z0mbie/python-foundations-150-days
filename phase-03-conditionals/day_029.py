"""
Day 29 – Sequential State Progression

1) Task:
Create a program where:
- states must be activated in a specific order
- some actions should only become available after previous stages are completed
- the program tracks progression through a sequence of dependent states

The goal is to make the program behave more like:
- a progression-based system
instead of:
- independent state activation

2) What I Learnt:
While working on this exercise, I learnt that some program states should only become active after previous states have been completed correctly. In this program, the Ducky must be assembled in a strict sequence: head, body, tail, and finally feet.

Each stage depends on the successful completion of the previous one, which creates a progression-based system rather than independent actions. I learnt that Boolean variables can be used to track progression through multiple stages and verify whether the correct sequence has been followed.

I also noticed how sequential progression systems are common in real-world applications such as games, manufacturing systems, tutorials, and workflow processes where certain actions only unlock after earlier steps are completed.

3) Key Concepts:
- conditionals
- sequential state progression
- dependent states
- Boolean state tracking
- procedural progression
- input/output

4) Challenges:
One challenge was managing the nested conditional statements while ensuring the assembly stages were checked in the correct order. It was also important to validate the user input at every stage to avoid invalid part selections.

5) How I Overcame It:
I overcame these challenges by breaking the progression into smaller stages and using Boolean variables to track whether each assembly part had been completed. Input validation checks were also added before moving to the next stage.

6) Mistakes:
One potential issue in the program is that the user can still continue through later stages even if an earlier stage was incorrect. The final validation only checks the sequence at the end rather than preventing incorrect progression immediately.

7) Improvements:
I would improve the program by stopping progression immediately if the wrong part is selected. I would also reduce repetition by using loops or lists instead of deeply nested conditionals.

Additionally, I could expand the system by adding more assembly stages and additional progression requirements.
"""

# State variables
head_assembled = False
body_assembled = False
tail_assembled = False
feet_assembled = False

print("\nWelcome to Ducky Assembly Line\n")

print(
    "Please assemble the Ducky in the following order:\n"
    "(1) Head\n"
    "(2) Body\n"
    "(3) Tail\n"
    "(4) Feet"
)

assembled_part_1 = int(input("Choose the first part to assemble: (1/2/3/4) "))

if 0 < assembled_part_1 < 5:
    if assembled_part_1 == 1:
        head_assembled = True

    assembled_part_2 = int(input("Choose the second part to assemble: (1/2/3/4) "))

    if 0 < assembled_part_2 < 5:
        if assembled_part_2 == 2:
            body_assembled = True

        assembled_part_3 = int(input("Choose the third part to assemble: (1/2/3/4) "))

        if 0 < assembled_part_3 < 5:
            if assembled_part_3 == 3:
                tail_assembled = True

            assembled_part_4 = int(input("Choose the fourth part to assemble: (1/2/3/4) "))

            if 0 < assembled_part_4 < 5:
                if assembled_part_4 == 4:
                    feet_assembled = True

                if head_assembled and body_assembled and tail_assembled and feet_assembled:
                    print(
                        "\nDucky assembled in the right order.\n"
                        "Duck gives you a rubber hug!"
                    )
                else:
                    print(
                        "\nDucky not assembled in the right order.\n"
                        "Ducky explodes!"
                    )
            else:
                print("\nDucky part does not exist.")
        else:
            print("\nDucky part does not exist.")
    else:
        print("\nDucky part does not exist.")
else:
    print("\nDucky part does not exist.")