from datetime import datetime
import speech_recognition as sr
import pyttsx3

class Jarvis:
	def __init__(self, voice_recognizer, voice_engine): 
		self.voice_recognizer = voice_recognizer
		self.voice_engine = voice_engine

	def initial_speak(self): 
		now = datetime.now() 
		if now.hour == 12:
			self.voice_engine.say("Hey, Good afternoon! I am Jarvis. I say what you say back to you.")
		elif now.hour > 12:
			self.voice_engine.say("Hey, Good evening! I am Jarvis. I say what you say back to you.") 

		self.voice_engine.runAndWait()

	def talk_back(self): 
		with sr.Microphone() as source:
			print("Listening...")
			r.pause_threshold = 1
			audio = self.voice_recognizer.listen(source)

			try:
				print("Recognizing...")
				query = self.voice_recognizer.recognize_google(audio)
				print("You said: " + query)
				self.voice_engine.say(query)
				self.voice_engine.runAndWait()
			except Exception as e:
				print(e)
				self.voice_engine.say("Nothing heard, please try again later")
				self.voice_engine.runAndWait()


if __name__ == '__main__':
	jarvis_init = Jarvis(sr.Recognizer(), pyttsx3.init())
	jarvis_init.initial_speak() 
	jarvis_init.talk_back()

"""
r = sr.Recognizer()
now = datetime.now() 
voice_engine = pyttsx3.init()

if now.hour == 12:
	voice_engine.say("Hey, Good afternoon! I am Jarvis. I say what you say back to you.")
elif now.hour > 12:
	voice_engine.say("Hey, Good evening! I am Jarvis. I say what you say back to you.")
	
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
"""