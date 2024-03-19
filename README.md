# Hand-Gesture Theremin (2024)

An electronic theremin that reads the user's hand gestures and positions from camera data and sends a musical chord to a Musical Instrument Digital Interface (MIDI) port.

## Features

* The Screen:
   A screen that shows the user what the software is seeing, and a terminal that displays the note or chord the user is currently playing.
* The E-Theremin:
   A theremin reads how many fingers are on the user's hands to determine which chord should be played. The position of the right hand determines the pitch of the chord's root note.

## How to Use

The theremin accesses the first available camera and detects your own two hands! Two hands must be visible for chords to be produced. The vertical position of the right hand, more specifically, the lower palm, represents the note (or pitch) it will start with. The fingers on the right hand represent how many notes will be played within the chord. The fingers on the left hand represent which scale the chord will play from. Like a theremin, the notes start from low to high, the lowest note being C and the highest note being B.

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

Generally, a chord is formed by taking every odd number of notes from a scale. According to [Wikipedia](https://en.wikipedia.org/wiki/Scale_(music)), a musical scale is any set of musical notes ordered by fundamental frequency or pitch. An ascending scale is ordered by increasing pitch, and a descending scale is ordered by decreasing pitch. Scales always start with a root note, the starting note, a C Major Scale would start with the note "C" and a G# Minor Scale would start with a "G#". The root note is selected using the vertical position of your right hand. Therefore, to make a maj7 chord, two fingers on the left hand need to be up and four on the right hand. 
<p align="center">
   <img src="https://github.com/runtime-terr0rs/hack-pompey-2024/blob/main/assets/maj7chord.png" alt="Image of two hands up, the left hand with the index and thumb raised, the right with all fingers except the ring finger raised.">
</p>
The three scales used in this application are Chromatic, Major, and Minor. The Chromatic scale contains all 12 notes (A through G#). The Major scale is known as the "Happy Scale," and the Minor scale is known as the "Sad Scale." 

#### MIDI

This application does not need a MIDI port; however, no sound will be produced. This application turns the chord into MIDI data and sends this data to a port. MIDI Ports can be detected by Digital Audio Workstations such as [Ableton](https://www.ableton.com/en/) or [CakeWalk](https://www.cakewalk.com/). These MIDI signals can then be turned into sounds using these applications.

We use [loopMIDI by Tobias Erichsen](https://www.tobias-erichsen.de/software/loopmidi.html) to create the MIDI port. The MIDI port's name has to be "HGTport"; if it is anything else, the application will not send MIDI signals.

## Design & Implementation Rationale

This was made by offloading a lot of the heavy work onto pre-existing libraries, and we also wrote out some problematic sections of code ahead of the competition. This gave us ample time to finish the project during the competition. Given the project's scope, we didn't want to overengineer it by using version control or branches that weren't needed. We used LiveShare (a VSCode extension) to have all of us work on the project during the day. We modularised the code by having all the utility functions in one file and having the main executable code in another.

## Future Work

* Velocity - The left hand's vertical position could control the velocity parameter on the MIDI signals to control the notes' volume.
* UI - Show where each note is on the camera output window.

## Installation

This was written in [Python 3.8.10](https://www.python.org/downloads/release/python-3810/).

* Clone the repository with:

   ```bash
   git clone https://github.com/runtime-terr0rs/hack-pompey-2024.git
   ```

* To install the dependencies:

   ```bash
   pip install python-rtmidi mingus opencv-python cvzone mediapipe
   ```

* After using "cd" to get inside the repo, run the application using:

   ```bash
   python main.py
   ```

### MIDI Ports

We use [loopMIDI by Tobias Erichsen](https://www.tobias-erichsen.de/software/loopmidi.html) to create the MIDI port. The MIDI port's name has to be "HGTport"; if it is anything else, the application will not send MIDI signals. 

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
