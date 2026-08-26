"""
Day 55 – Calculating Averages from Collections

1. Task:
Create a program where:
- multiple numerical values are stored in a collection
- the program processes all values
- the total is calculated
- the average is calculated
- the result is displayed

The goal is to make the program behave more like:
- an analytical system
instead of:
- a simple data-processing system

2. What I Learnt:
While working on this exercise, I learnt how an accumulator can be used alongside a loop to calculate a total from a collection of values. In this example, I used the number of values in the list and the accumulated total to calculate the average damage dealt during several attacks.

I also reinforced my understanding of the difference between / and //. Regular division is appropriate when calculating an average because the result can contain a decimal value, while floor division removes the fractional part.

Finally, I learnt that the result can be formatted using .2f when displaying the average, without changing the actual calculated value.

3. Key Concepts:
- accumulator variables
- for loops
- len()
- division
- formatted output

4. Challenges:
One thing I initially found confusing was whether an average should contain decimal values. I initially used floor division (//), but realised that this would remove the fractional part of the result.

5. How I Overcame It:
I compared the results of / and // and understood that / should be used for calculating the average, while formatting can be used separately if I want to control how the result is displayed.

6. Mistakes:
One mistake I initially made was using floor division (//) instead of regular division (/). This caused the average to be rounded down from 33.5 to 33.

7. Improvements:
I would expand the program to calculate other statistics, such as the highest and lowest damage values.

I could also display the total number of hits, total damage, and average damage together as a battle summary.
"""

battle_damage = [
    25,
    41,
    18,
    36,
    52,
    29
]

hits = len(battle_damage)
damage_total = 0

for hit in battle_damage:
    damage_total += hit

average = damage_total / hits

print(f"Average: {average:.1f}")