import wave
import pyaudio
import os, copy
from scipy.io.wavfile import write
from scipy.io.wavfile import read
import numpy as np

INT16_FAC = (2**15)-1


def play(y, fs):
	# play the array y as a sound using fs as the sampling rate
	
	x = copy.deepcopy(y)	#just deepcopying to modify signal to play and to not change original array
	
	x *= INT16_FAC	#scaling floating point -1 to 1 range signal to int16 range
	x = np.int16(x)	#converting to int16 type
	
	CHUNK = 1024
	write('temp_file.wav', fs, x)
	wf = wave.open('temp_file.wav', 'rb')
	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)

	data = wf.readframes(CHUNK)

	while data is not '':
		stream.write(data)
		data = wf.readframes(CHUNK)

	stream.stop_stream()
	stream.close()

	p.terminate()
	os.remove(os.getcwd()+'/temp_file.wav')
	
def wavread(filename):
	# read a sound file and return an array with the sound and the sampling rate
	
	(fs, x) = read(filename)
	
	#scaling down and converting audio into floating point number between range -1 to 1
	x = np.float32(x)/INT16_FAC
	
	return fs, x
      
def wavwrite(y, fs, filename):
	# write a sound file from an array with the sound and the sampling rate
	
	x = copy.deepcopy(y)	#just deepcopying to modify signal to write and to not change original array
	
	x *= INT16_FAC	#scaling floating point -1 to 1 range signal to int16 range
	x = np.int16(x)	#converting to int16 type

	write(filename, fs, x)