import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import webbrowser as web
import time
import keyboard
import pywhatkit as kit
import re
import os
import requests
import urllib.request
import pyjokes as pyjokes
import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import ecapture as ec
import wolframalpha
import json
import socket
import re
import requests
import pyaudio
import random
import headlines
import getpass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import librosa
import soundfile
import numpy as np
import pickle
import glob
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import pickle
from scipy.io import wavfile
from bs4 import BeautifulSoup
import requests
import platform
import pyshorteners
import pyperclip
from tkinter import *
import pyautogui
from PIL import Image, ImageGrab 
import qrcode
import speedtest

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')
engine.setProperty('rate',160)


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
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        statement = r.recognize_google(audio, language='en-in')
        print(f"User said: {statement}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"

    return statement

def htLine1():
    speak("It's " + coinRes)


def htLine2():
    speak("You got " + coinRes)


def htLine3():
    speak("It landed on " + coinRes)

def defination(searchtext):
    url = 'https://www.dictionary.com/browse/'
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    })
    wikistr = wikipedia.summary(searchtext, sentences=3)
    index = wikistr.find(searchtext)
    if (index != -1):
        wikidef = wikipedia.summary(searchtext, sentences=3)
        return (wikidef)
    else:
        req = requests.get(url + searchtext, headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        mydivs = soup.findAll("div", {"value": "1"})[0]

        for tags in mydivs:
            meaning = tags.text
        return (meaning)



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
    keyboard.press('enter')

def whatsapp_grp(group_id, message):
    open_chat = "htpps://web.whatsapp.com/accept?code=" + group_id 
    web.open(open_chat)
    time.sleep(15)
    keyboard.write(message)
    time.sleep(1)
    keyboard.press('enter')

print("Welcome To Jarvis")
speak("Welcome To Jarvis")
wishMe()

if __name__=='__main__':

    speak("Tell me how can i help you now?")
    while True:
        
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or 'exit' in statement:
            speak('Jarvis is shutting down,Good bye')
            print('Jarvis is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(10)

        elif 'youtube' in statement:
            statement = statement.replace("jarvis","")
            statement = statement.replace("search","")
            statement = statement.replace("youtube","")
            statement = statement.replace("on","")
            statement = statement.replace("for","")

            message = statement
            youtube(message)
            time.sleep(10)

        elif 'thank you' in statement:
            speak('It was my pleasure assisting you!')
            print("You're Welcome")

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

        
        elif 'who are you' in statement or 'what can you do' in statement or 'introduce yourself' in statement:
            speak('I am Jarvis  your personal assistant. I am programmed to do minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,access android devices,search wikipedia,whatsapp '
                  'message his friends ,analyse covid-19 patterns, get top headline news from times of india and much more!')
            
            
        
        
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
            time.sleep(60)

        elif 'hello jarvis i am' in statement or "jarvis i am" in statement:
            statement = statement.replace("jarvis","")
            statement = statement.replace("hello","")
            statement = statement.replace("i am","")
            statement = statement.replace("i'm","")
            message = statement
            speak(f"nice! meeting you {message}. i'm glad to assist you")
            print(f"Nice Meeting you!{message}")

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

        elif 'open geeks for geeks' in statement:
            os.system("start brave www.geeksforgeeks.org") 

        elif 'covid-19 tracker' in statement:
            webbrowser.open_new_tab(
                "https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN%3Aen"
            )
            speak("covid-19 tracker is open now")
            time.sleep(5)

        elif "shoping" in statement or 'shopping' in statement:
            websites = ['amazon', 'flipkart', 'myntra', 'limeroad']
            print('\n'.join(websites))
            speak("nice mood sir!, what do you want to open?")
            user_ip = takeCommand().lower().replace(' ', '')

            for website in websites:
                if website in user_ip:
                    webbrowser.open_new_tab(website + '.com')

            speak("here you are sir")

        elif 'online courses' in statement or 'course' in statement:
            platforms = [
                'coursera', 'udemy', 'edx', 'skillshare', 'datacamp', 'udacity'
            ]
            speak("Select a platform that you prefer : ")
            print("\n".join(platforms))
            statement1 = takeCommand().lower()
            if statement1 == 0:
                continue
            if 'coursera' in statement1:
                webbrowser.open_new_tab("https://www.coursera.org")
                speak("Coursera is open now")
                time.sleep(2)
            elif 'udemy' in statement1:
                webbrowser.open_new_tab("https://www.udemy.com")
                speak("udemy is open now")
                time.sleep(2)
            elif 'edx' in statement1:
                webbrowser.open_new_tab("https://www.edx.org/")
                speak("edx is open now")
                time.sleep(2)
            elif 'skillshare' in statement1:
                webbrowser.open_new_tab("https://www.skillshare.com")
                speak("skill share is open now")
                time.sleep(2)
            elif 'datacamp' in statement1:
                webbrowser.open_new_tab("https://www.datacamp.com")
                speak("datacamp is open now")
                time.sleep(2)
            elif 'udacity' in statement1:
                webbrowser.open_new_tab("https://www.udacity.com")
                speak("udacity is open now")
                time.sleep(2)
            else:
                speak("Sorry we couldn't find your search!!!")
            time.sleep(3)

        elif 'jobs' in statement or 'job' in statement or 'job recommandation' in statement or 'work' in statement:
            platforms = [
                'linkedin', 'indeed', 'glassdoor', 'hackerrank', 'naukri',
                'intern shala'
            ]
            speak("Select a platform that you prefer:")
            print('\n'.join(platforms))
            statement1 = takeCommand().lower()
            if (statement1 == 0):
                continue
            if 'linkedIn' in statement1:
                webbrowser.open_new_tab("https://www.linkedin.com/jobs")
                speak("LinkedIn is open now")
                time.sleep(2)
            elif 'indeed' in statement1:
                webbrowser.open_new_tab("https://www.indeed.com/jobs")
                speak("Indeed is open now")
                time.sleep(2)
            elif 'glassdoor' in statement1:
                webbrowser.open_new_tab("https://www.glassdoor.com/jobs")
                speak("Glassdoor is open now")
                time.sleep(2)
            elif 'hackerrank' in statement1:
                webbrowser.open_new_tab(
                    "https://www.hackerrank.com/jobs/search")
                speak("HackerRank is open now")
                time.sleep(2)
            elif 'naukri' in statement1:
                webbrowser.open_new_tab("https://www.naukri.com/jobs")
                speak("Naukri is open now")
                time.sleep(2)
            elif 'intern shala' in statement:
                webbrowser.open_new_tab('internshala.com')
                speak('Intern Shala is open now')
                time.sleep(2)
            else:
                speak("Sorry we couldn't find your search!!!")
            time.sleep(3)
            
        elif 'movie ticket booking' in statement or 'movie booking' in statement or 'movie ticket' in statement:
            speak('Here are some top websites for ticket booking')
            webbrowser.open_new_tab("https://in.bookmyshow.com/")
            speak(" Book my show website is open now")
            time.sleep(2)

        elif 'train ticket booking' in statement or 'train booking' in statement or 'train ticket' in statement or 'train ticket' in statement:
            speak('Here are some top websites for tarin ticket booking')
            webbrowser.open_new_tab("https://www.easemytrip.com/railways/")
            speak(" Ease My trip website is open now, have a good journey !")
            time.sleep(2)

        elif 'bus ticket booking' in statement or 'bus booking' in statement or 'bus ticket' in statement:
            speak('Here are some top websites for bus ticket booking')
            webbrowser.open_new_tab("https://www.redbus.in")
            speak(" Red bus website is open now, have a good journey !")
            time.sleep(2)

        elif 'airplane ticket booking' in statement or 'airplane booking' in statement or 'airplane ticket' in statement:
            speak('Here are some top websites for airplane ticket booking')
            webbrowser.open_new_tab("https://www.goindigo.in")
            speak(" Indigo website is open now, have a good journey !")
            time.sleep(2)

        elif "hotel" in statement or "hotel booking" in statement:
            speak('Opening go ibibo .com')
            webbrowser.open_new_tab('goibibo.com/hotels')

        elif 'top engineering colleges in india' in statement or 'indian engineering college' in statement or 'engineering college' in statement:
            webbrowser.open_new_tab(
                "https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-india/44-2-0-0-0"
            )
            speak("Colleges as per NIRF Ranking are open on Shiksha website!")
            time.sleep(2)

        elif 'top medical colleges in india' in statement or 'indian medical college' in statement or 'medical college' in statement:
            speak('Here are some top Medical Colleges in India')
            webbrowser.open_new_tab(
                "https://medicine.careers360.com/colleges/ranking")
            speak("Colleges as per NIRF rankings are opened!")
            time.sleep(2)

        elif 'top science colleges in india' in statement or 'indian science college' in statement or 'science college' in statement:
            speak('Here are some top website for Science Colleges in India')
            webbrowser.open_new_tab(
                "https://collegedunia.com/science-colleges")
            speak(" College Dunia website is opened!")

        elif 'top law colleges in india' in statement or 'indian law college' in statement or 'law college' in statement:
            speak('Here are some top website for law Colleges in India')
            webbrowser.open_new_tab(
                "https://www.collegedekho.com/law-humanities/law-colleges-in-india/"
            )
            speak(" College Deko website is opened!")
            time.sleep(2)

        elif 'top research colleges in india' in statement or 'indian research college' in statement or 'research college' in statement:
            speak('Here are some top website for Research Colleges in India')
            webbrowser.open_new_tab(
                "https://www.biotecnika.org/2019/09/top-govt-research-institutes-present-in-india-top-10-list/"
            )
            speak("Biotechnika website is opened!")
            time.sleep(2)

        elif "weather" in statement:

            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            city_name = 'Bangalore'
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " + str(current_humidiy) +
                      "\n description  " + str(weather_description))
                speak(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " + str(current_humidiy) +
                      "\n description = " + str(weather_description))
        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
   

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'flip the coin' in statement or 'toss the coin' in statement or 'toss a coin' in statement:
            chances = ['Heads', 'Tails']
            coinRes = random.choice(chances)
            picLine = random.randint(1, 3)
            lines = [htLine1, htLine2, htLine3]
            lines[picLine - 1]()

        elif 'dice' in statement:
            num = random.randint(1, 6)
            speak("Your dice number is " + str(num))
        elif 'hostname and ip' in statement or 'host name and ip' in statement:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            print("Host-name: " + host_name)
            print("IP address: " + host_ip)
            speak("Your host name is" + host_name + "and ip address is" +
                  host_ip)

        elif 'on screen keyboard' in statement or 'onscreen keyboard' in statement:
            subprocess.run('osk', shell=True)

        elif 'cmd' in statement or 'command prompt' in statement or 'terminal' in statement:
            os.system("start cmd")
        elif 'generate qr code' in statement:
            img = qrcode.make("https://github.com/ikiran-dev")
            img.save("Kirab_qr_code.png")
            subprocess.run('Kiran_qr_code.png', shell='True')

        elif 'take a screenshot' in statement or 'capture screen' in statement:
            print('Taking screenshot in 3 second')
            speak('Taking screenshot in 3 second')
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save('screenshot.png')
            subprocess.run('screenshot.png', shell='True')
        elif 'volume up' in statement or 'increase volume' in statement:
            pyautogui.press('volumeup')

        elif 'volume down' in statement or 'decrease volume' in statement or 'lower the volume' in statement:
            pyautogui.press('volumedown') 

        elif 'volume mute' in statement or 'turn off the volume' in statement or 'mute' in statement:
            pyautogui.press('volumemute')
        elif 'ask' in statement:
            speak(
                'I can answer to computational and geographical questions and what question do you want to ask now'
            )
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'jokes' in statement or 'joke' in statement:
            joke = pyjokes.get_joke('en', 'all')
            print(joke)
            speak(joke)
        elif 'visual studio code' in statement or 'open code' in statement or 'code' in statement or 'visual code' in statement:
            os.startfile('code')
            speak('visual studio code is open now')
        elif 'what is my current location' in statement or 'what is my location' in statement or 'where am I' in statement:
            ip = "https://api.ipify.org/"
            ip_r = requests.get(ip).text

            geoip = "http://ip-api.com/json/" + ip_r
            geo_r = requests.get(geoip)
            geo_json = geo_r.json()

            print(
                f"Your current location is {geo_json['city']}, {geo_json['regionName']}, {geo_json['country']} {geo_json['zip']}"
            )
            speak(
                f"Your current location is {geo_json['city']}, {geo_json['regionName']}, {geo_json['country']} {geo_json['zip']}"
            )

        elif "notepad" in statement:
            speak("Opening Notepad")
            os.system("start Notepad")

        elif "outlook" in statement:
            speak("Opening Microsoft Outlook")
            os.system("start outlook")

        elif "word" in statement:
            speak("Opening Word")
            os.system("start winword")

        elif "paint" in statement:
            speak("Opening Paint")
            os.system("start mspaint")

        elif "excel" in statement:
            speak("Opening Excel")
            os.system("start excel")
        elif "start brave" in statement:
            speak("Opening brave")
            os.system("start brave")

        elif 'bravein incognito mode' in statement or 'chrome in incognito' in statement:
            speak("Opening brave in Incognito mode")
            os.system('start brave -incognito')

        elif "power point" in statement or "powerpoint" in statement or "ppt" in statement:
            speak("Opening ppt")
            os.system("start powerpnt")

        elif "edge" in statement:
            speak("Opening Microsoft Edge")
            os.system("start msedge")

        elif "snipping tool" in statement:
            speak("Opening Snipping Tool")
            os.system("start snippingtool")

        elif "show deleted files" in statement or "Recycle Bin" in statement or "Delete files" in statement or "search deleted files" in statement:
            speak("Opening Recycle Bin")
            os.system("start shell:RecycleBinFolder")

        elif "calculator" in statement:
            speak("Opening Calculator")
            os.system("start calc")
        elif 'travel' in statement or 'cab-booking' in statement or 'trip' in statement or 'ola' in statement or 'uber' in statement or 'Cab' in statement:
            speak('It seems you are interested in travelling somewhere'
                  'Want to Use Cab Sevices or Travel long distanced Trip')
            print("Cab Sevices or Travel long distanced Trip")
            travelask = takeCommand().lower()

            if "travel-long" or "distanced-trip" or "trip" in travelask:
                websites = ['makemytrip', 'booking', 'airbnb', 'Trivago']
                print('\n'.join(websites))
                speak("what do you want to open?")
                user_ip = takeCommand().lower().replace(' ', '')
                for website in websites:
                    if website in user_ip:
                        speak('Opening' + str(website))
                        webbrowser.open(website + '.com')

            elif "cab-services" or "cab" in travelask:
                print("Want to use Ola or Uber")
                speak('Want to use Ola or Uber')
                travelask2 = takeCommand().lower()
                if "ola" in travelask2:
                    webbrowser.open_new_tab("https://www.olacabs.com")
                    speak('Ola website is open now')
                elif "uber" in travelask2:
                    webbrowser.open_new_tab("https://www.uber.com/in/en/")

                    speak('Uber website is open now')

            elif 'search' in statement or 'defination' in statement:
                speak('I guess you want to search defination'
                      'What do you want to search about sir')
                print("What do you want to search about sir")
                definationask = takeCommand().lower()
                finalmeaning = defination(definationask)
                print(finalmeaning)
                speak(finalmeaning)

                speak('Uber website is open now')

        elif 'system' in statement or 'system details' in statement or 'hardware' in statement:
            plat_det = platform.uname()
            print('User : ', plat_det.node)
            print('System :', plat_det.system, plat_det.release,
                  plat_det.version)
            print('Machine :', plat_det.machine)
            print('Processor : ', plat_det.processor)
            speak(plat_det.node)
            speak(plat_det.system)
            speak(plat_det.release)
            speak(plat_det.version)
            speak(plat_det.machine)
            speak(plat_det.processor)
