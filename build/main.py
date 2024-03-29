from cv2 import CascadeClassifier, VideoCapture, namedWindow, resizeWindow, flip, imshow, waitKey, WINDOW_KEEPRATIO, getWindowProperty, WND_PROP_VISIBLE
from cvzone.HandTrackingModule import HandDetector
from rtmidi import MidiOut
import utils

# Setup hand model
hand_cascade = CascadeClassifier('path/to/hand_cascade.xaml')
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# Initiate camera capture
cap = VideoCapture(0)
windowName = "Hand-Gesture Theremin"

# MIDI port selection
midiout = MidiOut()
available_ports = midiout.get_ports()

try:
  if available_ports:
    midiout.open_port(1)
  else:
    midiout.open_virtual_port("HGTport")
except:
  print("MIDI device not found")
  pass

# Global variables
notesActive = 0
numofFingers = 0


def main(hands):
  global numofFingers
  global notesActive 

  if len(hands) != 2 or not hands:
    return

  leftHand, rightHand = utils.handOrientationFinder(hands)
  if leftHand == [] or rightHand == []:
    return
  
  handCoord = rightHand["lmList"][1][1] - 80
  noteNumber = handCoord // 30
  
  if noteNumber > 12 or noteNumber < 1:
    return

  fingers1count = detector.fingersUp(leftHand).count(1)
  fingers2count = detector.fingersUp(rightHand).count(1)

  if numofFingers != fingers1count + fingers2count:
    notesActive = 0

  if fingers1count == 0 or fingers2count == 0:
    return
  
  numofFingers = fingers1count + fingers2count

  chord = utils.chordHandler(noteNumber, fingers1count, fingers2count)
  if chord == None or chord == []:
    return
  
  print(chord)
  midi = utils.midiConversion(chord)

  if notesActive == midi:
    return
  elif midi != notesActive:
    if notesActive != 0:
      for note in notesActive: 
        utils.stopNote(note, midiout)
    for note in midi:
      utils.playNote(note, midiout)
    notesActive = midi
    return
  else:
    return
  
  
# Main program loop
while True:
  success, img = cap.read()
  hands, img2 = detector.findHands(img, draw = True, flipType = True)

  try:
    main(hands)
  finally:
    pass
  
  namedWindow(windowName, WINDOW_KEEPRATIO)
  resizeWindow(windowName, 800, 500)
  img = flip(img, 1)
  imshow(windowName, img)
  waitKey(1)

  if getWindowProperty(windowName, WND_PROP_VISIBLE) < 1:
    break
  if waitKey(1) & 0xFF == 27:  # 27 is the ESC key
    break
