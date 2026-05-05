"""
Day 14 – Multiple Conditions (More Than Two Outcomes)

1) Task:
Create a program that takes user input and produces more than two possible outcomes based on different conditions.

2) What I Learnt:
Upon completing this exercise, I learnt that conditional logic can be expanded from if/else to if/elif/else in order to handle multiple scenarios and produce more specific outputs.

This type of logic is essential for building programs that reflect real-world situations, which often go beyond simple yes/no decisions. Compared to Day 13, I also became more aware of how multiple conditions can increase the risk of logical errors if they are not carefully structured.

3) Key Concepts:
- Conditions
- If / elif / else statements
- Logical thinking

4) Challenges:
No significant challenges were encountered during this exercise.

5) How I Overcame It:
No specific action was required, as no challenges were encountered.

6) Mistakes:
No mistakes were made during this exercise.

7) Improvements:
A possible improvement would be to handle invalid inputs (e.g. non-numeric values), which would require additional validation logic.
"""

favourite_number = int(input("What's your favourite number? "))

if favourite_number < 100:
    print("Your favourite number is less than 100")
elif favourite_number == 100:
    print("Your favourite number is 100")
else:
    print("Your favourite number is greater than 100")