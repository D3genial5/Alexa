from datetime import datetime, date, timedelta

day_en = [line.rstrip('\n') for line in open('A:\Alexa\Alexa\day\day_en.txt')]
day_es = [line.rstrip('\n') for line in open('A:\Alexa\Alexa\day\day_es.txt')]

def iterateDays(now):
    for i in range(len(day_en)):
        if day_en[i] in now:
            now = now.replace(day_en[i], day_es[i])
    return now

def getDay():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return iterateDays(now)

def getDaysAgo(rec):
    value =""
    if 'Ayer' in rec:
        days = 1
        value = 'Ayer'
    elif 'Antes de ayer' in rec:
        days = 2
        value = 'Antes de ayer'
    else:
        rec = rec.replace(",","")
        rec = rec.split()
        days = 0

        for i in range(len(rec)):
            try:
                days = float(rec[i])
                break
            except:
                pass
    
    if days != 0:
        try:
            now = date.today() - timedelta(days=days)
            now = now.strftime("%A, %d de %B del %Y").lower()

            if value != "":
                return f"{value} fue {iterateDays(now)}"
            else:
                return f"Hace {days} días fue {iterateDays(now)}"
        except:
            return "Aún no existíamos"
    else:
        return "No entendí, ¿Que quizo decir?"