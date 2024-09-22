import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import time

engine = pyttsx3.init()

nombre_asistente = "Saturno"

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

recognizer = sr.Recognizer()

def escuchar_comando():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        
        try:
            comando = recognizer.recognize_google(audio, language='es-ES')
            print(f"Comando recibido: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            hablar("Lo siento, no entendí el comando.")
            print("No entendí el comando")
        except sr.RequestError:
            hablar("Error al conectarse con el servicio de reconocimiento.")
            print("Error al conectarse con el servicio de reconocimiento.")

def decir_hora_actual():
    hora_actual = datetime.now().strftime("%H:%M:%S")
    hablar(f"La hora actual es: {hora_actual}")
    print(f"La hora actual es: {hora_actual}")

def pedir_busqueda_wikipedia():
    hablar("¿Qué quieres que busque en Wikipedia?")
    print("¿Qué quieres que busque en Wikipedia?")
    comando_busqueda = escuchar_comando()
    return comando_busqueda

def ejecutar_comando(comando):
    if "abre youtube" in comando:
        buscar = comando.replace("abre youtube", "").strip()
        if buscar:
            url_busqueda = f"https://www.youtube.com/results?search_query={buscar.replace(' ', '+')}"
            webbrowser.open(url_busqueda)
            hablar(f"Buscando {buscar} en YouTube")
            print(f"Buscando {buscar} en YouTube...")
        else:
            webbrowser.open("https://www.youtube.com")
            hablar("Abriendo YouTube")
            print("Abriendo YouTube...")
        
    elif "dime la hora" in comando:
        decir_hora_actual()
        
    elif "abre wikipedia" in comando:
        buscar = comando.replace("abre wikipedia", "").strip()
        if not buscar:
            buscar = pedir_busqueda_wikipedia()
        
        if buscar:
            url_busqueda = f"https://es.wikipedia.org/wiki/{buscar.replace(' ', '_')}"
            webbrowser.open(url_busqueda)
            hablar(f"Buscando {buscar} en Wikipedia")
            print(f"Buscando {buscar} en Wikipedia...")
        else:
            hablar("Lo siento, no entendí lo que querías buscar.")
            print("No se especificó búsqueda.")
        
    elif "chao" in comando:
        hablar("Chao, espero que necesites mi ayuda nuevamente")
        print("Chao, espero que necesites mi ayuda nuevamente")
        return False  
    
    else:
        hablar("Lo siento, no reconozco ese comando.")
        print("Comando no reconocido")
    return True  

def iniciar_asistente():
   
    hablar(f"Hola, soy {nombre_asistente}. ¿En qué te puedo ayudar?")
    print(f"Hola, soy {nombre_asistente}. ¿En qué te puedo ayudar?")
    
    time.sleep(2)
   
    while True:
        comando = escuchar_comando()
        if comando:
            continuar = ejecutar_comando(comando)
            if not continuar:  
                break

iniciar_asistente()

