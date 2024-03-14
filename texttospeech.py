import pyttsx3
text_speech = pyttsx3.init()
rate = text_speech.getProperty('rate')
text_speech.setProperty('rate', rate - 10)  # Decrease the rate by 10
answer = input("What do you want to convert to speech: ")
text_speech.say(answer)
text_speech.runAndWait()
