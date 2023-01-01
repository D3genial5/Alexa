import datetime
from .talk_a import talk

def greetings():
    s = ['Buenos días', 'Buenas tardes', 'Buenas noches']
    now = datetime.datetime.now()
    if now.hour >= 7 and now.hour <= 12:
        print(s[0]+" Señor Andre")
        talk(s[0]+" Señor Andre")
    elif now.hour > 12 and now.hour <= 18:
        print(s[1]+" Señor Andre")
        talk(s[1]+" Señor Andre")
    else:
        print(s[2]+" Señor Andre")
        talk(s[2]+"Señor Andre")

def greetings2():
    s = ['Buenos días', 'Buenas tardes', 'Buenas noches']
    now = datetime.datetime.now()
    if now.hour >= 7 and now.hour <= 12:
        return s[0]

    elif now.hour > 12 and now.hour <= 18:
        return s[1]

    else:
        return s[2]
