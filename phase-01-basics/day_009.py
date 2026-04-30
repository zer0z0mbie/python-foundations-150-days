"""
Day 9 – Getting User Input

1) Task:
Ask the user for input, store it in a variable, and display it.

2) What I Learnt:
When working with input, I learnt that it can be used to make programs more dynamic. In this short program, an alien greets a human and asks for their name. Once the input function is called, it stores the user’s name and returns it. This makes the program more interactive, as each user provides a different value for the variable human_name, meaning the program is no longer static.

I also observed that it is good practice to include a space at the end of the input prompt, so there is proper spacing between the prompt and what the user types. This helps improve the overall user experience.

3) Key Concepts:
- Input and output
- Dynamic data
- String handling

4) Challenges:
No significant challenges were encountered during this exercise. However, a potential challenge could arise when dealing with different data types, as input() returns a string by default. Additional steps would be required to handle other data types.

5) How I Overcame It:
No specific action was required, as no challenges were encountered.

6) Mistakes:
Although I did not make any mistakes when using the input function directly, I attempted to include the Vulcan salute (\\V/) in the output string. When I ran the program, it resulted in a SyntaxWarning. I resolved this by using an escape character, which allowed the string to be displayed correctly.

7) Improvements:
A possible improvement would be to allow the program to handle different types of input (e.g. numbers), which would require converting the input from a string to another data type.
"""

human_name = input("Greetings, human. What is your name? ")
alien_greeting = f"Live long and prosper, {human_name} \\V/"

print(alien_greeting)