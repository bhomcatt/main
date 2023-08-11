from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess

root = Tk()

root.geometry("600x600")
root.title("ehfuwihipañ")

label = Label(text="alexa pero mal hecho", font=("Bahnshcrift", 17,"bold"))
label.place(relx=0.5,rely=0.5,anchor=CENTER)

tts=pyttsx3.init()

def speak(audio):
    tts.say(audio)
    tts.runAndWait()

def r_audio():
    speech_recognisor = sr.Recognizer()
    speak("h")
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data= speech_recognisor.recognize_google(audio, language='es-mx')
        except sr.UnknownValueError:
            print("repitelo")
            speak("El misil sabe dónde está en todo momento. Lo sabe porque sabe dónde no está. Restando donde está de donde no está, o donde no está de donde está (lo que sea mayor), se obtiene una diferencia o desviación. El subsistema de guía usa desviaciones para generar comandos correctivos para conducir el misil desde una posición donde está a una posición donde no está, y llegando a una posición donde no estaba, ahora está. En consecuencia, la posición donde está, ahora es la posición que no estaba, y se sigue que la posición que estaba, ahora es la posición que no está.")
            speak("En el caso de que la posición en la que está no sea la posición en la que no estaba, el sistema ha adquirido una variación, siendo la variación la diferencia entre donde está el misil y donde no estaba. Si se considera que la variación es un factor importante, la GEA también puede corregirla. Sin embargo, el misil también debe saber dónde estaba.")
            speak("El escenario de la computadora de guía de misiles funciona de la siguiente manera. Debido a que una variación ha modificado parte de la información que ha obtenido el misil, no está seguro de dónde está. Sin embargo, está seguro de dónde no está, dentro de lo razonable, y sabe dónde estaba. Ahora resta donde debería estar de donde no estaba, o viceversa, y diferenciando esto de la suma algebraica de donde no debería estar y donde estaba, es capaz de obtener la desviación y su variación. , que se llama error.")
        respond(voice_data)

def respond(voice_data):
    print(voice_data)
    if "nombre" in voice_data:
        speak("mi nombre es patapatapatapatapatapatapatapatapatapatapatapatapatapon")
        print("mi nomre es mini alexa")

    if "hora" in voice_data:
        speak("la hora es")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)

    if "Buscar" in voice_data:
        speak("abriendo google")
        print("abriendo google")
        webbrowser.get().open("https://www.google.com.mx/search?q=do+a+barrel+roll&sxsrf=AB5stBgiE6X_x0bRvyj-1mXzyW7dnIVbiA%3A1691714284722&source=hp&ei=7ILVZPz4J-jQkPIP5PSOiAY&iflsig=AD69kcEAAAAAZNWQ_Ib5troa92MCJ7vDScxWTKdHHvHY&ved=0ahUKEwj8nv7nrtOAAxVoKEQIHWS6A2EQ4dUDCAk&uact=5&oq=do+a+barrel+roll&gs_lp=Egdnd3Mtd2l6IhBkbyBhIGJhcnJlbCByb2xsMgUQLhiABDIFEAAYgAQyBRAAGIAEMggQABiABBjLATIFEAAYgAQyBRAAGIAEMggQABiABBjLATIIEAAYgAQYywEyBRAAGIAEMgUQABiABEiNLFDSBFiYKnABeACQAQCYAacBoAHJDqoBBDIuMTS4AQPIAQD4AQGoAgrCAgcQIxjqAhgnwgIHEC4Y6gIYJ8ICBBAjGCfCAgcQIxiKBRgnwgILEAAYgAQYsQMYgwHCAgsQLhiABBjHARivAcICERAuGIAEGLEDGIMBGMcBGNEDwgIHEC4YigUYJ8ICDhAuGMcBGLEDGNEDGIAEwgIIEAAYgAQYsQPCAgsQLhiABBixAxiDAcICCBAuGIAEGMsB&sclient=gws-wiz")

    if "videos" in voice_data:
        speak("abriendo youtube")
        print("abriendo youtube")
        webbrowser.get().open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    if "Hola" in voice_data:
        speak("h. o. l. a.")
        print("hola")

r_audio()

btn = Button(text="iniciar", font=("Bahnshcrift", 17,"bold"), command=r_audio)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

root.mainloop()