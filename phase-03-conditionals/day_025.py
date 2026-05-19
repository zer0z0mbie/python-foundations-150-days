"""
Day 25 – Tracking Program State

1) Task:
Create a program where:
- the user’s choices change the state of the program
- later decisions depend on earlier outcomes
- the program keeps track of progression through multiple stages

The goal is to make the program behave more like:
- a state-driven system
instead of:
- isolated conditional branches

2) What I Learnt:
When working on this challenge, I learnt that user input can lead to multiple stages, which change according to the user's choices. I also learnt that conditionals and Boolean variables can be used to track the state of a procedural program.

3) Key Concepts:
- conditionals
- state change
- procedural flow
- Boolean variables

4) Challenges:
I was initially unsure how to design the states and how to make the program remember previous choices.

5) How I Overcame It:
Since this is a relatively small program, I used conditional checks and Boolean variables to track the program state.

6) Mistakes:
No mistakes made.

7) Improvements:
I would improve the input validation and create a clearer distinction between supported and unsupported vehicle brands.
"""

# State variables
is_motorcycle = False
is_car = False
is_bmw_motorcycle = False
is_kawasaki_motorcycle = False
is_toyota_car = False
is_volkswagen_car = False
is_other_brand = False

print("\nWelcome to Robot Repair Vehicle Wash\n")
print(
    "We wash:\n"
    "* Motorcycles (M)\n"
    "* Cars (C)\n"
)

vehicle = input("What's your vehicle type? (M/C) ").lower()

# Vehicle type
if vehicle == "m":
    is_motorcycle = True
elif vehicle == "c":
    is_car = True
else:
    print("Sorry, but we do not wash this type of vehicle!")


if is_motorcycle or is_car:
    print("We are happy to wash your", end=" ")

    if is_motorcycle:
        print(
            "motorcycle!\n"
            "\nWe charge per brand:\n"
            "* Kawasaki (K)\n"
            "* BMW (B)\n"
            "* Other (O)\n"
        )

        brand = input("What's your motorcycle brand? ").lower()

        # Motorcycle brand
        if brand == "k":
            is_kawasaki_motorcycle = True
        elif brand == "b":
            is_bmw_motorcycle = True
        elif brand != "k" and brand != "b":
            is_other_brand = True
    else:
        print(
            "car!\n"
            "\nWe charge per brand:\n"
            "* Toyota (T)\n"
            "* Volkswagen (V)\n"
            "* Other (O)\n"
        )

        brand = input("What's your car brand? ").lower()

        # Car brand
        if brand == "t":
            is_toyota_car = True
        elif brand == "v":
            is_volkswagen_car = True
        elif brand != "t" and brand != "v":
            is_other_brand = True

if is_kawasaki_motorcycle:
    print("Kawasaki motorcycle wash price: £45.00")

if is_bmw_motorcycle:
    print("BMW motorcycle wash price: £30.00")

if is_toyota_car:
    print("Toyota car wash price: £50.00")

if is_volkswagen_car:
    print("Volkswagen car wash price: £35.00")

if is_other_brand:
    print("Price per quotation only.")