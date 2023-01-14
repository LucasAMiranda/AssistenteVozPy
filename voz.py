import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Olá, Bom dia!")
        print("Olá, Bom dia!")
    elif hour >= 12 and hour < 18:
        speak("Olá, Boa Tarde!")
        print("Olá, Boa Tarde!")
    else:
        speak("Olá, Boa noite!")
        print("Olá, Boa noite!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Carregando...")
        audio = r.listen(source)

        try:
            statament = r.recognize_google(audio, language='pt-br')
            print(f"user said: {statament}\n ")
        
        except Exception as e:
            speak("Perdoe-me, por favor tente novamente!")
            return "None"
        return statament

print("Carregando sua Intelgência artificial assitente pessoal Robot7")
speak("Carregando sua Intelgência artificial assitente pessoal Robot7")
wishMe()

if __name__ == "__main__":

    while True: 
        speak("Diga-me como pode , eu ajudar você agora!")
        statament = takeCommand().lower()
        if statament == 0:
            continue

        if "tchau" in statament or "ok tchau" in statament or "stop" in statament:
            speak("Seu assistente pessoal Robot7 é desligado, Tchau!")
            print("Seu assistente pessoal Robot7 é desligado, Tchau!")
            break
