"""
Day 43 – Accumulator Loops

1. Task:
Create a program where:
- values are collected across multiple loop iterations
- the program keeps track of a running total or count
- the final result depends on everything entered during the loop

The goal is to make the program behave more like:
- an accumulator system
instead of:
- a single-input system

2. What I Learnt:
While working on this exercise, I learnt how accumulator variables can be used to keep track of values across multiple loop iterations.

In this program, each task entered by the user is added to a list, and the total number of tasks is tracked using a counter variable. Rather than processing only a single input, the program continuously accumulates information until the user decides to stop entering tasks.

I also learnt that accumulators can be used for different purposes. A variable such as total_tasks can accumulate a running count, while a list can accumulate multiple values entered over time.

This exercise helped me understand how loops and accumulators work together to store and update information as a program runs.

3. Key Concepts:
- accumulator variables
- counters
- lists
- while loops
- sentinel values
- running totals

4. Challenges:
One challenge was keeping the task counter synchronised with the contents of the task list. Whenever a task was added or removed, both the list and the counter needed to be updated correctly.

Another challenge was handling situations where the user attempted to remove a task that did not exist in the list.

5. How I Overcame It:
I overcame these challenges by updating the counter whenever tasks were added or removed and by using an if statement to check whether a task existed in the list before attempting to remove it.

This ensured that the task count remained accurate and prevented errors when invalid task names were entered.

6. Mistakes:
One potential mistake would be forgetting to update total_tasks when adding or removing tasks, causing the counter to become inaccurate.

Another potential mistake would be removing a task without first checking whether it exists in the list, which could cause unexpected behaviour.

A further mistake would be forgetting to request new input inside the loop, resulting in an infinite loop.

7. Improvements:
I would display all remaining tasks after each addition or removal so the user can easily see their current to-do list.

I could also prevent duplicate tasks from being added and allow task names to be entered in a case-insensitive manner.

Another improvement would be to calculate the total number of completed tasks and display a summary when the program ends.
"""

from string import capwords

total_tasks = 0
list_of_tasks = []

print("Welcome to the To Do List App")
print()

print(
    "Instructions:\n"
    "- Add tasks when prompted.\n"
    "- Mark tasks as completed when prompted.\n"
    "- Type 'Quit' at any time to leave the current section."
)

# Add items to the list
print()
print("Add Tasks:")

task_to_add = capwords(input("Enter a task: "))

while task_to_add != "Quit":
    total_tasks += 1
    list_of_tasks.append(task_to_add)

    print(f"Task '{task_to_add}' added.")
    print(f"Total tasks: {total_tasks}.")
    print()

    task_to_add = capwords(input("Enter a task: "))

if total_tasks == 0:
    print("No tasks added!")
else:
    print(f"{total_tasks}", end=" ")

    if total_tasks == 1:
        print("task", end=" ")
    else:
        print("tasks", end=" ")

    print("added.")

    # Remove items from the list
    print()
    print("Tasks Done:")

    task_to_remove = capwords(input("Task completed: "))

    while task_to_remove != "Quit" and total_tasks > 0:
        if task_to_remove not in list_of_tasks:
            print(f"Task '{task_to_remove}' not in task list.")
        else:
            list_of_tasks.remove(task_to_remove)
            total_tasks -= 1

            print(f"Task '{task_to_remove}' completed.")

        if total_tasks == 0:
            print()
            print("All tasks completed!")
            break

        print(f"Total tasks: {total_tasks}.")
        print()

        task_to_remove = capwords(input("Task completed: "))
