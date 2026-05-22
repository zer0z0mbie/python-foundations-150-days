"""
Day 28 – Hierarchical State Systems

1) Task:
Create a program where:
- some states depend on higher-level states
- lower-level states should only exist if parent states are active
- the program must maintain a valid hierarchy of states

The goal is to make the program behave more like:
- a hierarchical system
instead of:
- flat independent state checks

2) What I Learnt:
While working on this exercise, I learnt that certain states rely on higher-level ones. For example, the program is a short game where, depending on the selected character (higher-level state), a specific attack (lower-level state) is activated if the player decides to attack.

Each attack is assigned to a specific character, meaning that different characters cannot perform the same attack. I believe this is an important concept because many real-world systems contain hierarchical structures where lower-level states depend on higher-level ones before certain actions or features become available.

3) Key Concepts:
- conditionals
- hierarchical states
- parent/child state relationships
- input/output
- procedural progression

4) Challenges:
No significant challenges were faced during this exercise.

5) How I Overcame It:
Not applicable.

6) Mistakes:
A small mistake was made in the action input statement:

action = int(input("Character chosen: (1/2/) "))

The message should have referred to the action selection instead of the character selection.

7) Improvements:
I would improve the input validation and expand the hierarchy system by adding more characters, attacks, and additional hierarchy combinations.
"""

# Higher-level states
ninja = False
samurai = False
wizard = False

# Lower-level states
stealth_assassination = False
katana_combo = False
fireball = False

char_chosen = None
attack_chosen = None

print("\nWelcome to Monsters against Heroes")
print(
    "\nCharacters Available:\n"
    "(1) Ninja\n"
    "(2) Samurai\n"
    "(3) Wizard"
)

char = int(input("Character chosen: (1/2/3) "))

if 0 < char < 4:
    if char == 1:
        ninja = True
        char_chosen = "Ninja"
    elif char == 2:
        samurai = True
        char_chosen = "Samurai"
    elif char == 3:
        wizard = True
        char_chosen = "Wizard"

    print(f"\nYou chose the {char_chosen}.\n")
    print(
        "What do you want to do?\n"
        "(1) Attack\n"
        "(2) Flee"
    )

    action = int(input("Choose an option: (1/2/) "))

    if 0 < action < 3:
        if action == 1:
            if ninja:
                stealth_assassination = True
                attack_chosen = "Stealth Assassination"
            elif samurai:
                katana_combo = True
                attack_chosen = "Katana Combo"
            elif wizard:
                fireball = True
                attack_chosen = "Fireball"
            print(f"\nYou attack with the {attack_chosen}!")
        elif action == 2:
            print("\nYou flee from combat.")
    else:
        print("\nAction does not exist")
else:
    print("\nChar does not exist")