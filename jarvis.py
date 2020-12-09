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
			self.voice_recognizer.pause_threshold = 1
			audio = self.voice_recognizer.listen(source)

			try:
				print("Recognizing...")
				query = self.voice_recognizer.recognize_google(audio)
				print("You said: " + query)
				self.voice_engine.say(query)
				self.voice_engine.runAndWait()
			except Exception as e:
				print(e)
				self.voice_engine.say("Not in a language I understand, or not a valid command.")
				self.voice_engine.runAndWait()


if __name__ == '__main__':
	jarvis_init = Jarvis(sr.Recognizer(), pyttsx3.init())
	jarvis_init.initial_speak() 
	jarvis_init.talk_back()