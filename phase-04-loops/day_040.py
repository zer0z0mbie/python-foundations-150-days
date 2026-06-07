"""
Day 40 – Introduction to Loops

1) Task:
Create a program where:
- an action can repeat multiple times
- the user can continue interacting until they choose to stop
- the program avoids duplicating code by repeating a section automatically

The goal is to make the program behave more like:
- a repeating system
instead of:
- a one-time execution system

2) What I Learnt:
While working on this exercise, I reinforced my understanding of how loops can be used to repeat a section of code automatically instead of writing the same code multiple times.

In this example, the user repeatedly guesses a secret number. After each incorrect guess, the program continues running and asks for another guess. This process repeats until the correct number is entered.

I also learnt that a while loop can keep a program running as long as a condition remains true. By using "while True", the program creates an infinite loop that continues until a break statement is reached.

This exercise helped me understand how loops can be used to create interactive programs that continue running until a specific condition is met.

3) Key Concepts:
- loops
- while loops
- repetition
- user input
- conditional statements
- break statement
- infinite loops

4) Challenges:
One challenge was understanding how the loop knows when to stop repeating. At first, it may seem like "while True" would cause the program to run forever.

5) How I Overcame It:
I overcame this by using a break statement inside the loop. When the user enters the correct secret number, the break statement immediately exits the loop and ends the repeating process.

6) Mistakes:
A potential mistake would be forgetting to include a break statement when using "while True", which would cause the program to run indefinitely.

Another potential mistake would be placing the break statement in the wrong location, causing the loop to end too early or not end when intended.

A further mistake would be not validating user input, which could cause a ValueError if the user enters text instead of a number.

7) Improvements:
I would add input validation to prevent crashes when non-numeric values are entered.

I could also count the number of guesses made by the user and display the total when they successfully guess the secret number.

Another improvement would be to provide hints, such as whether the guess is too high or too low, to make the game more interactive.
"""

secret_number = 7

while True:
    user_number = int(input("Guess the secret number: "))

    if user_number == secret_number:
        print("Correct! You guessed the secret number.")
        break
    else:
        print("Wrong number. Guess again.")