import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "<Your news api >"



def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="< Your Open Ai API",
                    )



    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa, Google, Siri and Google Cloud."},
        {
            "role": "user",
            "content": command
        }
    ]
    )

    return completion.choices[0].message.content







def processCommand(c):
    speak(f"You said: {command}") #Speaks what you said

    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")   
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")   
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")   
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]
        link =musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            #Parse the Json Response
            data = r.json()

            #Extract the articles
            articles = data.get('articles',[])

            #Print the headlines.
            for article in articles:
                speak(article['title'])

    else:
        #Let OpenAI handle the request
       output =  aiProcess(c)
       speak(output)







if __name__ =="__main__":
    speak("Initializing Jarvis...")
    while True:
        #Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        print("Recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=3, phrase_time_limit=1)
            word = r.recognize_google(audio, language="en-IN")
            if(word.lower() == "jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)


                    processCommand(command)

        except Exception as e:
            print(" error; {0}".format(e))

