import speech_recognition as speech_recog

#Funzione che ci permette di esportare la funzione
def speech():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google_cloud(audio, language="it-IT")
    
#Script
mic = speech_recog.Microphone()
recog = speech_recog.Recognizer
with mic as audio_file:
    print("Si prega di parlare")

    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)

    print("Conversione della voce in testo...")
    print("Hai detto: " + recog.recognize_google_cloud(audio, language="it-IT"))