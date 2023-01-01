from os import system
import time
import pyautogui
import os
import tkinter as tk
import webbrowser
from .talk_a import talk
from .listen import audio, listen
import pywhatkit
import datetime
import wikipedia
from Numeros.numeros import nm, np, nb, nl, ns, nf, na, nl2, nA, ng, nn, nv, ni, no
from Days.days import getDay, getDaysAgo
import pyjokes
from .greetings import greetings2
from playsound import playsound

def run():
    while True:
        rec = audio()
        rec_json = audio()
        rec = rec_json['text']
        status = rec_json['status']

        if status:
            if 'reproduce' in rec:
                music = rec.replace('reproduce', '')
                print("Reproduciendo {}".format(music))
                talk("Reproduciendo {}".format(music))
                pywhatkit.playonyt(music)

            elif 'hora' in rec:
                hora = datetime.datetime.now().strftime('%I:%M %p')
                print('Son las '+ hora + f" del {getDay()}")
                talk('Son las '+ hora + f" del {getDay()}")

            elif 'wikipedia' in rec:
                print('Buscando en Wikipedia...')
                talk('Buscando en Wikipedia...')
                statement = rec.replace("wikipedia", "")
                wikipedia.set_lang("es")
                results = wikipedia.summary(statement, sentences=3)
                print("De acuerdo a Wikipedia")
                talk("De acuerdo a Wikipedia")
                print(results)
                talk(results)

            elif 'busca en google' in rec:
                search = rec.replace('busca en google', '')
                print("Buscando sobre {}".format(search))
                talk("Buscando sobre {}".format(search))
                pywhatkit.search(search)

            elif "busca en windows" in rec: 
                winsearch = rec.replace("busca en windows", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                print("Okey señor, busque {}".format(winsearch))
                talk ("Okey señor, busque {}".format(winsearch))
                pyautogui.click(74, 1067)
                time.sleep(2)
                pyautogui.write(winsearch)
                time.sleep(3)
                pyautogui.click(x=125, y=507)

            elif 'mensaje por whatsapp' in rec:
                print("A quien quieres que mande el mensaje?")
                talk("A quien quieres que mande el mensaje?")
                recwhat = listen()
                if 'mamá' in recwhat:
                    print("Que quiere que le envie a mamá?")
                    talk("Que quiere que le envie a mamá?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(nm, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif "benja" in recwhat:
                    print("Que quiere que le envie a Benji?")
                    talk("Que quiere que le envie a Benji?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(nb, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif "papá" in recwhat:
                    print("Que quiere que le envia a su padre?")
                    talk("Que quiere que le envia a su padre?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(np, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif "lore" in recwhat:
                    print("Que quiere que le envie a Lorena?")
                    talk("Que quiere que le envie a Lorena?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(nl, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif "francisco" in recwhat:
                    print("Que quiere que le envie a Woody?")
                    talk("Que quiere que le envie a Woody?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(ns, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif 'fdp' in recwhat:
                    print("Que quiere que le envie a Said?")
                    talk("Que quiere que le envie a Said?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(nf, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif 'victor' in recwhat:
                    print("Que quiere que le envie a Victor?")
                    talk("Que quiere que le envie a Victor?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(nv, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif 'paula' in recwhat:
                    print("Que quiere que le envie a Apu?")
                    talk("Que quiere que le envie a Apu?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(na, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif 'leandro' in recwhat:
                    print("Que quiere que le envie a Leandro?")
                    talk("Que quiere que le envie a Leandro?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(nl2, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif 'prima' in recwhat:
                    print("Que quiere que le envie a Abichita?")
                    talk("Que quiere que le envie a Abichita?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(nA, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif 'nalva' in recwhat:
                    print("Que quiere que le envie a Nalvita?")
                    talk("Que quiere que le envie a Nalvita?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(nn, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif 'Mariana' in recwhat:
                    print("Que quiere que le envie a Mariana?")
                    talk("Que quiere que le envie a Mariana?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(ng, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif 'bruno' in recwhat:
                    print("Que quiere que le envie a Brunito?")
                    talk("Que quiere que le envie a Brunito?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(ni, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                elif 'matias' in recwhat:
                    print("Que quiere que le envie a Matias?")
                    talk("Que quiere que le envie a Matias?")
                    recmsg = listen()
                    print("Usted quiere este mensaje: ", recmsg)
                    system("Pause")
                    pywhatkit.sendwhatmsg_instantly(no, recmsg, 15), pyautogui.click(1637, 985), pyautogui.click(x=1742, y=994)

                else: 
                    print('Por favor diga un contacto guardado')
                    talk('Por favor diga un contacto guardado')

            elif 'apaga la compu' in rec:
                print("Usted quiere que se apague la pc?")
                talk("Usted quiere que se apague la pc?")
                recoff = listen()
                if 'si' in recoff:
                    print("Okey señor usted quizo que es apague la pc, Se esta apagando, descanse")
                    talk("Okey señor usted quizo que es apague la pc, Se esta apagando, descanse")
                    os.system("shutdown /s /t 1")

                else:
                    talk("Usted no quizo que se apague la compu, continue en lo que estaba haciendo")
                    print("Usted no quizo que se apague la compu, continue en lo que estaba haciendo")

            elif 'abre' in rec:
                #print("Okey Señor, ¿Que quiere que abra?")
                #talk("Okey Señor, ¿Que quiere que abra?")
                #recopen = listen()
                if 'el navegador' in rec:
                    print("Okey señor, se esta abriendo opera")
                    talk("Okey señor, se esta abriendo opera")
                    os.startfile('C:/Users/leona/AppData/Local/Programs/OperaGX/launcher.exe')

                elif 'fortnite'in rec:
                    print("Okey señor, se esta abriendo Fortnite")
                    talk("Okey señor, se esta abriendo Fortnite")
                    os.startfile("D:/Fortnite/Fortnite/FortniteGame/Binaries/Win64/FortniteClient-Win64-Shipping.exe")

                elif 'crunchyroll' in rec:
                    print("Okey señor, se esta abriendo crunchyroll")
                    talk("Okey señor, se esta abriendo crunchyroll")
                    webbrowser.open('https://beta.crunchyroll.com/es-es?beta_opt_in=1')

                elif 'whatsapp' in rec:
                    if 'web' in rec:
                        print('Okey señor, se esta abriendo whatsapp web')
                        talk('Okey señor, se esta abriendo whatsapp web')
                        webbrowser.open('https://web.whatsapp.com')

                    else:
                        print('Okey señor, se esta abriendo whatsapp')
                        talk('Okey señor, se esta abriendo whatsapp')
                        pyautogui.click(74, 1067)
                        time.sleep(2)
                        pyautogui.write("whatsapp")
                        time.sleep(3)
                        pyautogui.click(x=125, y=507)

                elif 'grabadora' in rec:
                    print("Okey señor, Se esta abriendo OBS")
                    talk("Okey señor, Se esta abriendo OBS")
                    pyautogui.click(74, 1067)
                    time.sleep(2)
                    pyautogui.write("obs")
                    time.sleep(3)
                    pyautogui.click(x=125, y=507)

                elif "spotify" in rec:
                    print("Okey señor, se esta abriendo spotify")
                    talk("Okey señor, se esta abriendo spotify")
                    pyautogui.click(74, 1067)
                    time.sleep(2)
                    pyautogui.write("spotify")
                    time.sleep(3)
                    pyautogui.click(x=125, y=507)

                elif "archivos" in rec:
                    print("Okey señor, se esta abriendo el explorador de archivos")
                    talk ("Okey señor, se esta abriendo el explorador de archivos")
                    pyautogui.click(74, 1067)
                    time.sleep(2)
                    pyautogui.write("archivos")
                    time.sleep(3)
                    pyautogui.click(x=125, y=507)

                elif "instagram" in rec:
                    print("Okey señor, se esta abriendo instagram")
                    talk ("Okey señor, se esta abriendo instagram")
                    time.sleep(1)
                    webbrowser.open("https://www.instagram.com/?hl=en")

                elif "mensajes de insta" in rec:
                    print("Okey señor se estan abriendo el inbox de instagram")
                    talk("Okey señor se estan abriendo el inbox de instagram")
                    webbrowser.open("https://www.instagram.com/direct/inbox/?hl=en")

                else:
                    print("Usted no quizo que abra nada asi que retornemos desde el comienzo")
                    talk("Usted no quizo que abra nada asi que retornemos desde el comienzo")
                    run()

            #elif "escribe" or "escribas" in rec:
            #    print("Okey señor lo estoy escuchando para transcribir lo que dicte")
            #    talk("Okey señor lo estoy escuchando para transcribir lo que dicte")
            #    recesritura = listen()
            #    print("Okey señor aqui esta lo que quizo que yo escriba: ")
            #    talk("Okey señor aqui esta lo que quizo que yo escriba: ")
            #    escritura = recesritura
            #    print(escritura)
            #    talk(escritura)

            elif 'que dia' in rec:
                if 'fue' in rec:
                    print(f"{getDaysAgo(rec)}")
                    talk(f"{getDaysAgo(rec)}")
                else:
                    print(f"Hoy es {getDay()}")
                    talk(f"Hoy es {getDay()}")

            elif 'chiste' in rec:            
                chiste = pyjokes.get_joke("es")
                print(chiste)
                talk(chiste)

            elif "anime" in rec:
                print("¿Que anime quiere que ponga Señor?")
                talk("¿Que anime quiere que ponga Señor?")
                recanime = listen()
                print("Okey Señor, pondre: " + recanime)
                talk("Okey Señor, pondre: " + recanime)
                webbrowser.open("https://beta.crunchyroll.com/es-es/")
                time.sleep(7)
                pyautogui.click(x=1586, y=132), time.sleep(3), pyautogui.write(recanime), time.sleep(3), pyautogui.click(x=533, y=564), time.sleep(4), pyautogui.click(x=1338, y=902)

            elif "alarma" in rec:
                print("A que hora quiere la alarma?")
                talk("A que hora quiere la alarma?")
                recalh = int(input())
                print("Y ahora a que minutos los quiere la alarma?")
                talk("Y ahora a que minutos los quiere la alarma?")
                recalm = int(input())
                print("Quiere que sea pm o am?")
                talk("Quiere que sea pm o am?")
                recam = input()
                if "pm" in recam:
                    recalh+=12
                
                while True:
                    if recalh == datetime.datetime.now().hour and recalm == datetime.datetime.now().minute:
                        print("Se reproducira la alarma...")
                        talk("Se reproducira la alarma...")
                        playsound('C:/Users/leona/Downloads/mixkit-space-shooter-alarm-1002.wav')
                        break         

            elif "descansa" in rec:
                print(f"Okey señor, usted tambien descanse {greetings2()}")
                talk(f"Okey señor, usted tambien descanse {greetings2()}")
                break

            else:
                print('Por favor repita lo que dijo')
                talk('Por favor repita lo que dijo')
                run()
