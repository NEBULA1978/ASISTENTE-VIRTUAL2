import pyttsx3

engine = pyttsx3.init()
engine.say("Hola mundo")
# Para escribir en cosola texto a hablar
# engine.say(input())
engine.runAndWait()