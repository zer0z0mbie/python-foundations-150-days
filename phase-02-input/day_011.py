"""
Day 11 – Multiple User Inputs

1) Task:
Ask the user for more than one value, use those values together, and display a result.

2) What I Learnt:
I learnt that it is possible to handle multiple user inputs to perform operations in Python, as the values provided by the user are stored in variables that can be used throughout the program.

By default, input() returns a string, but it is possible to convert it to other data types, such as integers, when required.

The appropriate data type depends on the program requirements, and there are different ways to perform the conversion (e.g. converting the input directly or storing it first and converting it later if the original string is still needed).

3) Key Concepts:
- Input and output
- Type conversion
- Handling multiple user inputs

4) Challenges:
No significant challenges were encountered during this exercise. However, I observed that converting input directly to an integer can raise a ValueError if the user enters non-numeric input. While this approach was used here for simplicity, in a real-world scenario it would be necessary to validate user input.

5) How I Overcame It:
No specific action was required, as no challenges were encountered.

6) Mistakes:
No mistakes were made during this exercise.

7) Improvements:
The output could be improved by using a multi-line string instead of multiple print statements, which may make the code easier to manage and read.
"""

digital_games = int(input("How many digital video games do you have? "))
physical_games = int(input("How many physical video games do you have? "))
favourite_game = input("What is your favourite video game? ")
collection = digital_games + physical_games

print(f"Your video game collection is made of {collection} games:")
print(f"- Digital games: {digital_games}")
print(f"- Physical games: {physical_games}")
print(f"- Favourite game: {favourite_game}")
print("Keep the game on!")