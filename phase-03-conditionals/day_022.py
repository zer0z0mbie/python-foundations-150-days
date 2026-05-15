"""
Day 22 – Prioritising Conditions

1) Task:
Create a program where:
- multiple conditions exist
- some outcomes must take priority over others
- the order of the conditions changes the program behaviour

The goal is to understand that:
- condition order matters
and that poorly ordered logic can produce:
- incorrect or unreachable outcomes

2) What I Learnt:
While doing this exercise, I learnt that it is crucial to think about the logical ordering to ensure that the conditional checks are performed in the correct order, as priority matters.

The program created to illustrate the concept of prioritising conditions is a roller coaster theme park application that verifies both the customer's age and height. Based on the answers, the program prints the types of rides the customer can enjoy. In real-world scenarios, if the wrong order is used, it could lead to serious issues such as young customers being accepted onto adult rides, which could result in severe safety problems.

3) Key Concepts:
- overlapping conditions
- multiple outcomes
- conditional priority
- nested conditions

4) Challenges:
I struggled slightly with deciding the correct order of the conditions, as I was unsure whether I should start checking the highest age range (18 or older) or the lowest age range (under 12).

5) How I Overcame It:
I ended up starting with the highest age range (18 or older) because most customers in this theme park are adults, meaning fewer conditional checks are performed on average. Although this optimisation is not very significant in a small program, the same reasoning could apply to larger systems where data should be processed more efficiently.

6) Mistakes:
I made a mistake in the elif 15 <= age < 18 statement because I forgot to add the <= operator and instead wrote the statement as elif 15 < age < 18, which caused a logical error. As a result, users aged 15 were incorrectly placed into the wrong range.

7) Improvements:
I would add a way for the program to continue running until the customer provides valid data, and I would also add input validation.
"""

print()
print(
    "Welcome to the Land of the Coasters,\n"
    "the home of the fastest coasters in the world,\n"
    "or perhaps in the whole galaxy!\n"
)
print(
    "Please answer our short questionnaire,\n"
    "so we can put you give you the best ride experience\n"
)

age = int(input("How old are you? "))

if age >= 18:
    height = float(input("How tall are you (in metres)? "))
    if height < 1.75:
        print("You can ride either E.T. Experience or the Mission Apollo.")
    else:
        print("You can ride Life on Mars.")
elif 15 <= age < 18:
    print("You can ride either the Sputnik or the E.T. Experience.")
elif 12 <= age < 15:
    print("You can ride the Sputnik.")
else:
    print("Sorry, minimum age is 12.")





















