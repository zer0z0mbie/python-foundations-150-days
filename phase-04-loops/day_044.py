"""
Day 44 – Input Validation Loops

1. Task:
Create a program where:
- the user must enter valid input before continuing
- invalid input causes the program to ask again
- the loop continues until acceptable input is received

The goal is to make the program behave more like:
- a validation system
instead of:
- a trust-the-user system

2. What I Learnt:
While working on this exercise, I reinforced my understanding of input validation loops. This is a concept that I mentioned in many previous exercises because user input has been widely used throughout this challenge.

By working on this solution, I learnt that nested while loops can be used to validate both the data type and the range of a user's input. For example, the program can ensure that a number is entered instead of text and then verify that the number falls within an acceptable range.

This helps make the program more robust by ensuring that only valid input is accepted before execution continues.

This exercise also reinforced my understanding of exception handling and demonstrated how loops can be used to repeatedly request input until the user provides a valid response.

3. Key Concepts:
- input validation
- while loops
- exception handling
- nested loops
- data type validation
- range validation

4. Challenges:
No particular challenges were faced during this exercise.

5. How I Overcame It:
Not applicable.

6. Mistakes:
No mistakes were made during this exercise.

One potential mistake would be validating the data type but forgetting to validate the accepted range of values.

Another potential mistake would be placing the break statement incorrectly, causing the loop to terminate before valid input is received.

7. Improvements:
I would expand the program by allowing the user to repeatedly create characters rather than selecting only one class.

I could also validate character names and other attributes using the same input validation techniques.

Another improvement would be displaying the total number of invalid attempts before a valid option is selected.
"""

# Counter to compute the total of incorrect attempts.
wrong_option_count = 0

while True:
    while True:
        try:
            class_chosen = int(
                input(
                "Choose a class:\n"
                "(1) Warrior\n"
                "(2) Wizard\n"
                "(3) Archer\n"
                "Enter an option (1-3) > "
                )
            )

            break
        except ValueError:
            print("Must be a number.\n")
            wrong_option_count += 1

    if 1 <= class_chosen <= 3:
        print("You chose the", end=" ")
        if class_chosen == 1:
            print("Warrior", end=" ")
        elif class_chosen == 2:
            print("Wizard", end=" ")
        elif class_chosen == 3:
            print("Archer", end=" ")
        print("class.")

        break
    else:
        print("Invalid option. Choose from 1-3.\n")
        wrong_option_count += 1
