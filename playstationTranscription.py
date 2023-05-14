from flask import Flask, render_template
from threading import Thread
import speech_recognition as sr
import pyaudio
import openai

transcribedTextValue = "This is example transcribed text of what could be said by a person during a PlayStation party chat "
translatedTextValue = "これはPlayStationパーティーチャットで一人が話している可能性のある会話のためのエントリー翻訳テキストです"

app = Flask(__name__)

def query_question(question):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=100,
        n=1,
        stop=None
    )
    answer = response.choices[0].text.strip()
    return answer

def speachRecognizer():
    global transcribedTextValue, translatedTextValue

    init_rec = sr.Recognizer()
    openai.api_key = '#'
    with sr.Microphone() as source:
        while True:
            try:
                audio_data = init_rec.record(source, duration=5)
                text = init_rec.recognize_google(audio_data)
                print(text)
                transcribedTextValue = text
                try:
                    answer = query_question(
                        "You are hyper-fluent in Japanese, translate the following English sentence into Japanese: " + text)
                    print(answer)
                    translatedTextValue = answer
                except:
                    print("Translation Error")
            except:
                print("Transcription Error")

thread = Thread(target=speachRecognizer)
thread.start()

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/transcribedText',methods=['GET'])
def transcribedText():
    return transcribedTextValue 

@app.route('/translatedText',methods=['GET'])
def translatedText():
    return translatedTextValue

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
