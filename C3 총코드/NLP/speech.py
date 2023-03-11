#!/usr/bin/env python
# coding: utf-8

# In[35]:


#!/usr/bin/env python3
# Requires PyAudio and PySpeech.http://localhost:8890/edit/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C/sinju/speech.py#

def STT_main():
    import speech_recognition as sr
    # Record Audio 
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        STT1=r.recognize_google(audio,language="ko")
       # print(STT)
    # Seech recognition using Google Speech Recognition
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)
    except sr.UnknownValueError:
        print("다시 말하세요")
    except sr.RequestError as e:
        print("잘못된 입력; {0}".format(e))
        
    return STT1


