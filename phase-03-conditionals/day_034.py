"""
Day 34 – Dynamic State Networks

1) Task:
Create a program where:
- multiple states influence each other
- changing one state can affect several other states
- the program reacts to a network of connected conditions

The goal is to make the program behave more like:
- a dynamic state network
instead of:
- isolated state interactions

2) What I Learnt:
While working on this exercise, I learnt that states can influence one another and that a single decision can trigger multiple effects.

In this example, selecting a specific animal determines the outcome of the encounter (snake = poisoned, wolf = bitten, and bear = mauled). These injury states can then lead to a low-energy state, which influences future decisions and outcomes.

This exercise helped me understand that one state can create another state, which can then affect later parts of the program. Rather than moving directly from an initial event to a final outcome, the program can pass through multiple connected states before reaching a conclusion.

3) Key Concepts:
- input/output
- conditional statements
- nested conditionals
- Boolean variables
- state tracking
- dynamic state networks
- chained state dependencies

4) Challenges:
No challenges were faced, as I have become more confident using conditional statements at this stage.

5) How I Overcame It:
Not applicable.

6) Mistakes:
No mistakes made.

However, during the review process, I realised that my initial solution did not fully demonstrate a dynamic state network because the states led directly to the outcomes. I improved the solution by introducing an intermediate state (energy_low), allowing one state to create another state before determining the final outcome.

7) Improvements:
I would improve the same points mentioned in previous exercises, such as adding loops, functions, and input validation. However, I am intentionally avoiding more advanced concepts for now in order to respect the requirements of the challenge and build discipline while working within the current limitations.

For example, users can currently enter numbers outside the available options. In a real-world application, this would need to be addressed through proper validation. For the purposes of this exercise, I assumed a controlled environment where users always provide valid input.
"""

animal_interacted = None

poisoned = False
bitten = False
mauled = False

energy_low = False

died = False
passed_out = False
survived = False

animal_interaction = int(
    input(
    "You walk into a small forest and come across these animals:\n"
    "(1) Snake\n"
    "(2) Wolf\n"
    "(3) Bear\n"
    "Which animal do you interact with? (1-3) "
    )
)

if animal_interaction == 1:
    animal_interacted = "snake"
    poisoned = True
elif animal_interaction == 2:
    animal_interacted = "wolf"
    bitten = True
elif animal_interaction == 3:
    animal_interacted = "bear"
    mauled = True

print(f"You try petting the {animal_interacted}, but the {animal_interacted} attacks you.")

if poisoned:
    action = int(
        input(
            f"You start feeling fatigued as the {animal_interacted}'s poison goes through your body.\n"
            "You have two options:\n"
            "(1) Wait for help\n"
            "(2) Run\n"
            "What do you do? (1-2) "
        )
    )

    if action == 1:
        died = True
    elif action == 2:
        energy_low = True

if bitten:
    action = int(
        input(
            f"You feel a strong pain coming from the open wounds caused by the {animal_interacted}'s bite.\n"
            "You have two options:\n"
            "(1) Face the wolf\n"
            "(2) Run\n"
            "What do you do? (1-2) "
        )
    )

    if action == 1:
        died = True
    elif action == 2:
        energy_low = True

if mauled:
    action = int(
        input(
            f"The {animal_interacted}'s claws are too strong, throwing you to the ground.\n"
            "You have two options:\n"
            "(1) Pretend you are dead\n"
            "(2) Run\n"
            "What do you do? (1-2) "
        )
    )

    if action == 1:
        died = True
    elif action == 2:
        energy_low = True

if energy_low:
    action = int(
        input(
            "You run as fast as you can, but your body is too weak...\n"
            "You have two options:\n"
            "(1) Keep running\n"
            "(2) Take a quick breath, eat a fruit, and run again\n"
            "What do you do? (1-2) "
        )
    )

    if action == 1:
        passed_out = True
    elif action == 2:
        survived = True

if died:
    if animal_interacted == "snake":
        print(
            "You wait for help, but nobody comes.\n"
            f"The {animal_interacted}'s poison lays you to rest foreve"
        )
    elif animal_interacted == "wolf":
        print(
            f"You try attacking the {animal_interacted}, but its pack joins the party.\n"
            "You're bitten to death."
        )
    elif animal_interacted == "bear":
        print(
            f"The {animal_interacted} smells you and decides to make you its dinner\n"
            f"Your new house is the {animal_interacted}'s stomach."
        )

if passed_out:
    print("You pass out.")

if survived:
    print(
        "You manage to escape the small forest.\n"
        "You survive."
    )