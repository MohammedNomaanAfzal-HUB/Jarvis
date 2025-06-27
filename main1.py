import pyttsx3  
import speech_recognition as sr  
import datetime
import wikipedia  
import webbrowser
import os
import openai
import smtplib
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

openai.api_key = 'your-api-key'  # Replace 'your-api-key' with your actual OpenAI API key

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        print("Say that again please...")
        return "None"

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('b21cs028@kitsw.ac.in', 'Zohaib@028')  # Replace with sender email and password
    server.sendmail('b21cs028@kitsw.ac.in', to, content)
    server.close()

def openWhatsApp():
    webbrowser.open("https://web.whatsapp.com")

def start_chat():
    print("You are now chatting with the AI. Type 'quit' to end the conversation.")
    user_input = ""
    while user_input.lower() != 'quit':
        user_input = input("You: ")
        if user_input.lower() != 'quit':
            response = openai.Completion.create(
                engine="text-davinci-003",  # Specify the GPT model you want to use
                prompt=user_input,
                max_tokens=150
            )
            print("AI:", response.choices[0].text.strip())

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "zohaibuzohaib3@gmail.com"  # Replace with recipient email
                sendEmail(to, content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'play music' in query:
            # Modify this part based on how you want to play music
            speak("Sure! Playing music for you.")
            # Example: You can open a local file or a streaming service like Spotify
            # Example: os.system("start your_music_file.mp3") or 
            webbrowser.open("https://www.spotify.com")

        elif 'open vs code' in query:
            # Implement opening Visual Studio Code functionality using subprocess
            speak("Opening Visual Studio Code")
            subprocess.Popen(["code"])

        elif 'open chatgpt' in query:
            # Open ChatGPT
            speak("Opening ChatGPT")
            start_chat()

        elif 'open whatsapp' in query:
            # Open WhatsApp Web
            speak("Opening WhatsApp Web")
            openWhatsApp()

        elif 'shut down' in query:
            # Implement shutdown functionality using subprocess
            speak("Shutting down the computer")
            subprocess.call(["shutdown", "/s", "/f", "/t", "0"])
