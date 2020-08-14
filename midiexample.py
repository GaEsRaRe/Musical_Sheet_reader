############################################################################
# A sample program to create a single-track MIDI file, add a note,
# and write to disk.
############################################################################

#Import the library
#from midiutil.MidiFile import MIDIFile


import sys
sys.path.append('MIDI/src/midiutil')

from MidiFile3 import MIDIFile

"""
note_defs = {
     -4 : ("g5", 79),
     -3 : ("f5", 77),
     -2 : ("e5", 76),
     -1 : ("d5", 74),
      0 : ("c5", 72),
      
      1 : ("b4", 71),
      2 : ("a4", 69),
      3 : ("g4", 67),
      4 : ("f4", 65),
      5 : ("e4", 64),
      6 : ("d4", 62),
      7 : ("c4", 60),
      
      8 : ("b3", 59),
      9 : ("a3", 57),
     10 : ("g3", 55),
     11 : ("f3", 53),
     12 : ("e3", 52),
     13 : ("d3", 50),
     14 : ("c3", 48),
     
     15 : ("b2", 47),
     16 : ("a2", 45),
     17 : ("f2", 53),
}
"""
# Create the MIDIFile Object
MyMIDI = MIDIFile(1)

# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
def newNote(time, duration, pitch):
    track = 0
    MyMIDI.addTrackName(track,time,"Sample Track")
    MyMIDI.addTempo(track,time, 120)
    channel = 0
    volume = 100
    MyMIDI.addNote(track,channel,pitch,time,duration,volume)

newNote(0,1,60)#do
newNote(1,1,60)#do
newNote(2,1,62)#re
newNote(3,1,60)#do
newNote(4,1,65)#fa
newNote(5,1,64)#mi

newNote(7,1,60)
newNote(8,1,60)
newNote(9,1,62)
newNote(10,1,60)
newNote(11,1,67)
newNote(12,1,65)

newNote(14,1,60)
newNote(15,1,60)
newNote(16,1,72)
newNote(17,1,69)
newNote(18,1,65)
newNote(19,1,64)
newNote(20,1,62)


# And write it to disk.
binfile = open("output2.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

