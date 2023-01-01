import pyttsx3
engine = pyttsx3.init()
def voice(): 
    engine.setProperty('rate', 178)
    engine.setProperty('volume', 1.5)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    return voices