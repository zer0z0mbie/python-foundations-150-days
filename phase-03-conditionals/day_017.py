"""
Day 17 – Checking Value Ranges

1) Task:
Create a program that determines whether a value falls within a specific range and produces different outputs depending on the result.

2) What I Learnt:
While completing this exercise, I experimented with different ways of representing ranges. I used the range() function to generate odd numbers from 1 to 9, while using a conventional list for even numbers for comparison and practice purposes.

This helped me understand that ranges can be used to group values and generate different outputs depending on whether a value belongs to a specific range or collection.

3) Key Concepts:
- range() function
- Lists
- Conditional statements
- Membership checking

4) Challenges:
No significant challenges were encountered during this exercise.

5) How I Overcame It:
No specific action was required, as no challenges were encountered.

6) Mistakes:
Although no mistakes were made, I observed that incorrect parameters in the range() function could lead to logical errors. For example, using range(1, 10) without a step value would include both odd and even numbers between 1 and 9. This reinforced the importance of understanding how ranges work and paying close attention to boundaries and parameters.

7) Improvements:
Besides validating user input, another possible improvement would be to determine whether a number is odd or even using the modulo operator (%) instead of predefined ranges and lists. For example, if number % 2 == 0, the number is even; otherwise, it is odd.

However, I intentionally focused on ranges in this exercise to align with the learning objective of the task.
"""

odd_numbers = range(1, 10, 2)
even_numbers = [2, 4, 6, 8, 10]

user_number = int(input("Enter a number from 1 to 10: "))

if user_number in odd_numbers:
    print(f"{user_number} is odd.")
elif user_number in even_numbers:
    print(f"{user_number} is even.")
else:
    print("Number is out of range (1-10 only).")