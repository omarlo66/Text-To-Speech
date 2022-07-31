from googletts import TTS
Text = input("Enter Text: ")
Language = input("Enter Language name:  (eg. English, Arabic, French, etc.) ")
FileName = input("Enter the file name: ")
print('Please Wait...')
TTS.Save(Text=Text,language=Language,filename=FileName)
print("Saved")