import pyttsx3
import speech_recognition as sr
import pytchat

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

vid_url = input("Video URL: ")
chat = pytchat.create(video_id=vid_url)
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.datetime} [{c.author.name}]- {c.message}")
        c.message.lower()
        if c.message == "hello":
            speak("Hello" + c.author.name + "Welcome to my stream!")