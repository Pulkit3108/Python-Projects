import os
from gtts import gTTS
from playsound import playsound
a=input('Enter Text : ')
file_path=input('Enter File Path : ')
while not os.path.exists(file_path) or os.path.getsize(file_path)==0:
    try:
        tts=gTTS(text=a, lang='en', slow=False)
        tts.save(file_path)
    except Exception as e:
        print(e)
playsound(file_path)
