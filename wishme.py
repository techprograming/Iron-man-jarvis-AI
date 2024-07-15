import datetime
from speak import*

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning Sir!")
    
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Sir!")
    
    else:
        speak("Good Evening Sir!")