"""
Day 48 – Searching Through Collections

1. Task:
Create a program where:
- multiple records are stored in a collection
- the user searches for a specific record
- the program reports whether the record exists

The goal is to make the program behave more like:
- a search system
instead of:
- a data collection system

2. What I Learnt:
While working on this exercise, I learnt that loops can be used to search through collections of data and return the results to the user. In this example, a list stores multiple classic rock albums, and a for loop searches each album until it either finds a match or reaches the end of the collection.

I also learnt that searches can be made case-insensitive by converting both the stored data and the user's input to lowercase before comparing them. Once a matching album is found, the loop stops immediately using the break statement, making the search more efficient. This exercise helped me understand how search systems work and how collections of data can be queried to determine whether specific information exists.

3. Key Concepts:
- lists
- for loops
- linear search
- Boolean variables
- case-insensitive comparisons
- break statement

4. Challenges:
No particular challenges were faced during this exercise.

5. How I Overcame It:
Not applicable.

6. Mistakes:
Although no mistakes were made during this exercise, I acknowledge that a potential mistake would be forgetting to stop the loop after finding the requested item, causing the program to continue searching unnecessarily. Another potential mistake would be performing a case-sensitive comparison, preventing valid matches when the user enters different capitalisation.

7. Improvements:
I would display the position of the album in the collection after it is found. I could also allow partial searches so that entering part of an album title would return matching results. Another improvement would be sorting the collection alphabetically before displaying or searching it.
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

album_search = input("Enter an album > ")
album_found = False

for album in classic_rock_albums:
    if album.lower() == album_search.lower():
        album_found = True
        album_search = album # Preserves list capitalisation
        break

if album_found:
    print(f"'{album_search}' was found in the library.")
else:
    print(f"'{album_search}' was not found in the library.")