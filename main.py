import pyttsx3
import time

motor = pyttsx3.init()
motor.say('Hola amanda como estas? Donde esta ramon?')
time.sleep(10)
motor.say('cache gato amanda')
motor.runAndWait()