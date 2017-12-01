# coding: utf-8
import wx
import os
import wikipedia
import time 
import webbrowser 
import winshell
import json
import requests
import ctypes 
import random
import urllib
import ssl
from bs4 import BeautifulSoup
import win32com.client as wicl
from urllib.request import urlopen
import speech_recognition as sr
import requests
requests.packages.urllib3.disable_warnings()
try:
        _create_unverified_https_context=ssl._create_unverified_context
except 'AttributeError':
        pass
else:
        ssl._create_default_https_context=_create_unverified_https_context
        
headers = {'''user-agent':'Chrome/53.0.2785.143'''}
speak=wicl.Dispatch("SAPI.SpVoice")
# Creating the graphical user interface
i=0
class MyFrame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self,None,pos=wx.DefaultPosition, size=wx.Size(400,100),style=wx.MINIMIZE_BOX| wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, title="BENJI")
            panel=wx.Panel(self)
            ico= wx.Icon('benji1.ico',wx.BITMAP_TYPE_ICO)
            self.SetIcon(ico)
            my_sizer=wx.BoxSizer(wx.VERTICAL)
            lbl=wx.StaticText(panel,label="Hello Agent! How can I help you")
            my_sizer.Add(lbl,0,wx.ALL,6)
            self.txt=wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER,size=(400,40))
            self.txt.SetFocus()
            self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
            my_sizer.Add(self.txt,0,wx.ALL,6)
            panel.SetSizer(my_sizer)
            self.Show()
            speak.Speak('''Hi Agent! BENJI at your service''')
     
        def OnEnter(self,event):
            put=self.txt.GetValue()
            #put=put.lower()
            link=put.split()
            if put=='':
                m=sr.Recognizer()
                with sr.Microphone() as srm:
                    audio=m.listen(srm)
                try:
                    self.txt.SetValue("Listening...")
                    put=m.recognize_google(audio)
                    put=put.lower()
                    link=put.split()
                    self.txt.SetValue(put)
                except sr.UnknownValueError:
                    print("BENJI could not understand audio")
                except sr.RequestError as RE:
                    print("could not request results from IMF archives;{0}".format(RE))
                except:
                    print("Unknown error occurred, while taking speech input!")
         
         #Play song on  Youtube
            if put.startswith('play '):
                try:
                    link = '+'.join(link[1:])
#                    print(link)
                    say = link.replace('+', ' ')
                    url = 'https://www.youtube.com/results?search_query='+link
#                    webbrowser.open('https://www.youtube.com'+link)
                    fhand=urllib.request.urlopen(url).read()
                    soup = BeautifulSoup(fhand, "html.parser")
                    songs = soup.findAll('div', {'class': 'yt-lockup-video'})
                    hit = songs[0].find('a')['href']
#                    print(hit)
                    speak.Speak("playing "+say)
                    webbrowser.open('https://www.youtube.com'+hit)
                except:
                    print('Sorry Ethan. Looks like its not working!')
        #Who are you?
            elif put.startswith('who are you '):
                try: 
                    speak.Speak("I am BENJI, a digital assistant declassified for civilian use. Previously I was used by the Impossible Missions Force")
                except:
                    print('Error. Try reading the ReadMe to know about me!')
        #Open a webpage
            elif put.startswith('open '):
                try:
                    speak.Speak("opening "+link[1])
                    webbrowser.open('http://www.'+link[1]+'.com')
                except:
                    print('Sorry Ethan,unable to access it. Cannot hack either-IMF protocol!')
        #Google search
            elif put.startswith('search '):
                try:
                    link='+'.join(link[1:])
                    say=link.replace('+',' ')
                    speak.Speak("searching google for "+say)
                    webbrowser.open('https://www.google.com/search?q='+link)
                except:
                    print('Nope, this is not working.')
        #Wikipedia
            elif put.startswith('wiki '):
                try:
                    link='+'.join(link[1:])
                    say=link.replace('+',' ')
                    speak.Speak("Wikipedia search for"+say)
                    webbrowser.open('https://en.wikipedia.org/wiki/'+link)
                except:
                	print('Wikipedia could not either find the article or your Third-world connection is unstable')
       #Lock the device 
            elif put.startswith('secure '):
                try:
                        speak.Speak("locking the device")
                        ctypes.windll.user32.LockWorkStation()
                except :
                        print('Cannot lock device')  

        #News of various press agencies
            elif put.startswith('aljazeera '):
                try:
                    jsonObj=urlopen('''  https://newsapi.org/v1/articles?source=al-jazeera-english&sortBy=latest&apiKey=571863193daf421082a8666fe4b666f3''')
                    data=json.load(jsonObj)
                    i+=1
                    speak.Speak('''Our agents from Al-Jazeera report this''')
                    print('''  =====Al Jazeera====='''+'\n')
                    for item in data['articles']:
                        print(str(i)+'. '+item['title']+'\n')
                        print(item['description']+'\n')
                        i+=1
                except:
                    print('Qatari agents have refused to share this intel, Ethan')
            elif put.startswith('bbc '):
                try:
                    jsonObj=urlopen('''https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=571863193daf421082a8666fe4b666f3''')
                    data=json.load(jsonObj)
                    i+=1
                    speak.Speak('''Our agents from BBC report this''')
                    print('''  =====BBC====='''+'\n')
                    for item in data['articles']:
                        print(str(i)+'. '+item['title']+'\n')
                        print(item['description']+'\n')
                        i+=1
                except:
                    print('MI6 is going crazy! Not allowing this!')
            elif put.startswith('cricket '):
                try:
                    jsonObj=urlopen(''' https://newsapi.org/v1/articles?source=espn-cric-info&sortBy=latest&apiKey=571863193daf421082a8666fe4b666f3''')
                    data=json.load(jsonObj)
                    i+=1
                    speak.Speak('''Cricket news are''')
                    print('''  =====ESPN====='''+'\n')
                    for item in data['articles']:
                        print(str(i)+'. '+item['title']+'\n')
                        print(item['description']+'\n')
                        i+=1
                except:
                    print('Connection not secure')
            elif put.startswith('news '):
                try:
                    jsonObj=urlopen('''https://newsapi.org/v1/articles?source=the-hindu&sortBy=latest&apiKey=571863193daf421082a8666fe4b666f3''')
                    data=json.load(jsonObj)
                    i+=1
                    speak.Speak('''Some news from The Hindu''')
                    print('''  =====The Hindu====='''+'\n')
                    for item in data['articles']:
                        print(str(i)+'. '+item['title']+'\n')
                        print(item['description']+'\n')
                        i+=1
                except:
                    print('R&A W is blocking our reports, Ethan. Sorry! ')
            # Finding files in pc
            elif put.startswith('lookfor '):
                try:
                    name=link[1]
                    path=link[2]
                    result=[]
                    for root, dirs, files in os.walk(path):
                        if name in files:
                            result.append(os.path.join(root, name))
                    for item in result:
                        print(item+'\n')
                except:
                    print("Error")
                os.close()

    #Trigger the GUI. Light the fuse!
if __name__=="__main__":
    app = wx.App(True)
    frame= MyFrame()
    app.MainLoop()




