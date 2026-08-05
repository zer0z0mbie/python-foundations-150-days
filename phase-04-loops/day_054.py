"""
Day 54 – Finding Maximum and Minimum Values

1. Task:
Create a program where:
- multiple values are stored in a collection
- the program examines every value
- the highest and lowest values are identified
- the results are displayed to the user

The goal is to make the program behave more like:
- an analysis system
instead of:
- a reporting system

2. What I Learnt:
While working on this exercise, I learnt how to analyse a collection of values by comparing each element to find the highest and lowest values. Instead of using Python's built-in max() and min() functions, I manually implemented the algorithm by assuming that the first value in the list was both the highest and the lowest. As the loop processed each value, these variables were updated whenever a larger or smaller value was found.

This exercise helped me understand the logic behind one of the most common algorithms used when processing collections of data.

3. Key Concepts:
- lists
- for loops
- comparison operators
- accumulator variables
- data analysis

4. Challenges:
No particular challenges were faced during this exercise.

5. How I Overcame It:
Not applicable.

6. Mistakes:
No mistakes were made during this exercise. One potential mistake would be initialising the highest and lowest values incorrectly, which could produce inaccurate results. Another potential mistake would be forgetting to update either the highest or lowest value when a larger or smaller value is found.

7. Improvements:
I would extend the program to calculate the total and average damage dealt. I could also display which attack or round produced the highest and lowest damage values.
"""

damage_dealt = [
    25,
    41,
    18,
    36,
    52,
    29,
]

highest_damage = damage_dealt[0]
lowest_damage = damage_dealt[0]

for damage in damage_dealt:
    if damage > highest_damage:
        highest_damage = damage

    if damage < lowest_damage:
        lowest_damage = damage

print(
    "Battle Summary\n"
    f"Highest damage: {highest_damage}\n"
    f"Lowest damage: {lowest_damage}"
)