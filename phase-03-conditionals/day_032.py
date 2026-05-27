"""
Day 32 – Memory-Based Access Systems

1) Task:
Create a program where:
- access to certain actions depends on remembered past decisions
- some features become permanently available or unavailable
- the program uses stored states to determine permissions and outcomes

The goal is to make the program behave more like:
- a memory-based access system
instead of:
- simple one-time conditional checks

2) What I Learnt:
While working on this exercise, I learnt that access checks can be implemented using conditional statements in Python. Depending on the user's input, progression can be saved in Boolean variables that can later be used to grant access permissions. Future events can be unlocked only if certain conditions are met.

3) Key Concepts:
- input/output
- conditional statements
- Boolean variables
- state tracking
- memory-based access systems
- permission systems

4) Challenges:
One challenge I faced was understanding which type of program I should create to illustrate this concept. Most of the examples I initially thought about were similar to previous exercises, and I wanted to create something different that would feel closer to real-world systems.

It was also challenging to understand how I should organise the conditional statements, especially regarding their order and how deeply nested the conditionals should be.

Another challenge was ensuring that the message "Wrong password. Admin dashboard access denied." would not be printed when the user selected the Editor or Moderator dashboards.

5) How I Overcame It:
To overcome these challenges, I broke down the problem into smaller steps and tested the program continuously. In addition, I experimented with organising the program sections in different orders.

Regarding the "Wrong password. Admin dashboard access denied." message, I used the sys.exit() function and ensured that the outputs for the Editor and Moderator dashboard sections appeared before the Admin dashboard output.

6) Mistakes:
No mistakes made during this exercise.

7) Improvements:
I would improve the password security (a simple example was used here for practice purposes) and also add user input validation.
"""

import sys
import string

admin_password = "Bananarama!"
admin_dashboard_access = False
regular_dashboard_access = False

user_name = string.capwords(input("What's your name? "))

dashboard_chosen = int(
    input(
        f"Hi, {user_name}.\n"
        "Which dashboard do you want to access?\n"
        "(1) Admin\n"
        "(2) Editor\n"
        "(3) Moderator\n"
        "Choose an option: (1-3) "
    )
)

# If admin dashboard is chosen, asks for password
if dashboard_chosen == 1:
    password = input("Please enter your password: ")

    # Access granted if password inputted matches admin password
    if password == admin_password:
        admin_dashboard_access = True
else:
    regular_dashboard_access = True

# Editor/Moderator Dashboards
if regular_dashboard_access:
    if dashboard_chosen == 2:
        print("Editor dashboard access granted.")
        sys.exit()
    elif dashboard_chosen == 3:
        print("Moderator dashboard access granted.")
        sys.exit()

# Admin Dashboard
if admin_dashboard_access:
    print("Admin dashboard access granted.")
else:
    print("Wrong password. Admin dashboard access denied.")
