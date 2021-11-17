# EncounterManager
Gloomhaven encounter manager

Python command line application that manages a road and city encounter deck stored in individual text files.

## Details
To start run
`python em.py`

### Interface
Road Encounter:
 *        dr: Draw.
 *       sr: Shuffle.
 *        ar: Add an road encounter.
City Encounter:
*         dc: Draw.
*         sc: Shuffle.
*         ac: Add an city encounter.
Personal Goals:
*         dg: Draw to goals, select one (or none).
*         sg: Shuffle.
Press q to quit.

### Storage
The city and road encounter and the personal goal decks are stored in the respective txt file. Each txt file contains a simple list representing the order of the encounter.

Every action that changes a deck is also logged in log.txt.
