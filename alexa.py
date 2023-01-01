import speech_recognition as sr
from Settings_a.voice_a import voice
from Settings_a.greetings import greetings
from Settings_a.run import run
listener = sr.Recognizer()

voice()
greetings()
run()

