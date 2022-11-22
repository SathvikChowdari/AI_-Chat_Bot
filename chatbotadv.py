import speech_recognition as sr
from gtts import gTTS
import transformers
import os
import time
import datetime
import pywhatkit as pwt
import time
import numpy as np
import webbrowser
from googlesearch import search
class ChatBot():
    def __init__(self,name):
        print("----- Starting up",name,"----")
        self.name=name
    def speech_to_text(self):
        recognizer=sr.Recognizer()
        with sr.Microphone() as mic:
            time.sleep(5)
            print("Listening...")
            audio=recognizer.listen(mic)
            self.text="ERROR"
            
        try:
            self.text=recognizer.recognize_google(audio)
            print("Me:",self.text)
        except:
            print("Me : ERROR" )
    def text_to_speech(self,text,yt):
        print("Jarvis:",text)
        
        speaker=gTTS(text=text,lang="en",slow=False)
        speaker.save("res.mp3")
        os.system("start res.mp3") 
        if any(i in text for i in ["youtube"]):
            pwt.playonyt(yt)
        elif any(i in text for i in ["google"]):    
            for j in search(yt,tld="co.in",num=1,stop=1,pause=2):
                l=j
            webbrowser.open(l)
        
        
    def wake_up(self,text):
        return True if self.name in text.lower() else False
    def action_time(self):
        
        return datetime.datetime.now().time().strftime('%H:%M')
if __name__=="__main__":
    ai=ChatBot(name="jarvis")
    nlp=transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
   
    os.environ["TOKENIZERS_PARALLELISM"]="true"

    ex=True
    y="Error"
    l=''
    while ex:
        ai.speech_to_text()
        if ai.wake_up(ai.text) is True:
            res="Hello I am Jarvis the AI,what can I do for you?"
        elif "time" in ai.text:
            res=ai.action_time()
        elif any(i in ai.text for i in ["thank","thanks"]):
            res=np.random.choice(["you're welcome!","aytime!","no problem!","cool!","I'm here if you need me!","mention not"])
        elif any(i in ai.text for i in {"exit","close"}):
            res=np.random.choice(["Have a good day","closing jarvis","Goodbye"])
            print("-----Closing down-----")            
            ex=False
        elif any(i in ai.text for i in ["play"] ):
            y=ai.text
            res="redirecting to youtube"  
        elif any(i in ai.text for i in ["search"] ):
            y=ai.text
            res="redirecting to google"       
        else:
            if ai.text=="ERROR":
                res="Sorry, come again?"
            else:
                chat=nlp(transformers.Conversation(ai.text),pad_token_id=50256)
                res=str(chat)
                res=res[res.find("bot >> ")+6:].strip()
                
                
        ai.text_to_speech(res,y)
                    