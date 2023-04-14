import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

# Take Some Voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
# Make Speak Function for Speaking Computer
def speak(audio):
    engine.say(audio)
    engine.setProperty('rate',100)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    elif hour>18  :
        speak("Good Evening!")  
    
    else:
        speak("Good Night!")

    speak("Me hoo Bhola,  bolo Ki meeh aapki Kaisee Madat Kar Sakta hoon")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        # query = r.recognize_bing(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        speak("Teez boolo")
        print("Say that again please...")  
        return "None"
        
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kumarp73616@gmail.com', 'PkJk@1508')
    server.sendmail('kumarp73616@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # query = input("Enter Your Choice: ")

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'game' in query:
            gmpath= "C:\\Users\\Prem Kumar\\Desktop\\Cricket2009.exe - Shortcut"
        
            os.startfile(gmpath)

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        
        elif 'music' in query:
            music_dir = 'C:\\Users\\kumar\\Music\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'code' in query:
            codePath = "C:\\Users\\Prem Kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'bye' in query:
            speak("Bye Mere Dost Twinkle Twinkle Little Star Bye Meere Yaar") # Twinkle Twinkle Little Star Bye Meere Yaar
            break
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harry@codewitharry.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Mere Dost  Prem bhai. Meeh Iss Email Ko nahi Bhej Sakta Hoon")

        else:
            speak("I can't Do That")
        
