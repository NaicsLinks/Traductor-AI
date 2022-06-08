from gtts import gTTS
from playsound import playsound
from scipy.io.wavfile import write
import sounddevice as sd 
import speech_recognition as sr
import soundfile as sf

def text2voice(texts):
    salida = gTTS(text=texts, lang="es-us", slow=False)
    salida.save("zioVoice.mp3")
    playsound("zioVoice.mp3")

def voice2text():
    frec = 44100
    timegrap = 4
    print("rec on speack")
    record = sd.rec(int(timegrap*frec), samplerate=frec, channels=2)
    sd.wait()

    print("i got it my lord")

    write("voice.wav", frec, record)

    data, samplerate = sf.read('voice.wav')
    sf.write('voice.wav', data, samplerate, subtype='PCM_16')

    r = sr.Recognizer()
    audioFile = sr.AudioFile('voice.wav')
    with audioFile as source:
        audio = r.record(source)
    try:
        val = r.recognize_google(audio, language='es-PA')
    except Exception as e:
        val = ""
        print(e)
    return str(val)

if __name__ == '__main__':
    pass