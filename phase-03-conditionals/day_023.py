"""
Day 23 – Combining Multiple Paths

1) Task:
Create a program where:
- different combinations of conditions lead to different execution paths
- the program can follow multiple possible routes depending on user input
- some paths should contain additional checks or outcomes

The goal is to make the program behave more like:
- a branching system
instead of:
- a single linear flow

2) What I Learnt:
While working on this exercise, I created a program that helps users who live in the southside, central, and northside areas plan their journeys. I noticed that the order of conditionals is really important, especially in situations where longer and shorter distances are being considered.

For example, users who live in either of the two extremes (north or south) require further checks in case they decide to travel from one extreme to the other, while users living in the central area travel the same distance when going from central to northside or central to southside. Therefore, users travelling from the southside or northside required additional checks.

Multiple execution paths can occur because travelling from the southside or northside to the central area in under one hour may be possible using an express bus or buses.

3) Key Concepts:
- input
- conditionals
- multiple paths
- "or" logical operator

4) Challenges:
At the beginning, I was unsure how to start. I initially created separate if and elif structures for the "s" and "n" starting points, but I noticed that the code was becoming more complex and larger.

5) How I Overcame It:
As the theoretical distances in this application are the same from south to central and north to central, as well as from south to north and north to south, I ended up combining those conditions into:

if starting_point == "s" or starting_point == "n"

This simplified the code significantly and reduced duplicated logic.

6) Mistakes:
No mistakes made.

7) Improvements:
Add input validation.
"""

print("\nWelcome to the Journey Planner")
print("==================================")
print(
    "\nWe cover the Southside (S), Central (C),"
    "and Northside areas of town.\n"
)
print("==================================")
print(
    "Transportation:\n"
    "- Bus\n"
    "- Express Bus\n"
    "- Tram\n"
    "- Train\n"
)

starting_point = input("What is your starting point? (S/C/N) ").lower()
destination = input("What is your final destination? (S/C/N) ").lower()

if starting_point == destination:
    print("Starting point and destination cannot be the same.")
else:
    if starting_point == "s" or starting_point == "n":
        if destination == "c":
            arrival_time = int(input(
                "When do you need to arrive?\n"
                "Under 30 min (1)\n"
                "Under 1 hour (2)\n"
                "More than 1 hour (3)\n"
                "Choose an option (1/2/3) : "
            ))

            if arrival_time == 1:
                print("You can take the tram.")
            elif arrival_time == 2:
                maximum_stops = int(input("Maximum number of stops: (1/2) "))

                if maximum_stops == 1:
                    print("You can take the express bus.")
                else:
                    print("You can take two buses.")
            else:
                print("You can take three buses and the tram.")
        else:
            print("You can take the train.")
    else:
        maximum_stops = int(input("Maximum number of stops: (1/2) "))

        if maximum_stops == 1:
            print("You can take the express bus.")
        else:
            print("You can take two buses.")