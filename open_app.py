def open_application(input): 
  
    if "chrome" in input: 
        assistant_speaks("Google Chrome") 
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
        return
  
    elif "firefox" in input or "mozilla" in input: 
        assistant_speaks("Opening Mozilla Firefox") 
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe') 
        return
  
    elif "word" in input: 
        assistant_speaks("Opening Microsoft Word") 
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk') 
        return
  
    elif "excel" in input: 
        assistant_speaks("Opening Microsoft Excel") 
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk') 
        return
  
    else: 
  
        assistant_speaks("Application not available") 
        return