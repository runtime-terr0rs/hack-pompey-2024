# Hand-Gesture Theremin (2024)

## Authors
   Ethan Egerton (@ethan-egerton), Oliver Goggins (@OGoggins), Jack Ramsay (@jramsay21)

## Contents
   An electronic theremin that reads the user's hand gestures and positions, and sends the appropriate note to a MIDI port.

## Features
   * The Screen:
      A screen that shows the user what the software is seeing. It can show the note or chord the user is currently playing too. 
   * The E-Theremin:
      A theremin that reads how many fingers on both the user's hands to detemine which note is being played. The position of the right hand determines the pitch.

## Design & Implementation Rationale
   This was made by offloading a lot of the heavy work onto pre-existing libraries, and we also wrote out some difficult sections of code ahead of the competition. This was to give us ample time during the competition to actually finish the project. We didn't want to overengineer the project by using version control or branches where it just wasn't needed, given the scope of the project. We used LiveShare (a VSCode extension) to have us all working on the project on the day. We modularised the code by having all the utility functions in one file and having the main executable code in another.
   

## Future Work
   * 
   * 
   * 

## Installation & Use
1. Clone the repository with:
   ```bash
   git clone [Enter URL here]
   ```
2. Go into the locally cloned repo with:
   ```bash
   cd 
   ```
3. 

## Built With
   * Visual Studio Code
   * Python
   * MIDI
   * cvzone
   * cv2
   * Mingus
   * RtMIDI
   * cx_Freeze

## Sources
   * RtMIDI - https://pypi.org/project/python-rtmidi/
   * Mingus - https://github.com/bspaans/python-mingus
   * cvzone - https://github.com/cvzone/cvzone?tab=readme-ov-file#hand-tracking-module
   