name = input("enter your name: ")
f = ("playing music for you!",name)
n = ("Hello",name,"I am jarvis, how can I help you ?")
import os
import smtplib
import random
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser as wb

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

jokes = ["Name the kind of tree you can hold in your hand? A palm tree!","whats Thanos favourite app ?","Whats a cats favorite dessert? A bowl full of mice-cream","Why do birds fly south in the winter? Its faster than walking!","What did the left eye say to the right eye? Between us, something smells!"]

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("ashwinkyadav12354@gmail.com", "VSCODEM1")
    server.sendmail("ashwinkyadav12354@gmail.com", to, content)
    server.close()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour<=12):
        speak("Good morning!")
    elif (hour >= 12) and (hour <= 18):
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak(n)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    
    try:
        print("Recongnizing...")    
        query = r.recognize_google(audio,language="en-in")
        print(f"You said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again!")
        return "none"
    return query

if __name__ == "__main__":
    wishme()
    if 2:
        query = takecommand().lower()
        
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open Google" in query:
            speak("opening google for you.")
            wb.open_new("https://www.google.com")
        elif "play music" in query:
            music = "D:\\songs"
            songs = os.listdir(music)
            os.startfile(os.path.join(music, songs[0]))
            speak(f)
        elif "open youtube" in query:
            speak("opening youtube for you.")
            wb.open_new("youtube.com")
        elif "the time" in query:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            print(t)
            speak(t)
        elif "tell me joke" in query:
            speak("Name the kind of tree you can hold in your hand?  A palm tree!")
            speak("DID YOU LIKE THIS??")
            a = input()

            if "yes" in a:
                speak("Oh! thanks for your feedback!")
            elif "no" in a:
                speak("Oh! I done a mistake! Sorry!")
            else:
                speak("don,t wanna give a feedback?? no problem!!")
        elif "python" in query:
            speak("here's what I have found on the web")
        elif "oscillation" in query:
            speak("you have been a studious student!! see this I have found you this video for you!!")
            wb.open_new("https://www.youtube.com/oscillation/PhysicsWallah")
        elif "html" in query:
            speak("opening w3schools website to teach you html!!")
            wb.open_new("https://www.w3schools.com/htmltutorial")
        elif "send email to riya" in query:
            try:
                speak("What do I say??")
                to = "vaibhav6193911@gmail.com"
                content = takecommand()
                sendEmail(to, content)
                speak("Email has been sent!!")
            except Exception as e:
                speak("Sorry sir, this email cannot be sent!!")
        elif "I am bored" in query:
                speak("THERE ARE MORE STARS IN THE UNIVERSE THAN GRAINS OF SANDS ON EARTH!")
                speak("The universe extends far beyond our own galaxy, The Milky Way, which is why scientists can only estimate how many stars are in space.  However, scientists estimate the universe contains approximately 1,000,000,000,000,000,000,000,000 stars, or a septillion.   While no one can actually count every single grain of sand on the earth, the estimated total from researchers at the University of Hawaii, is somewhere around seven quintillion, five hundred quadrillion grains.  That is an awfully big sand castle!")
                speak("did you find this interesting??")
                h = takecommand()

                if "yes" in h:
                    speak("ok,thank you so much for your feedback!!")
                elif "no" in h:
                    speak("Ok I will improve myself!!")
                else:
                    speak("don't wanna give a feedback, no worries")
