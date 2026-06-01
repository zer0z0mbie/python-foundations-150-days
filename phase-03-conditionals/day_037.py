"""
Day 37 – State Persistence Across Multiple Events

1. Task:
Create a program where:
- states persist across several separate events
- earlier decisions continue affecting later situations
- multiple events occur before the final outcome is determined

The goal is to make the program behave more like:
- a persistent event system
instead of:
- a single-event state system

2. What I Learnt:
While working on this exercise, I learnt how states can persist throughout multiple events and continue affecting later parts of a program.

In this example, the player's early decisions occur before the hike begins. Choosing whether to charge the phone and refill the water bottle creates states that remain active for the rest of the program.

Later events, such as becoming thirsty and getting lost in the dark, rely on those earlier states. The program does not immediately determine the outcome after the initial decisions. Instead, several separate events occur, and the final result is only calculated after all relevant situations have been processed.

This exercise reinforced my understanding of persistent state systems and demonstrated how earlier choices can influence multiple future events.

3. Key Concepts:
- input/output
- conditional statements
- Boolean variables
- state tracking
- persistent states
- event-driven progression
- multi-stage outcomes

4. Challenges:
No particular challenges were faced during this exercise.

5. How I Overcame It:
Not applicable.

6. Mistakes:
One potential mistake would be determining the final outcome too early. Since the purpose of this exercise is to allow states to persist across multiple events, the outcome should only be evaluated after all events have occurred.

I also had to ensure that the phone_charged and water_bottle_refilled states remained available throughout the entire program so they could affect later situations.

7. Improvements:
I would add input validation to ensure that only valid responses can be entered.

I could also expand the hiking scenario by introducing additional events, such as bad weather, injuries, or finding shelter, allowing the persistent states to influence additional situations.

Another improvement would be to provide alternative ways to escape if the phone is not charged, making the system more dynamic and realistic.
"""

phone_charged = False
water_bottle_refilled = False
thirsty = True
lost = False
escape = False

print("You're about to go hiking.")

charge_phone = input("Do you charge your phone? (Y/N) ").lower()
refill_water_bottle = input("Do you refill your water bottle? (Y/N) ").lower()

if charge_phone == "y":
    print("You charge your phone.")
    phone_charged = True

if refill_water_bottle == "y":
    print("You refill your water bottle.")
    water_bottle_refilled = True

print("Somewhere in the afternoon...")

print("You feel thirsty.")

if water_bottle_refilled:
    print("You drink from your water bottle and stay hydrated.")
    thirsty = False
else:
    print("You didn't refill your water bottle, so you have no water to drink.")

print("Somewhere in the evening...")

print("It's getting dark and you cannot remember the way back.")

if phone_charged:
    print("You open the Maps app and check for a route back.")
else:
    print("Your phone is out of battery, so you cannot check for an exit route.")
    lost = True

if lost:
    print("You are lost in the mountains.")

if thirsty:
    print("You pass out without water.")

if not lost and not thirsty:
    escape = True

if escape:
    print("You escape in safety.")
