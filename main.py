import pyttsx3  #pip install pyttsx3
import speech_recognition as sr     #pip install speechRecognition
import datetime
import wikipedia    #pip install wikipedia
import webbrowser
import os
import smtplib


MASTER = "Arif"
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


#fungsi inisilalisasi jarvis agar dapat dibaca oleh mesin
def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("arif is a good boy")

#fungsi untuk menyapa sang MASTER alias tuan
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 0 and hour < 9:
        speak("Good Morning" + MASTER)

    elif hour >= 9 and hour < 15:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good evening" + MASTER)

    #speak("I am Jarvis. How may i can help you?")



#program utama jarvis / mengambil perintah dari microphone
#perintah dalam bentuk suara

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-id")
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please!")
        query = None

    return query


'''
#program fungsi untuk mengirim email menggunakan smtplib
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("ouremail@gmail.com", to, content)
    server.close()
'''


def programUtama():
    # program akan dimulai dari sini
    #speak("initializing Tama...")
    wishMe()
    query = takeCommand()

    #logika untuk mengeksekusi perintah suaran
    if "wikipedia" in query.lower():
        speak("Searching wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif "open google maps" in query.lower():
        url = "maps.google.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    #elif 

    elif "open youtube" in query.lower():
        url = "youtube.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    elif "open google" in query.lower():
        url = "google.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    elif "open facebook" in query.lower():
        url = "facebook.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    elif "open instagram" in query.lower():
        url = "instagram.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    elif "open whatsapp" in query.lower():
        url = "web.whatsapp.com/"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    elif "play music" in query.lower():
        songs_dir = "D:\\uk"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif "the time" in  query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"{MASTER} the time is {strTime}")

    elif "open coding" in query.lower():
        codePath ="C:\\Users\COSTUMER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif "what is your name" or "what's your name" in query.lower():
        speak("my name is Andre, i am Arifin assisten, i am building using python")
        speak("i can do anything, like play music, open a browser, youtube, facebook, instagram or anything")
        speak("call me if you need help")
        speak("but please understand if there are deficiencies because I am still in the development stage. thank you")


#    elif "have a girlfriend" in query.lower():
        #speak("no, i dont have a girlfriend")
        #speak("i can do anything, like play music, open a browser, youtube, facebook, instagram or anything")
        #speak("call me if you need help")
        #speak("but please understand if there are deficiencies because I am still in the development stage. thank you")

    '''
    #send email
    elif "send email" in query.lower():
    try:
        speak("What should i will send")
        content = getCommand()
        to = "emailyouwillsendthemassage@gmail.com"
        sendEmail(to, content)
        speak("email has been sent successfully")
    except exceptions as e:
        speak(e)'''


programUtama()