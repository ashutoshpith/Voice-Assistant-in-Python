import Main as m
import os

def open_application(input): 
  
    if "chrome" in input: 
        m.assistant_speaks("Google Chrome") 
        os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
        return
  
    elif "firefox" in input or "mozilla" in input: 
        m.assistant_speaks("Opening Mozilla Firefox") 
        os.startfile(r'C:\Program Files\Mozilla Firefox\\firefox.exe') 
        return
  
    elif "word" in input: 
        m.assistant_speaks("Opening Microsoft Word") 
        os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk') 
        return
  
    elif "excel" in input: 
        m.assistant_speaks("Opening Microsoft Excel") 
        os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk') 
        return
  
    else: 
  
        m.assistant_speaks("Application not available") 
        return