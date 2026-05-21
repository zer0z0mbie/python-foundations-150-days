"""
Day 27 – State Conflicts and Resolution

1) Task:
Create a program where:
- multiple states can conflict with each other
- some state combinations are incompatible
- the program must detect and resolve conflicting states correctly

The goal is to make the program behave more like:
- a controlled state-management system
instead of:
- independent state checks with no conflict handling

2) What I Learnt:
While working on this exercise, I learnt that multiple states can conflict with each other. For example, in a blog management application, depending on the permission level, users may be able to perform operation X but not operation Y (e.g., admins being able to view dashboards while not being allowed to edit them).

This exercise further reinforced my understanding of conditional logic and demonstrated how important well-designed conditions are. In some real-world scenarios, if the logic is not implemented correctly, users could be granted access to features they should not have access to (e.g., an editor being able to edit the dashboard).

3) Key Concepts:
- conditional statements
- input/output
- multiple states
- managing and resolving conflicting states

4) Challenges:
No significant challenges were faced during this exercise.

5) How I Overcame It:
Not applicable.

6) Mistakes:
In the condition:
if 0 < permission_level < 5

I accidentally wrote:
if 1 < permission_level < 4

which caused a logical error because permission levels 1 and 4 were ignored. This was identified during the first execution of the program and was an easy fix.

7) Improvements:
I believe an improvement would be adding user input validation and creating more complex permission combinations with additional restricted operations.
"""

# Permission level state variables
is_editor = False
is_moderator = False
is_admin = False
is_super_admin = False

# Welcomes user
username = input("\nUsername: ")

print(f"\n👾 👾 👾 Welcome to the Gameplay Blog, {username} 👾 👾 👾\n")

# Permission level
print(
    "What is your permission level?\n"
    "(1) Editor\n"
    "(2) Moderator\n"
    "(3) Admin\n"
    "(4) Super Admin\n"
)

permission_level = int(input("Choose an option: (1/2/3/4) "))

if 0 < permission_level < 5:
    if permission_level == 1:
        is_editor = True
    elif permission_level == 2:
        is_moderator = True
    elif permission_level == 3:
        is_admin = True
    elif permission_level == 4:
        is_super_admin = True

    # Blog operation
    print(
        "\nWhat do you want to do?\n"
        "(1) Write an Article\n"
        "(2) Moderate\n"
        "(3) View Dashboard\n"
        "(4) Edit Dashboard\n"
    )

    blog_operation = int(input("Choose an option: (1/2/3/4) "))

    # Access granted/denied
    if 0 < blog_operation < 5:
        if blog_operation == 1:
            print("Access granted.")
        elif blog_operation == 2:
            if is_editor:
                print("Access denied")
            else:
                print("Access granted.")
        elif blog_operation == 3:
            if is_admin or is_super_admin:
                print("Access granted.")
            else:
                print("Access denied.")
        elif blog_operation == 4:
            if is_super_admin:
                print("Access granted.")
            else:
                print("Access denied.")
    else:
        print("Operation invalid.")
else:
    print("Permission level invalid.")
