import datetime
import os
import random
import webbrowser
import pywhatkit
import speech_recognition as sr
import openai
import wikipedia

from config import api_key
import win32com.client


# web driver
def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    print("Listening...")
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print("User Said: ", query)
            return query
        except Exception as e:
            return "I can't Understand Sorry"


def ai(prompt):
    openai.api_key = api_key
    text = "☠☠ Ultimate- Responses ☠☠ \n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        result = response["choices"][0]["text"]
        text += result
        print(result)
        if not os.path.exists("ultimate-power"): os.mkdir("ultimate-power")
        with open(f"ultimate-power/{prompt[0:30]}.txt", "w", encoding="utf-8") as f:
            f.write(text)
        say("Done Existing Ultimate Mode")
    except Exception as e:
        print(e)
        say("Ultimate Has No Choices")

if __name__ == '__main__':
    say("Jarvis Activated")
    while True:
        text = takeCommand()
        query = text.lower()
        sites = [["youtube", "https://youtube.com"], ["google", "https://google.com"], ["github", "https://github.com"],
                 ["instagram", "https://instagram.com"]]
        if "ultimate" in query:
            say("Ultimate Jarvis Activated")
            say("Say Your Command Sir")
            prompt = takeCommand()
            ai(prompt)

        if "wikipedia" in query:
            say("Say What do you want to search on the wikipedia")
            query = takeCommand()
            res = wikipedia.search(query)
            print(res)
            say(res)


        elif "time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the Time is {strfTime}")
            print(strfTime)

        elif "code" in query:
            os.system(f"code")

        elif 'hello' in query:
            say("Hey, Sir How Can I Help You?")

        elif 'music' in query:
            music_dir = 'C:\\Users\\PremT\\Music\\'
            songs = os.listdir(music_dir)
            print(songs)
            r = random.randint(0, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[r]))

        elif 'bye' in query:
            say("Bye Sir Have a Nice Day")
            quit()

        elif 'song' in query:
            say("Tell me the name of the song")
            command = takeCommand()
            pywhatkit.playonyt(command)

        for site in sites:
            print(site)
            if site[0] in query:
                webbrowser.open_new_tab(site[1])
                say(f"Opening {site[0]} Sir")
                break
