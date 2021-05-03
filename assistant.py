import pyttsx3
import wikipedia
import webbrowser
import datetime
import random
import os
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning sir!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon sir!')
    else:
        speak('Good evening sir!')
    speak('How may i help you?')

    

def takeCommand():
    '''
    takes microphone input from user and returns string output
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...\n')
        r.pause_threshold= 1
        audio=r.listen(source)

    try:
        print('Recognizing...\n')
        query=r.recognize_google(audio,language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
       #print(e)
        print('Say again please...')
        return 'None'

    return query
if __name__=='__main__':
    #speak('hello Harsh sir')
    #speak('How can i help you?')
    wishMe()
    while(True):
        query=takeCommand().lower()

        if "search" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak('Wikipedia says')
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open codeforces" in query:
            webbrowser.open("codeforces.com")

        elif "open codechef" in query:
            webbrowser.open("codechef.com")

        elif "what's the time" in query or 'say time' in query:

            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime} ") 

        elif "open VScode" in query or 'open code' in query:
            path="C:\\Users\\pipal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif  "play music" in query:
            m=random.randint(0,10)
            music_dir="C:\\Users\\pipal\\OneDrive\\Desktop\\Songs"
            songs=os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[m]))

        elif "play my favourite video" in query:
            webbrowser.open("https://www.youtube.com/watch?v=Fckxobna9bk")

        elif "quit" in query:
            speak("quitting")
            speak("chaltu huuu bro")


        else:
            print("Thanks for using")



