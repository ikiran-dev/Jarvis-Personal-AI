import os
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import subprocess
import webbrowser as web
import time
import keyboard
import pywhatkit as kit
import re
import mouse
#import trial


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')
engine.setProperty('rate',185)
from pyfiglet import figlet_format
from termcolor import colored
art = ("                  WELCOME TO "
"                                    JARVIS")
ascii_art = figlet_format(art, )
clr = colored(ascii_art,"green")
print(clr)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Pardon me, Please say that again")
            return "None"
        return statement

def gooogle(message):

    url = "https://google.com/search?q=" + message
    speak(f"searching for {message} on google")
    webbrowser.open(url)

def youtube(message):
    url = "https://www.youtube.com/results?search_query=" + message
    speak(f"searching for {message} on youtube")
    webbrowser.open(url)

    
    

def whatsapp (number, message):
    num = '+91' + number
    int(num)
    message = message
    open_chat = "https://web.whatsapp.com/send?phone=" + num + "&text=" + message
    web.open(open_chat)
    time.sleep(15)
    mouse.click('left')
    keyboard.press('enter')

def whatsapp_grp(group_id, message):
    open_chat = "htpps://web.whatsapp.com/accept?code=" + group_id 
    web.open(open_chat)
    time.sleep(15)
    mouse.click('left')
    keyboard.write(message)
    time.sleep(1)
    keyboard.press('enter')

print("Loading your AI personal assistant Jarvis")
speak("Loading your AI personal assistant Jarvis")
wishMe()

if __name__=='__main__':


    while True:
        speak("Tell me how can i help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or 'exit' in statement:
            speak('your personal assistant Jarvis is shutting down,Good bye')
            print('Your personal assistant Jarvis is shutting down, Good bye!!')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(10)

        elif 'sleep' in statement:
            speak("Going to sleep")
            print("In sleep mode for 100 seconds")
            time.sleep(100)
            

        elif 'youtube' in statement:
            statement = statement.replace("jarvis","")
            statement = statement.replace("search","")
            statement = statement.replace("youtube","")
            statement = statement.replace("on","")

            message = statement
            youtube(message)
            time.sleep(10)

        elif 'thank you' in statement:
            speak('It was my pleasure assisting you!')
            print("You're Welcome")
            time.sleep(5)

        elif 'google' in statement or 'search' in statement:
            statement = statement.replace("jarvis","")
            statement = statement.replace("google","")
            statement = statement.replace("search","")
            message = statement
            gooogle(message)
            time.sleep(10)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com")
            speak("G-Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "open github" in statement:
            webbrowser.open_new_tab("https://github.com/ikiran-dev")
            speak("Here is kiran's GitHub")

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by kiirran")
            print("I was built by kiran")

        elif  "mobile" in statement:
            speak("Hang on! acessing your mobile")
            print("Acessing your mobile")
            file = "E:\\orgscrcpy\\scrcpy.exe"
            os.startfile(file)
            time.sleep(30)

        elif  "covid analysis" in statement:
            speak("Hang on! analysing covid patterns")
            print("Covid Analysis Report")
            file = "E:\\projects\\covid analysis\\covid-19.py"
            os.startfile(file)
            time.sleep(20)


        elif 'who are you' in statement or 'what can you do' in statement or 'introduce yourself' in statement:
            speak('I am Jarvis  your personal assistant. I am programmed to do minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,access android devices,search wikipedia,whatsapp '
                  'message his friends ,analyse covid-19 patterns, get top headline news from times of india and much more!')
            time.sleep(5)
            
        
        
        elif 'whatsapp message' in statement:
            statement = statement.replace("Jarvis","")
            statement = statement.replace("send","")
            statement = statement.replace("whatsapp message","")
            statement = statement.replace("to","")
            name = statement

            if 'rohit' in name:
                numb ="9731310176"
                speak(f"What's the message for {name}")
                mess = takeCommand()
                speak(f"sending {mess} to rohit")
                whatsapp(numb,mess)
            elif 'narendra' in name:
                numb ="9902394522"
                speak(f"What's the message for {name}")
                mess = takeCommand()
                speak(f"sending {mess} to narendra")
                whatsapp(numb,mess)
            

                
        elif 'play' in statement:
            statement = statement.replace("jarvis","")
            statement = statement.replace("play","")
            message = statement
            speak(f'playing {message} on youtube')
            time.sleep(1)
            kit.playonyt(message)
            time.sleep(10)

        elif 'hello jarvis i am' in statement or "jarvis i am" in statement:
            statement = statement.replace("jarvis","")
            statement = statement.replace("hello","")
            statement = statement.replace("i am","")
            statement = statement.replace("i'm","")
            message = statement
            speak(f"Thanks for the introduction. Lovely to meet you {message}")
            print(f"Lovely to meet you{message}")
            time.sleep(2)

        elif "college website" in statement:
            url ="https://gsksjti.ac.in/"  
            webbrowser.open(url)
            speak("welcome to Government Shri Krishnarajendra Silver Jubilee Technological Institute")
            print("Welcome to Government Sri Krishnarajendra Silver Jubilee Technological Institute")
            time.sleep(30)
        
        elif "wi-fi password" in statement:
           command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
           profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
           wifi_list = []
           if len(profile_names) != 0:
                for name in profile_names:
                    wifi_profile = {}
                    profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
                    if re.search("Security key           : Absent", profile_info):
                        continue
                    else:
                        wifi_profile["ssid"] = name
                        profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
                        password = re.search("Key Content            : (.*)\r", profile_info_pass)
                        if password == None:
                            wifi_profile["password"] = None
                        else:
                            wifi_profile["password"] = password[1]
                            wifi_list.append(wifi_profile) 

           for x in range(len(wifi_list)):
                print(wifi_list[x]) 
           speak('here are your wifi passwords')

        '''elif "lights" in statement or "light" in statement:
            statement = statement.replace("jarvis","")
            statement = statement.replace("turn","")
            statement = statement.replace("lights","")
            message = statement
            

            trial.light_control(message)'''
