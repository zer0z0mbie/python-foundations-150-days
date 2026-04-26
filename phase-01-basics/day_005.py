"""
Day 5 – Combining Variables

1) Task:
Create multiple variables and use them together in a single output.

2) What I Learnt:
Although this task did not introduce a new concept, completing it reinforced my knowledge of how values can be used together through printing. Maintaining meaningful variable names is a vital practice, as it keeps the output clear and readable (which is crucial for collaboration and user understanding).

3) Key Concepts:
- Variable assignment
- Output in Python
- print function

4) Challenges:
The main challenge was understanding the syntax of the print statement, as there are different ways to produce output (e.g. using commas, using the + operator, or using f-string formatting).

5) How I Overcame It:
Considering this was a simple task and my variables are straightforward, I used commas to print the values.

6) Mistakes:
At the beginning, I added a space before the dash in "- Favourite food:", which resulted in the following output:

Full name: Matheus Majer  - Favourite food: Lasagna

I corrected this by removing the extra space, as the print function already inserts a space between values when using commas.

7) Improvements:
I believe using f-strings would make the print statement more readable in this case. For example, the same output could be achieved using formatted strings instead of commas.
"""

name = "Matheus"
surname = "Majer"
favourite_food = "Lasagna"

print("Full name:", name, surname, "- Favourite food:", favourite_food)