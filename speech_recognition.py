import speech_recognition as sr
r=sr.recognizer()
with sr.microphone() as source:
    print('Speak anything:')
    a=r.listen(source)
    try:
     text=r.recognize_google(a)
     print('you said:{}'.format(text))
    except:
        print("Didn't recognize the voice." )

