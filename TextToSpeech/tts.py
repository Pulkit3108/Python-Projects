import pyttsx3 as pt
import speech_recognition as sr
print('1. Convert Text To Speech')
print('2. Convert Speech To Text')
print('Enter Your Choice :',end=' ')
c=int(input())
if(c==1):
    s=input('Enter Text : ')
    a=pt.init()
    try:
        a.say(s)
        a.runAndWait()
        print('Speech Done....') 
    except Exception as e:
        print("Error : " + str(e))
elif(c==2):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Please Speak....')
        audio=r.listen(source)
        p=r.recognize_google(audio)
        try:
            print("Text From Speech : " + r.recognize_google(audio))
        except Exception as e:
            print("Error : " + str(e))
else:
    print('Wrong Choice')
