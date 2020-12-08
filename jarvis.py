import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

voice_engine = pyttsx3.init()
voice_engine.say("Hey, I am Jarvis. I say what you say back to you.")
voice_engine.runAndWait()

with sr.Microphone() as source:
	print("Listening...")
	r.pause_threshold = 1
	audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio)
		print(query)
		if query == 'switch to Farsi':
			voice_engine.setProperty('voice', 'fa')
			voice_engine.say('سلام، من جارویس هستم. یک دستیار صوتی')
			voice_engine.runAndWait()
		else: 
			voice_engine.say(query)
			voice_engine.runAndWait()
	except Exception as e:
		print(e)
		print("404!")
