# import pyttsx3

# engine = pyttsx3.init()
# engine.say("Hola mundo")
# # Para escribir en cosola texto a hablar
# # engine.say(input())
# engine.runAndWait()

import speech_recognition as sr

r = sr.Recognizer()

# Hablo con micro y me escribe lo hablado en consola
with sr.Microphone() as source:
    print("Por favor habla")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, languages="es")
        print(text)
    except:
        print("No entendi lo que dijiste")