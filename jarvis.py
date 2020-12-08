import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Listening...")
	r.pause_threshold = 1
	audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio)
		print(query)
	except Exception as e:
		print(e)
		print("404!")
