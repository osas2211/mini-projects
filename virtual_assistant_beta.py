from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr
import random
import webbrowser

#GOOGLE TEXT TO SPEECH
def speech(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio = 'audio-' + str(r) + '.mp3'
    tts.save(audio)
    playsound(audio)
    print(audio_string)
    os.remove(audio)

#GET VOICE DATA
r = sr.Recognizer()
def record_voice(ask = False):
    with sr.Microphone() as source:
        if ask:
            speech(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speech('Sorry, I did not get you')
        except sr.RequestError:
            speech('Sorry, you are either offline or my services are down')
        return voice_data

#RESPONSE FROM gTTS
def respond(voice_data):
    if 'what is your name' in voice_data:
        speech('My Name is Frank Jarvis!')
    if 'who are you' in voice_data:
        speech("I am Frank's Virtual assistant")
    if 'search' in voice_data:
        search = record_voice('What do you Want to Search for ?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
    if 'what is my relationship status' in voice_data:
        speech('Do you have a girlfriend? or should i keep quiet?. Try shift go one side')

name = lambda : record_voice('what is your name')
speech(f'Hello {name()}, how may i help?')
voice_data = record_voice()
respond(voice_data)


