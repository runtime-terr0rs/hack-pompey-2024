import cv2 as cv
import utils
import math
from cvzone.HandTrackingModule import HandDetector
import time
import rtmidi

hand_cascade = cv.CascadeClassifier('path/to/hand_cascade.xaml')
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

notesActive = 0
numofFingers = 0

cap = cv.VideoCapture(0)
windowName = "Image"

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print(available_ports)

if available_ports:
    midiout.open_port(1)
else:
    midiout.open_virtual_port("HackPompeyLmao")

def main(hands, img):
  global numofFingers
  global notesActive #???

  if hands:
    if len(hands) == 2:

      leftHand, rightHand = utils.handOrientationFinder(hands)
      if leftHand == [] or rightHand == []:
        return
      
      handCoord = rightHand["lmList"][1][1] - 80
      noteNumber = handCoord // 30
      if noteNumber > 12 or noteNumber < 1:
        return

      fingers1 = detector.fingersUp(leftHand)
      fingers2 = detector.fingersUp(rightHand)

      fingers1count = fingers1.count(1)
      fingers2count = fingers2.count(1)

      if numofFingers != fingers1count + fingers2count:
        notesActive = 0

      if fingers1count == 0 or fingers2count == 0:
        return
      
 
      
      numofFingers = fingers1count + fingers2count

      chord = utils.chordHandler(noteNumber, fingers1count, fingers2count)
      if chord == None or chord == []:
        return
      midi = utils.midiConversion(chord)

      print(notesActive, midi)
      if notesActive == midi:
        return
      elif midi != notesActive:
        if notesActive != 0:
          # test = str(notesActive)
          # cv.addText(img,test,(50, 50), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
          for note in notesActive: 
            utils.stopNote(note, midiout)
        for note in midi:
          utils.playNote(note, midiout)
        notesActive = midi
        return
      else:
        print("error")
        return

while True:
  success, img = cap.read()
  hands, img2 = detector.findHands(img, draw = True, flipType = True)

  try:
    main(hands, img2)
  finally:
    pass

  cv.namedWindow(windowName, cv.WINDOW_KEEPRATIO)
  cv.resizeWindow(windowName, 800, 500)
  img = cv.flip(img, 1)
  cv.imshow(windowName, img)
  cv.waitKey(1)
