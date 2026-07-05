"""
Day 49 – Filtering Collections

1. Task:
Create a program where:
- multiple records are stored in a collection
- the program displays only the records that satisfy a specific condition
- records that do not satisfy the condition are ignored

The goal is to make the program behave more like:
- a filtering system
instead of:
- a search system

2. What I Learnt:
While working on this exercise, I learnt that loops can be used to filter collections of data based on a specific condition. In this example, a collection of classic rock albums is stored in a list. Rather than searching for one specific album, the program examines every album in the collection and stores all albums whose titles begin with the letter entered by the user.

This exercise helped me understand the difference between searching and filtering. A search typically stops once a matching record is found, whereas filtering continues checking every record in the collection to find all matching results.

3. Key Concepts:
- lists
- for loops
- filtering
- conditional statements
- data collections
- accumulator lists

4. Challenges:
No particular challenges were faced during this exercise.

5. How I Overcame It:
Not applicable.

6. Mistakes:
No mistakes were made during this exercise. One potential mistake would be stopping the loop after finding the first matching album. Unlike a search system, a filtering system must continue checking every record in the collection.

Another potential mistake would be displaying matching albums immediately instead of storing them first. Storing the filtered results in a separate list makes it easier to process or display them later.

7. Improvements:
I would make the filtering system more flexible by allowing the user to search for albums containing a word rather than only filtering by the first letter. I could also sort the filtered albums alphabetically before displaying them.

Another improvement would be displaying the total number of matching albums found before printing the filtered results.
"""

classic_rock_albums = [
    "The Dark Side of the Moon",
    "Money for Nothing",
    "Sgt. Pepper's Lonely Hearts Club Band",
    "Led Zeppelin IV",
    "Rumours",
    "Back in Black",
    "Hotel California",
    "Who's Next",
    "A Night at the Opera",
    "Born to Run",
    "The Rise and Fall of Ziggy Stardust and the Spiders from Mars",
    "Exile on Main St.",
    "Abbey Road",
    "Wish You Were Here",
    "Physical Graffiti",
    "Boston",
    "Appetite for Destruction",
    "Toys in the Attic",
    "Paranoid",
    "Damn the Torpedoes",
    "Brothers in Arms",
    "Machine Head",
    "The Wall",
    "Sticky Fingers",
    "Van Halen",
    "Chronicle",
    "Bat Out of Hell",
    "Aqualung",
    "Déjà Vu",
    "Moondance",
    "Harvest",
    "L.A. Woman",
    "At Fillmore East",
    "Goodbye Yellow Brick Road",
    "Crime of the Century",
    "Frampton Comes Alive!",
    "Some Girls",
    "News of the World",
    "Moving Pictures",
    "Synchronicity",
    "Eliminator",
    "Reckless",
    "1984",
    "The Joshua Tree",
    "Full Moon Fever",
    "Born in the U.S.A.",
    "Pyromania",
    "Cosmo's Factory",
    "Bridge over Troubled Water",
    "Agents of Fortune"
]

first_letter = input("Type a letter > ").upper()
albums_filtered = []

for album in classic_rock_albums:
    if first_letter == album[0]:
        albums_filtered.append(album)

if len(albums_filtered) == 0:
    print(f"No albums beginning with {first_letter} in the collection.")
else:
    print(f"Albums beginning with {first_letter}:")

    for album in albums_filtered:
        print(f"- '{album}'")