from enum import IntEnum

class NoteLetter(IntEnum):
	C = 0
	CS = 1
	D = 2
	DS = 3
	E = 4
	F = 5
	FS = 6
	G = 7
	GS = 8
	A = 9
	AS = 10
	B = 11

midiNumA4 = 69
class Note:
	"""
	Represent a musical note with letter and octave
	to derive frequency and MIDI number
	"""
	def __init__(self, note : NoteLetter, octave : int, weirdo : bool = False):
		self.note = note
		self.octave = octave
		self.midiNum = int(self.note) + 12 * (self.octave + 1)
		self.concertAFreq = 432 if weirdo else 440
		self.freq = int(
			round(
				2 ** ((self.midiNum - midiNumA4) / 12) * self.concertAFreq
			)
		)
	def __str__(self) -> str:
		return [
			" C", "C#", " D", "D#", " E", " F",
			"F#", " G", "G#", " A", "A#", " B"
		][
			int(self.note)
		] + format(self.octave, " 2d") + " (" + str(self.freq) + "Hz)"
	def __repr__(self) -> str:
		return self.__str__()

class DuraNote:
	"""
	Represent a musical note with beat duration
	"""
	def __init__(self, noteLetter : NoteLetter, octave : int, duration : int, note : Note = None):
		if note is not None:
			self.note = note
		else:
			self.note = Note(noteLetter, octave)
		self.duration = duration
	def __str__(self) -> str:
		return str(self.note.freq) + ' ' + str(self.duration)
	def __repr__(self) -> str:
		return self.__str__()
	def verbose(self) -> str:
		return "A " + str(self.duration) + "-beat " + str(self.note)

def noteStringToNoteObject(s : str) -> Note:
	"""
	Convert a string with a note letter (with or without a sharp) and octave
	into a Note object (see above definition for more info
	"""
	s = s.lstrip()
	try:
		splitter = list(set(list(s)) & {' ', '-', '_', '.', ','})[0]
	except IndexError as e:
		print(e)
		return None
	#print(s, s.split(splitter))

	noteLetter, octaveStr = s.split(splitter)

	if len(noteLetter) > 1:
		if '#' in noteLetter:
			noteLetter = noteLetter[0] + 'S'
		else:
			print("Error! The Note object uses sharps (#) only, not flats (b).")
			return None

	return Note(NoteLetter[noteLetter], int(octaveStr))

