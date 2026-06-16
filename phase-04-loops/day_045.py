"""
Day 45 – Loop-Controlled Retry Systems

1. Task:
Create a program where:
- the user can repeatedly retry an action after failure
- the loop continues until success or until retries are exhausted
- the program keeps track of remaining attempts

The goal is to make the program behave more like:
- a retry system
instead of:
- a one-attempt system

2. What I Learnt:
While working on this exercise, I learnt that loops can be used to create retry systems. Counters can be added to limit the number of attempts, which is useful in real-world applications such as password entry systems and login authentication.

To demonstrate this concept, I created a simple game where the player must guess a secret word in order to open a mystical door.

This exercise helped me understand how loops, counters, and conditional statements can work together to control the number of retries available to a user. It also showed how the program can respond differently depending on whether the player succeeds before running out of attempts.

3. Key Concepts:
- while loops
- retry systems
- counters
- conditional statements
- loop termination
- success and failure states

4. Challenges:
One challenge was deciding how to manage the remaining attempts while ensuring that the player received the correct number of retries.

5. How I Overcame It:
I overcame this challenge by testing the program multiple times and manually tracking the value of the attempts_left variable after each incorrect guess.

6. Mistakes:
One mistake was in the loop condition:

while player_guess != secret_word and attempts_left > 1:

This caused the loop to stop when attempts_left reached 1, meaning the player never received their final attempt.

7. Improvements:
I could add input validation to ensure that only valid responses are accepted.

I could also display both the remaining attempts and the total number of attempts used.

Another improvement would be allowing the player to choose a difficulty level, which could change the number of available attempts.
"""

secret_word = "abracadabra"
attempts_left = 5
total_attempts = 0

user_ready = input("Are you ready to play the game? > ").upper()

while user_ready != "Y":
    print("You must type 'Y' to start the game.")
    user_ready = input("Are you ready to play the game? > ").upper()

print(
    "\nYou come across a mystical door.\n"
    "To open it, you must say the secret word.\n"
)

while attempts_left > 0:
    player_guess = input("What's the secret word? > ").lower()
    total_attempts += 1

    if player_guess == secret_word:
        break

    attempts_left -= 1

    if attempts_left > 0:
        print(
            f"'{player_guess}' is not the secret word.\n"
            f"Attempts left: {attempts_left}\n"
            "Please try again!\n"
        )

if player_guess == secret_word:
    print(
        f"Congratulations, you guessed the secret word: '{secret_word}'!\n"
        f"Total attempts: {total_attempts}\n"
        "Thank you for playing the game."
    )
else:
    print(
        "No more attempts. You cannot enter the door.\n"
        f"Total attempts: {total_attempts}"
    )