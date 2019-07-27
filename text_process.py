import web_access as wa
import wolframalpha
import speech_recognition as sr 
import playsound 
from open_app import open_application
from gtts import gTTS 
import os 
import assistant_speaks as ass
import date_access as da
import get_audio as ga

def process_speak(text):
    # print(text)
    try: 
        if 'search' in text or 'play' in text: 
            wa.find_web(text) 
            return
            
        elif 'todays date' in text or 'date' in text:
            ass.assistant_speaks(da.get_date())
            return
  
        elif "who are you" in text or "define yourself" in text: 
            speak = "Hello, I am Goku Sir" 
            ass.assistant_speaks(speak) 
            return
  
        elif "who made you" in text or "created you" in text: 
            speak = "You Sir Ashutosh."
            ass.assistant_speaks(speak) 
            return
  
        elif "ashutoshpith" in text:
            speak = """It's Your Website Sir"""
            ass.assistant_speaks(speak) 
            return
  
        elif "calculate" in text.lower(): 
              
            # write your wolframalpha app_id here 
            app_id = "WOLFRAMALPHA_APP_ID" 
            client = wolframalpha.Client(app_id) 
  
            indx = text.lower().split().index('calculate') 
            query = text.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            ass.assistant_speaks("The answer is " + answer) 
            return
  
        elif 'open' in text: 
            open_application(text.lower())  
            return
  
        else: 
  
            ass.assistant_speaks("I can search the web for you, Do you want to continue?") 
            ans = ga.get_audio() 
            if 'yes' in str(ans) or 'yeah' in str(ans): 
                wa.find_web(text) 
            else: 
                return
    except : 
  
        ass.assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
        ans = ga.get_audio() 
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            wa.find_web(text) 
