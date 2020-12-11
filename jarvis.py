from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import ytm

class Jarvis:
	def __init__(self, voice_recognizer, voice_engine): 
		self.voice_recognizer = voice_recognizer
		self.voice_engine = voice_engine

	def initial_speak(self): 
		now = datetime.now() 
		if   now.hour < 12 and now.hour > 6:
			self.voice_engine.say("Hey, Good morning! I am Jarvis, a voice assistant who serves you in the way you like.")
		elif now.hour >= 12 and now.hour < 16: 
			self.voice_engine.say("Hey, Good afternoon! I am Jarvis, a voice assistant who serves you in the way you like.")
		elif now.hour > 16 and now.hour < 20:
			self.voice_engine.say("Hey, Good evening! I am Jarvis, a voice assistant who serves you in the way you like.") 
		elif now.hour > 20:
			self.voice_engine.say("Hey, Good night! I am Jarvis, a voice assistant who serves you in the way you like.")
		else:
			self.voice_engine.say("Hey, Good day! I am Jarvis, a voice assistant who serves you in the way you like.")

		self.voice_engine.runAndWait()

	def get_command(self): 
		with sr.Microphone() as source:
			print("Listening...")
			self.voice_recognizer.pause_threshold = 1
			audio = self.voice_recognizer.listen(source)

			try:
				print("Recognizing...")
				query = self.voice_recognizer.recognize_google(audio)
			except Exception as e:
				print(e)
				query = "Invalid command."

			return query

	def talk_back(self): 
		query = self.get_command() 
		self.voice_engine.say(query)
		self.voice_engine.runAndWait()

	def destroy_session(self):
		now = datetime.now()
		if   now.hour < 12 and now.hour > 6:
			self.voice_engine.say("Good morning! until the next time" )
		elif now.hour >= 12 and now.hour < 16: 
			self.voice_engine.say("Good afternoon! until the next time" )
		elif now.hour > 16 and now.hour < 20:
			self.voice_engine.say("Good evening! until the next time" ) 
		elif now.hour > 20 :
			self.voice_engine.say("Good night! until the next time" )
		else: 
			self.voice_engine.say("Good day! until the next time")

		self.voice_engine.runAndWait()
		exit()



if __name__ == '__main__':
	jarvis_init = Jarvis(sr.Recognizer(), pyttsx3.init())
	jarvis_init.initial_speak() 
	while True:
		query = jarvis_init.get_command().lower()
		print(query)
		if query == "what time is it":
			jarvis_init.voice_engine.say(f"The time is {datetime.now().hour} {datetime.now().minute}")
		elif query == "goodbye" or query == "bye":
			jarvis_init.destroy_session()
		elif "search for " in query:
			webbrowser.open_new_tab("https://google.com/search?q=" + query.replace("search for ", ""))
		elif query == "play music":
			jarvis_init.voice_engine.say("I will play what you say. It may take a few seconds. Please tell me the name of the song or artist.")
			jarvis_init.voice_engine.runAndWait()
			music_control = ytm.YouTubeMusic()
			track = jarvis_init.get_command().lower()
			results = music_control.search(track)
			track_details = results['songs'][0]
			jarvis_init.voice_engine.say("Now playing " + track)
			jarvis_init.voice_engine.runAndWait()
			webbrowser.open_new_tab("https://music.youtube.com/watch?v=" + track_details['id'] + "&list=" + track_details['radio']['playlist_id'])
			exit()
		else: 
			jarvis_init.voice_engine.say("Sorry sir, I don't now how to respond to that.")

		jarvis_init.voice_engine.say("done, what can I do for you now, Sir?")
		jarvis_init.voice_engine.runAndWait()
