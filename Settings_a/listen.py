import speech_recognition as sr
from .talk_a import talk
listener = sr.Recognizer()
def listen():
    status = False
    try:
        with sr.Microphone() as source:
            print("Lo estoy escuchando Señor")
            #talk("Lo estoy escuchando Señor")
            listener.adjust_for_ambient_noise(source, duration=0.05)
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-ES")
            rec = rec.lower()
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            status = True
    except:
        pass  
    return {'text':rec, 'status':status}

green_color = "\033[1;32;40m"
normal_color = "\033[0;37;40m"

name = "alexa"
def audio():
    r = sr.Recognizer()
    status = False

    with sr.Microphone() as source:
        print(f"{green_color}Lo estoy escuchando Señor{normal_color}")
        #talk("Lo estoy escuchando Señor")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        rec = ""

        try:
            rec = r.recognize_google(audio, language='es-ES').lower()
            
            if name in rec:
                rec = rec.replace(f"{name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                status = True

        except:
            pass
    return {'text':rec, 'status':status}