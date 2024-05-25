import pyttsx3
import speech_recognition as sr

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, couldn't request results from Google Speech Recognition service.")
        return ""

def main():
    choice = input("Enter 't' for text to speech, 'v' for voice to text: ")
    if choice == 't':
        text = input("Enter text to translate to speech: ")
        text_to_speech(text)
    elif choice == 'v':
        text = speech_to_text()
        if text:
            print("You said:", text)
            text_to_speech(text)
        else:
            print("No speech detected.")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
