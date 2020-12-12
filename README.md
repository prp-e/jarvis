# Jarvis ; Voice assistant inspired by Iron man

Edwin Jarvis, or Jarvis, is a person who helps Tony Stark and a bunch of other heros from Marvel's Universe. This is how he looks like: 

![Edwin Jarvis](Edwin_Jarvis.jpg) 

But for some reason, they decided to make him an artifial intelligence assistant in the Iron Man trilogy. Back in 2008, it wasn't really easy to make something like this. But it's 2020 now. Despite all bad things happened to us, we just need some fun. What is better than developing our own personal assistant? This version here isn't an A.I. by the way. It's just a simple voice assistant who does what you code for him. 

## Dependencies

* `pyaudio` 
* `SpeechRecognition`
* `requests`
* `python-youtube-music` : apparantly this one isn't installable from PyPi yet. Follow instructions [here](https://github.com/tombulled/python-youtube-music). 

### pyaudio 

In order to get pyaudio to work, you need `portaudio`. To install portaudio, on Linux machines (Debian/Ubuntu. I have no idea how it will be installed on Fedora or those fancy non-systemd distros!) you should run `sudo apt install portaudio19-dev` and after that, `sudo apt install python3-pyaudio`. On macOS, you just need to install `portaudio` from `brew` using `brew install portaudio` and then install each dependency using `pip`. 

## Notes for macOS users 

If you've installed python using `brew`, it's not gonna work. Why? I don't know. Apparantly there is some problems with needed libraries and XCode. So the best solution is installing python from [python.org](http://python.org/). 

## How to configure Jarvis 

First of all, copy `config_example.py` to `config.py` so it can be understood by `jarvis.py` as a legit configuration file. Then, you need to modify these variables : 

* `WEATHER_API_KEY` : Go to [OpenWeatherMap](http://openweathermap.org/) and sign up. It doesn't require anything and it will give you an api key. Copy and paste it here. 
* `MY_NAME` : So, type your name here. 
* `MY_TITLE`: To make it more like what we saw in the movie, I used _Sir_. But of course you can use everything your like. I don't know, maybe _Ma'am_ or _Your Majesty_ or _Bro_? (Do you know what Bro means in Mandarin? Oh, sorry for Silicon Valley reference. ) 
* `NEIGHBORHOOD` : Leave it 0, Jarvis will ask you for the location anytime you say "weather". If you fill it with some appropriate locations (trust me, it's a bit hard for him to understand Iranian citites!) he will answer you much better. 

## Commands 

- [x] What time is it? Jarvis will tell you the time. 
- [x] Search for _Keyword_. Jarvis will do a web search for you. 
- [x] Information about _Keyword_. Jarvis will do a wikipedia search for you. 
- [x] Goodbye. This command destroys current Jarvis session.
- [x] Play Music. Jarvis will play your favorite song for you.