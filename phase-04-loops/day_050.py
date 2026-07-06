"""
Day 50 – Sorting Collections

1. Task:
Create a program where:
- multiple records are stored in a collection
- the records are organised into a defined order
- the sorted collection is displayed to the user

The goal is to make the program behave more like:
- a data organisation system
instead of:
- a filtering system

2. What I Learnt:
While working on this exercise, I learnt how collections can be organised by sorting them into a specific order. I also learnt that the `sorted()` function creates a new sorted list without modifying the original collection. This allowed me to display both the original and sorted lists for comparison. This exercise reinforced that sorting is one of the most common operations performed on collections to make information easier to browse and read.

3. Key Concepts:
- lists
- sorting
- `sorted()` function
- for loops
- collections

4. Challenges:
No particular challenges were faced during this exercise.

5. How I Overcame It:
Not applicable.

6. Mistakes:
No mistakes were made during this exercise, however, one potential mistake would be assuming that `sorted()` modifies the original list when it actually returns a new sorted list.

7. Improvements:
I would allow the user to choose between ascending and descending order. I could also sort the collection using different criteria, such as release year or title length.
"""

ps5_games = [
    "Elden Ring",
    "Marvel's Spider-Man 2",
    "Demon's Souls",
    "God of War Ragnarök",
    "Returnal",
    "Ratchet & Clank: Rift Apart",
    "Baldur's Gate 3",
    "Final Fantasy VII Rebirth",
    "Ghost of Tsushima: Director's Cut",
    "Horizon Forbidden West"
]

ps5_games_sorted = sorted(ps5_games)

print("PS5 games before sorting:")

for game in ps5_games:
    print(f"- '{game}'")

print()

print("PS5 games after sorting:")

for game in ps5_games_sorted:
    print(f"- '{game}'")