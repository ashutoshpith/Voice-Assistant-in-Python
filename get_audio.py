import speech_recognition as sr 
import assistant_speaks as ass

def get_audio(): 

	rObject = sr.Recognizer() 
	audio = '' 

	with sr.Microphone() as source: 
		print("Please Ask What You Need") 
		
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 2) 
	print("Please Stop.") # limit 5 secs 

	try: 

		text = rObject.recognize_google(audio, language ='en-US') 
		print("You : ", text) 
		return text 

	except: 

		ass.assistant_speaks("Could not understand your audio, PLease try again !") 
		return 0

