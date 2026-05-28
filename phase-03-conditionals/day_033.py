"""
Day 33 – Persistent Multi-Role Systems

1) Task:
Create a program where:
- multiple remembered states interact together
- different combinations of states produce different permissions or outcomes
- the program supports multiple persistent roles or conditions simultaneously

The goal is to make the program behave more like:
- a persistent multi-role system
instead of:
- isolated single-permission checks

2) What I Learnt:
While working on this exercise, I learnt how multiple Boolean variables can interact together to create more complex systems. Instead of checking only one condition at a time, the program combines several remembered states, such as the character role, the time of day, and the chosen action, to determine different outcomes.

I also learnt how persistent role systems work by allowing different characters to access different actions and events. Some actions produce different results depending on whether it is day or night, which made the program feel more dynamic and interconnected.

In addition, I improved my understanding of nested conditional statements and how to organise large conditional structures without losing track of the program flow.

3) Key Concepts:
- input/output
- conditional statements
- nested conditionals
- Boolean variables
- state tracking
- multi-role systems
- permission systems
- persistent conditions

4) Challenges:
One challenge I faced was organising the large number of conditional statements. Since each character had different actions depending on the time of day, it became difficult to structure the program cleanly without getting confused.

Another challenge was making the interactions feel connected instead of isolated. I wanted certain events to react differently depending on multiple states being active at the same time, such as the Royal Guard arresting the Commoner during the night invasion.

It was also sometimes difficult to keep track of all the Boolean variables and ensure that the correct actions and outputs were triggered.

5) How I Overcame It:
To overcome these challenges, I divided the program into sections: character selection, time selection, action selection, and event outcomes. This helped me understand the flow of the program more clearly.

I also used descriptive Boolean variable names to make the conditions easier to read and debug. In addition, I tested the program repeatedly using different combinations of roles, times, and actions to ensure that the correct outcomes appeared.

6) Mistakes:
No major mistakes were made during this exercise.

However, I noticed that some inputs are not validated, meaning the user could enter numbers outside the available options and potentially create unexpected behaviour.

I also noticed that one conditional path became unreachable due to conflicting states. The invade_the_castle action could only happen at night, meaning the condition if invade_the_castle and is_day could never execute simultaneously.

7) Improvements:
Next time, I would improve the program by reducing repetition in the conditional statements. Some sections could be simplified using functions or dictionaries.

I would also add proper input validation to prevent invalid options from being entered.

Another improvement would be allowing multiple characters to exist simultaneously within the same session so that actions from one character could directly affect another character later in the story.
"""

# Character options
is_king = False
is_royal_guard = False
is_wizard = False
is_commoner = False

# Time of the day
is_day = False
is_night = False

# Actions to do
enter_royal_grounds = False
visit_imperial_library = False
practice_falconry = False
guard_the_castle = False
arrest_intruder = False
invade_the_castle = False
teleport = False
visit_flea_market = False
visit_tavern = False
fish = False
bath = False

print("Welcome to the Medieval Tale")

char = int(
    input(
        "Choose your character:\n"
        "(1) King\n"
        "(2) Royal Guard\n"
        "(3) Wizard\n"
        "(4) Commoner\n"
        "Choose an option (1-4): "
    )
)

if char == 1:
    is_king = True
elif char == 2:
    is_royal_guard = True
elif char == 3:
    is_wizard = True
elif char == 4:
    is_commoner = True

day_or_night = int(
    input(
        "Choose the time of the day:\n"
        "(1) Day\n"
        "(2) Night\n"
        "Choose an option (1-2): "
    )
)

if day_or_night == 1:
    is_day = True
elif day_or_night == 2:
    is_night = True

if is_day:
    if is_king:
        action = int(
            input(
                "What do you do:\n"
                "(1) Enter royal grounds\n"
                "(2) Visit imperial library\n"
                "(3) Practice falconry\n"
                "Choose an option (1-3): "
            )
        )

        if action == 1:
            enter_royal_grounds = True
        elif action == 2:
            visit_imperial_library = True
        elif action == 3:
            practice_falconry = True
    elif is_royal_guard:
        action = int(
            input(
                "What do you do:\n"
                "(1) Guard the castle\n"
                "(2) Arrest intruder\n"
                "Choose an option (1-2): "
            )
        )

        if action == 1:
            guard_the_castle = True
        elif action == 2:
            arrest_intruder = True
    elif is_wizard:
        action = int(
            input(
                "What do you do:\n"
                "(1) Visit imperial library\n"
                "(2) Teleport\n"
                "Choose an option (1-2): "
            )
        )

        if action == 1:
            visit_imperial_library = True
        elif action == 2:
            teleport = True
    elif is_commoner:
        action = int(
            input(
                "What do you do:\n"
                "(1) Visit flea market\n"
                "(2) Fish\n"
                "Choose an option (1-2): "
            )
        )

        if action == 1:
            visit_flea_market = True
        elif action == 2:
            fish = True
elif is_night:
    if is_king:
        action = int(
            input(
                "What do you do:\n"
                "(1) Enter royal grounds\n"
                "(2) Bath\n"
                "Choose an option (1-2): "
            )
        )

        if action == 1:
            enter_royal_grounds = True
        elif action == 2:
            bath = True
    elif is_royal_guard:
        action = int(
            input(
                "What do you do:\n"
                "(1) Guard the castle\n"
                "(2) Arrest intruder\n"
                "Choose an option (1-2): "
            )
        )

        if action == 1:
            guard_the_castle = True
        elif action == 2:
            arrest_intruder = True
    elif is_wizard:
        action = int(
            input(
                "What do you do:\n"
                "(1) Visit tavern\n"
                "(2) Teleport\n"
                "Choose an option (1-2): "
            )
        )

        if action == 1:
            visit_tavern = True
        elif action == 2:
            teleport = True
    elif is_commoner:
        action = int(
            input(
                "What do you do:\n"
                "(1) Visit tavern\n"
                "(2) Invade the castle\n"
                "Choose an option (1-2): "
            )
        )

        if action == 1:
            visit_tavern = True
        elif action == 2:
            invade_the_castle = True


if enter_royal_grounds:
    if is_day:
        print("You welcome the noble families in the Royal Garden.")
    if is_night:
        print("You feast with the noble families in the Banqueting Hall.")
if visit_imperial_library:
    if is_king:
        print("You look for the wizard to request a potion.")
    if is_wizard:
        print("You come across the king, who requests you a potion.")
if practice_falconry:
    print("You practice falconry with the fire falcons from the Scarlet region.")
if guard_the_castle:
    if is_day:
        print(
            "You patrol the interior of the castle.\n"
            "Everything is calm."
        )
    if is_night:
        print(
            "You patrol the exterior of the castle.\n"
            "The night is as quiet as the moon."
        )
if arrest_intruder:
    if is_day:
        print("During your guard, you find no intruders.")
    if is_night:
        print(
            "You notice a commoner invading the castle.\n"
            "You arrest him."
        )
if invade_the_castle:
        print(
            "You invade the castle through the side walls.\n"
            "A guard spots you and arrests you."
        )
if teleport:
    if is_day:
        print("You teleport to the Dwarf Forest.")
    if is_night:
        print("You teleport to the secret catacomb.")
if visit_flea_market:
    print("You notice an unattended market stall and steal a loaf of bread.")
if visit_tavern:
    if is_wizard:
        print("You get drunk but use a spell to get sober.")
    if is_commoner:
        print("You ask for a job but you're kicked out instead.")
if fish:
    print("You spend the whole day trying fishing but can't get any fish. You pass out.")
if bath:
    print("You have your yearly shower.")