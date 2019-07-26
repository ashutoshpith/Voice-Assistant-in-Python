# importing speech recognition package from google api 
import speech_recognition as sr 
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import text_process as tp
import date_access as da

num = 1
def assistant_speaks(output): 
	global num 

	# num to rename every audio file 
	# with different name to remove ambiguity 
	num += 1
	print("Goku : ", output) 

	toSpeak = gTTS(text = output, lang ='en', slow = False) 
	# saving the audio file given by google text to speech 
	file = str(num)+".mp3" 
	toSpeak.save(file) 
	
	# playsound package is used to play the same file. 
	playsound.playsound(file, True) 
	os.remove(file)



def get_audio(): 

	rObject = sr.Recognizer() 
	audio = '' 

	with sr.Microphone() as source: 
		print("Please Ask What You Need") 
		
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5) 
	print("Please Stop.") # limit 5 secs 

	try: 

		text = rObject.recognize_google(audio, language ='en-US') 
		print("You : ", text) 
		return text 

	except: 

		assistant_speaks("Could not understand your audio, PLease try again !") 
		return 0


# Driver Code 
if __name__ == "__main__": 
	assistant_speaks("Hello, Ashutosh This is Goku For You...") 
	n ="Ashutosh"
	# name = get_audio()
	assistant_speaks("Today's date is "+da.get_date()) 
	
	while(1): 


		assistant_speaks("TELL me Sir What for today? Anything Special For me") 		
		text = get_audio().lower() 

		if text == '': 
			continue

		if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
			assistant_speaks("Ok bye, "+ n+'.') 
			break

		# calling process text to process the query 
		tp.process_speak(text)
	
		 
