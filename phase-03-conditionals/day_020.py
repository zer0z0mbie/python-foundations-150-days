"""
Day 20 – Multi-Step Decision Flow

1) Task:
Create a program where:
- an initial condition determines whether the program continues
- additional conditions then determine different outcomes

The program should feel like:
- a small decision process
rather than:
- a single isolated condition

2) What I Learnt:
I learnt how to use more than one condition in a program. I also learnt how one decision can lead to another decision, which helped me understand how procedural flow works in practice.

3) Key Concepts:
- if statements
- nested conditions
- user input
- procedural flow

4) Challenges:
It was initially confusing to know where to place the second if statement and how to organise the logic clearly.

5) How I Overcame It:
I fixed it by checking my indentation carefully and testing different answers to observe how the program flow changed depending on the user input.

6) Mistakes:
A potential mistake in this exercise would be placing the second conditional statement outside the permission check, which would allow users without permission to access the second decision flow.

7) Improvements:
Next time, I would add input validation and more choices to make the program easier to use and more interactive.
"""

user_permission = input("Do you have admin permission?").lower()

continue_running = user_permission == "yes"

if continue_running:
    print("Access granted.")
    action = input("Do you want to view or edit files? ").lower()
    if action == "view":
        print("Opening files in read-only mode.")
    elif action == "edit":
        print("Editing access enabled.")
    else:
        print("Unknown action.")
else:
    print("No permission to continue.")