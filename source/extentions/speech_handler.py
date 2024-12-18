import speech_recognition as sr
from .sentence_interpreter import get_token_lemmas
import threading
import queue

def __listen(result_queue):
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print("Say something")
        audio = microphone.listen(source, timeout=100, phrase_time_limit=5)
    
    try:
        phrase = microphone.recognize_google(audio) ## <-- This is right, for some reason its giving an error 
        result_queue.put(get_token_lemmas(phrase.lower()))
    except sr.UnknownValueError:
        print("I couldn't understand what you said")
        result_queue.put([])
    
def listen():
    results_queue = queue.Queue()
    listening_thread = threading.Thread(target=__listen(results_queue))
    listening_thread.start()
    return results_queue.get()
    
if __name__ == "__main__":
    print(listen())