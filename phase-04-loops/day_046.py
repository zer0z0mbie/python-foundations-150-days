"""
Day 46 – Event Counting Loops

1. Task:
Create a program where:
- a loop processes multiple events
- the program keeps track of how many times specific events occur
- the final result is determined using the collected event counts

The goal is to make the program behave more like:
- an event-tracking system
instead of:
- a simple repetition system

2. What I Learnt:
While working on this exercise, I learnt that event-counting loops can be used in programs that process multiple events and keep track of how many times specific events occur.

In this short game, the player encounters three different enemies and fights them throughout multiple rounds. Each encounter is recorded using separate counters, and the current round number is also tracked. At the end of the game, the encounter statistics are displayed to the player.

To achieve this, I used a combination of while loops, for loops, counters, and dictionaries.

This exercise helped me understand how counters can be used to collect statistics while a program is running and how those statistics can later be summarised and displayed to the user.

3. Key Concepts:
- while loops
- for loops
- event counting
- counters
- dictionaries
- random events
- game statistics

4. Challenges:
One challenge was understanding how to correctly update an enemy’s HP after it suffered damage.

5. How I Overcame It:
I used IDLE and Python Tutor to visualise the code while it was running. I also reviewed dictionary methods because the last time I used dictionaries was during a college assignment and I needed a refresher.

Initially, I attempted to reduce the enemy’s HP using:
    for enemy, hp in enemies.items():
        if enemy == current_enemy:
            hp -= player_attack_damage

However, the HP value stored in the dictionary was not being updated.

After researching the issue, I realised that modifying the hp variable only changed the temporary value stored in the loop variable rather than the value inside the dictionary itself. I corrected this by updating the dictionary directly using:
    enemies[enemy] -= player_attack_damage

6. Mistakes:
Initially, I attempted to reduce the enemy’s HP by modifying the hp variable obtained from:
    for enemy, hp in enemies.items():

However, changing hp did not update the value stored in the dictionary.

I corrected this mistake by updating the dictionary directly:
    enemies[enemy] -= player_attack_damage

7. Improvements:
I would reduce some of the repetition in the combat system and look for ways to simplify the enemy-selection and combat logic. I could also determine which enemy was encountered the most and display this information in the final statistics. Another improvement would be tracking additional statistics such as total damage dealt, total damage received, and the number of enemies defeated.
"""

from random import choice, randint
from time import sleep
from string import capwords

player_name = capwords(input("What's your name, warrior? > "))
player_hp = 100 # Initialises player's HP

enemies = {
    "Dark Elf": 100, # Initialises Dark Elf's HP
    "Necromancer": 100, # Initialises Necromancer's HP
    "Fire Dragon": 100 # Initialises Fire Dragon's HP
}

# Counters
current_round = 0
dark_elf_encounters = 0
necromancer_encounters = 0
fire_dragon_encounters = 0

print(
    f"\n{player_name} enters the dungeon.\n"
    f"{', '.join(enemies)} spawn.\n"
)

while len(enemies) > 0 and player_hp > 0:
    current_round += 1

    # Displays the current round
    print(f"Round {current_round}:")

    # Picks a random enemy
    current_enemy = choice(list(enemies.keys()))

    # Counts the encounter
    if current_enemy == "Dark Elf":
        dark_elf_encounters += 1
    elif current_enemy == "Necromancer":
        necromancer_encounters += 1
    elif current_enemy == "Fire Dragon":
        fire_dragon_encounters += 1

    # Set attack damage variables
    current_enemy_attack_damage = randint(5, 10)
    player_attack_damage = randint(15, 30)

    for enemy in enemies:
        if enemy == current_enemy:
            # Player turn
            print(f"{player_name} turn:")

            enemies[enemy] -= player_attack_damage

            print(
                f"{player_name} attacks and deals {player_attack_damage} to {current_enemy}.\n"
                "Outcome:", end=" "
            )

            if enemies[enemy] <= 0:
                print(f"{current_enemy} dies.")
                enemies.pop(current_enemy)
                break

            else:
                # Enemy turn
                print(
                    f"{current_enemy} survives.\n"
                    f"\n{current_enemy} turn:"
                )

                player_hp -= current_enemy_attack_damage

                print(
                    f"{current_enemy} attacks and deals {current_enemy_attack_damage} to {player_name}.\n"
                    "Outcome:", end=" "
                )

                if player_hp <= 0:
                    print(f"{player_name} dies.")
                    break
                else:
                    print(f"{player_name} survives.\n")

                print(
                    "--*--*--*--*--*--*--*--*--\n"
                    "Round Stats:\n"
                    f"{player_name} took {current_enemy_attack_damage} damage.\n"
                    f"{player_name} HP: {player_hp}\n"
                    "\n"
                    f"{current_enemy} took {player_attack_damage} damage.\n"
                    f"{current_enemy} HP: {enemies[enemy]}\n"
                    f"--*--*--*--*--*--*--*--*--\n"
                )

    for time in [3, 2, 1]:
        print(f"Next round starts in {time}...")
        sleep(1)
    print()

print(
    "Game Stats:\n"
    f"Dark Elf Encounters: {dark_elf_encounters}\n"
    f"Necromancer Encounters: {necromancer_encounters}\n"
    f"Fire Dragon Encounter: {fire_dragon_encounters}\n"
    "Thank you for playing!"
)

input("Press ENTER to exit.")
