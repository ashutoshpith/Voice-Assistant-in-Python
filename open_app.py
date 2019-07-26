import assistant_speaks as ass
import os

def open_application(input): 
  
    if "chrome" in input: 
        ass.assistant_speaks("Google Chrome") 
        os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
        return
  
    elif "firefox" in input or "mozilla" in input: 
        ass.assistant_speaks("Opening Mozilla Firefox") 
        os.startfile(r'C:\Program Files\Firefox Developer Edition\firefox.exe') 
        return
  
    elif "code" in input: 
        ass.assistant_speaks("Opening Microsoft visual Code") 
        os.startfile(r'C:\Users\ashut\AppData\Local\Programs\Microsoft VS Code\Code.exe') 
        return
  
    elif "hatch" in input: 
        ass.assistant_speaks("Opening Hatch File") 
        os.startfile(r'H:') 
        return
  
    else: 
  
        ass.assistant_speaks("Application not available") 
        return