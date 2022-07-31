#!/user/bin/python
# -*- coding: utf-8 -*-
import os
import random
import gtts
from pygame import mixer

SayDir = os.path.dirname(os.path.realpath(__file__)) + '\say/'.replace('/','\\')
print(SayDir)

class Functions:
    def IDGenerator():
        F = random.randint(1000, 9999)
        A = random.randint(0, 25)
        AList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        return f'{AList[A]}{F}.mp3'

    def DeleteLastFiles():
        try:
            os.chdir(SayDir)
            for file in open('DeleteList.txt','r').readlines():
                F = file.replace('\n','')
                try:
                    os.remove(F)
                except:
                    if os.path.exists(F):
                        os.remove(F)
                    else:
                        pass
                open('DeleteList.txt','w').truncate()
        except Exception as e:
            print(e)
            pass
class TTS:
    def Say(Text,Language):
        try:
            os.mkdir(SayDir)
        except:
            Functions.DeleteLastFiles()
        File = Functions.IDGenerator()
        Lang = Convert.Language(Language)
        tts = gtts.gTTS(lang=Lang, text=Text)
        os.chdir(SayDir)
        tts.save(File)
        print("Saved")
        Sound = mixer.init()
        mixer.music.load(File)
        mixer.music.play()
        print("Played") 
        while mixer.music.get_busy():
            continue
        open('DeleteList.txt','a').write(File + '\n')
        open('DeleteList.txt','w').truncate()

    def LangList():
        F = gtts.tts.tts_langs()
        AllValues = F.values()
        AllKeys = F.keys()
        Values = []
        Keys = []
        for i in AllValues:
            Values.append(i)
        for i in AllKeys:
            Keys.append(i)
        return Values
    def Save(Text,language,filename):
        Lang = Convert.Language(language)
        tts = gtts.gTTS(lang=Lang, text=Text)
        tts.save(str(filename).join('.mp3'))
        print("Saved")

class Convert:
    def Language(lang):
        F = gtts.tts.tts_langs()
        AllValues = F.values()
        AllKeys = F.keys()
        Values = []
        Keys = []
        for i in AllValues:
            Values.append(i)
        for i in AllKeys:
            Keys.append(i)
        for i in range(len(Values)):
            if Values[i] == lang:
                return Keys[i]
            
