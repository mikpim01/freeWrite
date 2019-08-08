# freeWrite

An application for the collection and archival of personal logs. The application should encourage daily logging and review. The application should discourage deletion or revision.

## Use

Run this prototype on linux systems with:
```bash
[user@host ../freeWrite/] $ python freeWrite.py
```
Not sure about other systems, I don't use them enough to know. There is nothing that should cause problems for running on other systems. Just make sure that python's dbm module has a decent backend, so it doesn't default to the dumb one.

## Methodology

To encourage daily logging and review:

- [x] Daily Goals
- [x] Calendar Navigation
- [ ] Entry Tags Navigation
- [ ] Log Statistics
- [ ] Generated Writing Prompts

To discourage deletion or revision:

- [x] "Micro-logger" interface
- [x] Logging prohibitted on past or future dates
- [ ] Logging profiles frontend to database selection
- [ ] Alert dialog at Deletion/Revision attempts

## Implementation

Python3.7 with modules dbm and PyQt5. PyQt5 layouts built and generated using QtBuilder. Composed with the help of KDevelop. 
