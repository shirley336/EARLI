import sys
import subprocess, os

from pydub import AudioSegment
from pydub.silence import split_on_silence

#Take in the audio that need to sliced
sound_file = AudioSegment.from_wav("ABC.wav")
#Divides the audio into chunks depending silence threshold and silence lengths
alphabet = split_on_silence(sound_file, min_silence_len=500, silence_thresh=-40)

#List of letters in the alphabet
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "empty", "n", "o", "p", 
			"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i, letter in enumerate(alphabet):
	#Format out file name
	out_file = "letter_{0}.wav".format(letters[i])
	#Print which file is outputing
	print ("exporting{0}".format(out_file))
	#Export the wav files
	letter.export(out_file, format="wav")