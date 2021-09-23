import speech_recognition as sr
def recog_audio():
    r = sr.Recognizer()
    r.pause_threshold = 2.5

    with sr.Microphone() as source:
        print('Say something')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            return voice_data.lower()
        
        # let user choose whether to say something again 
        except sr.UnknownValueError:
            # TODO: when this error happend redirect the user to speak in microphone again
            print("Google SR engine could not understand the audio. Say again please ...")
            #recog_audio()
        except sr.RequestError as e:
            print("Web request error")