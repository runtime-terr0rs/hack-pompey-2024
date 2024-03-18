# Hand-Gesture Theremin (2024)

An electronic theremin that reads the user's hand gestures and positions, and sends the appropriate note to a MIDI port.

## Features

* The Screen:
   A screen that shows the user what the software is seeing. It can show the note or chord the user is currently playing too.
* The E-Theremin:
   A theremin that reads how many fingers on both the user's hands to detemine which note is being played. The position of the right hand determines the pitch.

## How to Use

   The theremin accesses the first available camera and detects your own two hands! Two hands must visable for chords to be produced. The vertical position of the right hand, more specifically, the lower palm, represents the note (or pitch) it will start with. The fingers on the right hand represent how many notes will be played within the chord. The fingers on the left hand represent which scale the chord will play from. Like a theremin, the notes start from low to high, the lowest note being C and the highest note being B.

### Left Hand

* 1 finger up: Chromatic Scale
* 2 fingers up: Major Scale
* 3 fingers up: Minor Scale

### Right Hand

* 1 finger up: 1st note
* 2 fingers up: 1st and 3rd note
* 3 fingers up: 1st, 3rd, and 5th note
* 4 fingers up: 1st, 3rd, 5th, and 7th note
* 5 fingers up: 1st, 3rd, 5th, 7th, and 9th note

#### Music Theory

Generally, a chord is form from taking every odd number of note from a scale. According to [Wikipedia](https://en.wikipedia.org/wiki/Scale_(music)), A musical scale is any set of musical notes ordered by fundamental frequency or pitch. A scale ordered by increasing pitch is an ascending scale, and a scale ordered by decreasing pitch is a descending scale.

The rootnote, the starting note, is selected using the vertical position of your right hand. Therefore, to make a maj7 chord, two fingers need to be up on the left hand, and four on the right hand.

#### MIDI

A MIDI port is not necessary for this application to work, however, no sound will be produced. This application turns the chord into MIDI data and sends this data into a port. MIDI Ports can be detected by Digtial Audio Workstations such as [Ableton](https://www.ableton.com/en/), or [CakeWalk](https://www.cakewalk.com/), these MIDI signals can then be turned into sounds using these applications.

We use [loopMIDI by Tobias Erichsen](https://www.tobias-erichsen.de/software/loopmidi.html) to create the MIDI. The MIDI ports name has to be "HGTport", if it is anything else, the application will not send MIDI signals.

## Design & Implementation Rationale

   This was made by offloading a lot of the heavy work onto pre-existing libraries, and we also wrote out some difficult sections of code ahead of the competition. This was to give us ample time during the competition to actually finish the project. We didn't want to overengineer the project by using version control or branches where it just wasn't needed, given the scope of the project. We used LiveShare (a VSCode extension) to have us all working on the project on the day. We modularised the code by having all the utility functions in one file and having the main executable code in another.

## Future Work

* Velocity - To control the volume of the notes, the vertical position of the left hand could control the velocity parameter on the MIDI signals.
* UI - Show on the camera output where each note is.

## Installation

This was written in [Python 3.8.10](https://www.python.org/downloads/release/python-3810/).

* Clone the repository with:

   ```bash
   git clone https://github.com/runtime-terr0rs/hack-pompey-2024.git
   ```

* To install the dependencies

   ```bash
   pip install python-rtmidi mingus opencv-python cvzone mediapipe
   ```

* After using "cd" to get inside the repo, run the application.

   ```bash
   python main.py
   ```

Alternatively, download and run the executable in the release section.

### MIDI Ports

We use [loopMIDI by Tobias Erichsen](https://www.tobias-erichsen.de/software/loopmidi.html) to create the MIDI. The MIDI ports name has to be "HGTport", if it is anything else, the application will not send MIDI signals. These MIDI

## Built With

* Visual Studio Code
* Python
* MIDI
* cvzone
* cv2
* Mingus
* RtMIDI
* cx_Freeze

### Sources

* [RtMIDI](https://pypi.org/project/python-rtmidi/)
* [Mingus](https://github.com/bspaans/python-mingus)
* [cvzone](https://github.com/cvzone/cvzone?tab=readme-ov-file#hand-tracking-module)

## Authors

* Ethan Egerton ([@ethan-egerton](https://github.com/ethan-egerton))
* Oliver Goggins ([@OGoggins](https://github.com/OGoggins))
* Jack Ramsay ([@jramsay21](https://github.com/jramsay21))
