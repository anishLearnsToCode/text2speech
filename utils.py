import pyttsx3

ENGINE = pyttsx3.init('sapi5')
VOICES = ENGINE.getProperty('voices')
ENGINE.setProperty('voice', VOICES[1].id)


def speak(text: str) -> None:
    ENGINE.say(text)
    ENGINE.runAndWait()
