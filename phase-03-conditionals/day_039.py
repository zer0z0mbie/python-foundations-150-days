"""
Day 39 – Conditional Priority Systems

1. Task:
Create a program where:
- multiple states may be active at the same time
- some states take priority over others
- the final outcome depends on which conditions are considered most important

The goal is to make the program behave more like:
- a conditional priority system
instead of:
- a simple condition combination system

2. What I Learnt:
While working on this exercise, I learnt how multiple states can exist at the same time while certain states take priority when determining the final outcome.

In this example, the player can become armed, infected, escape, or die. Some of these states can be active simultaneously. For example, the player may pick up a weapon and gain the ability to escape, but still become infected by a zombie.

Rather than treating all active states equally, the program uses a priority system. Death is considered more important than escape, so if both the death and escape states are active at the same time, the death outcome is displayed because it has higher priority.

This exercise helped me understand how priority systems can be used to resolve situations where multiple outcomes are possible by selecting the most important condition.

3. Key Concepts:
- input/output
- conditional statements
- Boolean variables
- state tracking
- conditional priority systems
- outcome prioritisation
- logical operators

4. Challenges:
One challenge was deciding how to handle situations where multiple outcome states could be active at the same time.

5. How I Overcame It:
I overcame this by using an if/elif structure for the final outcome checks. This allowed higher-priority conditions to be evaluated first and prevented lower-priority outcomes from being displayed when a more important condition was active.

6. Mistakes:
A potential mistake would be using separate if statements for the final outcomes, which could cause multiple conflicting outcomes to be displayed.

Another potential mistake would be checking lower-priority conditions before higher-priority conditions, resulting in incorrect behaviour.

7. Improvements:
I would add input validation to ensure that only valid responses can be entered.

I could also introduce additional states such as finding a cure, being rescued, or running out of ammunition to create a more complex priority hierarchy.

Another improvement would be to assign several outcome levels and explicitly rank them from highest to lowest priority.
"""

import random

armed = False
infected = False
escaped = False
died = False

print("Zombie Survival Simulator")

print("A horde of zombies approaches...")

pick_weapon = input("Do you pick up a weapon? (Y/N) ").lower()

if pick_weapon == "y":
    armed = True

print("A starving zombie approaches you...")

zombie_bites = random.choice(["success", "fail"])

if zombie_bites == "success":
    print("The zombie bites you, but you manage to get away.")
    infected = True
elif zombie_bites == "fail":
    print("You avoid the zombie and escape.")
    escaped = True

if infected:
    died = True

if armed:
    escaped = True

if died:
    print("You died.")
elif escaped:
    print("You escaped.")
