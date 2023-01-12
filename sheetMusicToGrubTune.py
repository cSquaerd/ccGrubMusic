#!/usr/bin/python
from Music import Note, DuraNote, noteStringToNoteObject 
import sys

"""
To use this script, either pipe the contents of a tune to it,
or give it the name of a file with the tune written within.

The tune notation used is as follows:

[Note Letter] [Octave] [Duration (bpm)],

Where Note Letters go from C to B, with sharps indicated with a #;
ex. C#, F#, G, A

A sequence of note-octave-duration triplets, separated by commas,
with or without newlines after the commas, makes up a tune
ex 1.
C 4 3, F 4 3, B 4 3, A 4 1, G 4 1, F 4 1

ex 2.
G 5 3,
C 5 3,
E 5 3,
D 5 1,
C 5 1,
B 4 1
"""

if __name__ == "__main__":
	verbose = False
	if len(sys.argv) < 2:
		raw = sys.stdin.read().split(',')
	else:
		try:
			with open(sys.argv[1], 'r') as inFile:
				raw = inFile.read().split(',')
		except FileNotFoundError as fnfe:
			print(fnfe)
			exit(-1)

		for flag in sys.argv[2:]:
			if 'V' in flag.upper():
				verbose = True
				break
	
	splitter = list(set(list(raw[0])) & {' ', '-', '_', '.'})[0]
	#print(raw)
	mild = [el.split(splitter)[-3:] for el in raw]
	#print(mild)
	noteStrings = [el[0] + splitter + el[1] for el in mild]
	duras = [int(el[2]) for el in mild]

	#print(noteStrings)
	#print(duras)

	notes = list(map(noteStringToNoteObject, noteStrings))
	#print(notes)
	
	duraNotes = []
	for i in range(len(notes)):
		duraNotes.append(DuraNote(None, 0, duras[i], notes[i]))
	#print(duraNotes)
	if verbose:
		print()
		for dn in duraNotes:
			print(dn.verbose())
		print()

	print("Here is your tune string:\n")
	print(' '.join(map(str, duraNotes)))
	print("\nPlease choose a tempo (in beats per minute) and write that number first,")
	print("followed by the tune string, into your /etc/default/grub file,")
	print("or other grub config generation file.")
