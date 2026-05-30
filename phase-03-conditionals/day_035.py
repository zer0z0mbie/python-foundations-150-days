"""
Day 35 – Cascading State Systems

1. Task:
   Create a program where:

* one state change can trigger multiple other state changes
* a single decision can create a chain reaction throughout the system
* multiple states may be affected indirectly by earlier events

The goal is to make the program behave more like:

* a cascading state system
  instead of:
* a simple state dependency chain

2. What I Learnt:
   While working on this exercise, I was able to visualise how a single decision can create a chain reaction throughout the system.

For example, once the player enters Room B, a zombie encounter begins. The player then performs a series of actions, such as taking cover and deciding whether to reload their weapon. Depending on the actions chosen, a new series of events takes place.

At the end of the encounter, the player will either survive or die. During this example, multiple states were affected, with the main cascade occurring after entering Room B, while entering Room A leads directly to the player's death.

This exercise reinforced my understanding of cascading state systems and how a single decision can create several dependent events throughout a program.

3. Key Concepts:

* input/output
* conditional statements
* nested conditionals
* Boolean variables
* state tracking
* cascading state systems
* chained state dependencies

4. Challenges:
   No particular challenges were faced.

5. How I Overcame It:
   Not applicable.

6. Mistakes:
   When writing the condition that checks whether the weapon was reloaded, I accidentally checked reload_weapon instead of weapon_reloaded. This caused a semantic error because the message stating that the player blew the zombie's head off was printed even when the weapon had not been reloaded.

7. Improvements:
   I would add input validation to prevent invalid choices from being entered.

I would also continue looking for opportunities to reduce unnecessary states and improve the organisation of the program while maintaining readability.

Additionally, some narrative events, such as taking cover, could be converted into proper program states in future versions so that they directly affect later events and outcomes.
"""

enters_room_a = False
enters_room_b = False

weapon_reloaded = False

failed_shot = False
successful_shot = False

zombie_attacks = False
kills_zombie = False
trap_activated = False

survived = False
died = False

print("You're trying to survive a zombie apocalypse.")

room_chosen = input(
    "You find two rooms.\n"
    "Which one do you enter? (A/B) "
).lower()

if room_chosen == "a":
    print("You enter room A.")
    enters_room_a = True
elif room_chosen == "b":
    print("You enter room B.")
    enters_room_b = True

if enters_room_a:
    print("You hear a click.")
    trap_activated = True
elif enters_room_b:
    print(
        "A hungry zombie approaches.\n"
        "You quickly take cover."
    )

    reload_weapon = input("Do you reload your gun? (Y/N) ").lower()

    if reload_weapon == "y":
        print("You get the ammo out of your pockets and reload your gun as fast as you can.")
        weapon_reloaded = True

    print("The zombie gets closer. You aim at its head, pull the trigger, and", end =" ")

    if weapon_reloaded:
        print("blow its head off")
        successful_shot = True
    else:
        print(
            "hear an empty click sound.\n"
            "Your gun is empty, so you miss the shot."
        )
        failed_shot = True

    if successful_shot:
        print("You kill the zombie.")
        kills_zombie = True
        survived = True
    elif failed_shot:
        print("The zombie hits you to the ground and bites you.")
        zombie_attacks = True
        died = True

if trap_activated:
    print("A booby trap is activated.")
    died = True

if survived:
    print("You survived.")

if died:
    print("You died.")
