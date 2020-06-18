import datetime
from gtts import gTTS
import os
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import pyautogui
import psutil
import pyjokes


class VoiceAssistant:
    '''A simple voice assistant.'''

    def __init__(self, name, email_address, email_password,
                 browser_path, music_dir):
        self.name = name
        self.email_address = email_address
        self.email_password = email_password
        self.browser_path = browser_path
        self.music_dir = music_dir


    def run(self):
        '''Start the work of assistant.'''
        self.greet()
        while True:
            query = self.listen()

            if query is None:
                continue
            else:
                query = query.lower()

            if 'time' in query:
                self.speak_current_time()
            elif 'date' in query:
                self.speak_current_date()
            elif 'wikipedia' in query:
                self.search_in_wiki(query)
            elif 'email' in query:
                self.send_email()
            elif 'browser' in query:
                self.search_in_browser()
            elif 'logout' in query:
                os.system('shutdown -1')
            elif 'shutdown' in query:
                os.system('shutdown /s /t 1')
            elif 'restart' in query:
                os.system('shutdown /r /t 1')
            elif 'music' in query:
                self.play_music()
            elif 'remember' in query:
                self.remember_something()
            elif 'what do you know' in query:
                self.recollect_something()
            elif 'screenshot' in query:
                self.make_screenshot()
            elif 'cpu' in query:
                self.speak_cpu_usage()
            elif 'battery' in query:
                self.speak_battery_remaining()
            elif 'joke' in query:
                self.joke()
            elif 'offline' in query:
                self.speak('As you wish, sir. Good luck!')
                quit()
            else:
                self.speak('Repeat please!')


    def speak(self, message):
        '''Speak a message.'''
        speech = gTTS(text=str(message), lang='en', slow=False)
        speech.save('tmp.mp3')
        os.system('mpg123 -q tmp.mp3')
        os.remove('tmp.mp3')


    def listen(self):
        '''Listen to user.'''
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f'Query: {query}')
        except Exception as e:
            if str(e) != '':
                print(f'Error: {e}')

            return None

        return query


    def greet(self):
        '''Greet the user.'''
        hour = datetime.datetime.now().hour
        if 6 <= hour < 12:
            self.speak('Good morning, sir! Welcome back!')
        elif 12 <= hour < 18:
            self.speak('Good afternoon, sir! Welcome back!')
        elif 18 <= hour < 24:
            self.speak('Good evening, sir! Welcome back!')
        else:
            self.speak('Good night, sir! Welcome back!')

        self.speak(f'{self.name} at your service, please tell me how can I help you?')


    def speak_current_time(self):
        '''Speak the current time.'''
        time = datetime.datetime.now().strftime('%I:%M:%S')
        self.speak(f'The current time is {time}')


    def speak_current_date(self):
        '''Speak the current date.'''
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        day = int(datetime.datetime.now().day)
        self.speak(f'The current date is {day}/{month}/{year}')


    def search_in_wiki(self, query):
        '''Search something in Wikipedia.'''
        self.speak('What should I search?')
        what_to_search = self.listen().lower()
        self.speak('Searching...')
        result = wikipedia.summary(what_to_search, sentences=2)
        self.speak(result)


    def send_email(self):
        '''Send an email.'''
        try:
            self.speak('What should I say?')
            content = self.listen()
            self.speak('Enter the destination email:')
            to = input()

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.email_address, self.email_password)
            server.sendmail(self.email, to, content)
            server.close()

            self.speak('Email has been sent!')
        except Exception as e:
            print(f'Error: {e}')
            self.speak('Unable to send the email!')


    def search_in_browser(self):
        '''Search something in browser.'''
        self.speak('What should I search?')
        what_to_search = self.listen().lower()
        self.speak('Searching...')
        wb.get(self.browser_path).open_new_tab(what_to_search)


    def play_music(self):
        '''Start to play music.'''
        music = os.listdir(self.music_dir)
        os.startfile(os.path.join(self.music_dir, music[0]))


    def remember_something(self):
        '''Save some info to a file.'''
        self.speak('What should I remember?')
        what_to_remember = self.listen()
        self.speak(f'You said me to remember that {what_to_remember}')
        with open('data.txt', 'w') as remember:
            remember.write(what_to_remember)

        self.speak('Done!')


    def recollect_something(self):
        '''Speak previously saved info.'''
        with open('data.txt', 'r') as recollection:
            self.speak(f'You said me to remember that {recollection.read()}')


    def make_screenshot(self):
        '''Make a screenshot.'''
        img = pyautogui.screenshot()
        img.save('screenshot.png')
        self.speak('Done!')


    def speak_cpu_usage(self):
        '''Speak the current CPU usage.'''
        usage = str(psutil.cpu_percent())
        self.speak(f'CPU is at {usage}')


    def speak_battery_remaining(self):
        '''Speak how much battery is left.'''
        battery = psutil.sensors_battery()
        self.speak(f'Battery is at {round(battery.percent)}%')


    def joke(self):
        '''Speak a joke.'''
        joke = pyjokes.get_joke()
        self.speak(joke)


if __name__ == '__main__':
    jarvis = VoiceAssistant('Jarvis', 'example@gmail.com', '123',
                            'opera', 'Music')
    jarvis.run()
