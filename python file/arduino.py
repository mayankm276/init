#Program to Control	LED of Arduino from Pyhton

import serial #Serial imported for Serial communication
import time #Required to use delay functions
import speech_recognition as sr

	

ArduinoSerial = serial.Serial('/dev/ttyACM0', 9600) #Create Serial port object called 
time.sleep(2) #wait for 2 seconds for the communication to get established

print (ArduinoSerial.readline()) #read the serial data and print it as line
print ("Say light on to turn ON LED and light off to turn OFF LED")

while 1: #Do this forever

	# obtain audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Say something!")
	    audio = r.listen(source)

	# recognize speech using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))



	
	var = r.recognize_google(audio) #get input from user
	print ("you said", var) #print the input for confirmation
	var.lower()

	a=0
	b=0

	if "light" in var:
		a += 1
		b += 1

	if "on" in var:
		a += 1
	
	if "off" in var:
		b += 1	

	if (a == 2): #if the value is 1
		ArduinoSerial.write(b'1') #send 1
		print ("LED turned ON")
		time.sleep(1)

	if (b == 2): #if the value is 0
		ArduinoSerial.write(b'0') #send 0
		print ("LED turned OFF")
		time.sleep(1)	