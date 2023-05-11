import speech_recognition as sr
import pyaudio
import openai


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


def main():
    init_rec = sr.Recognizer()
    openai.api_key = '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'
    with sr.Microphone() as source:
        while True:
            try:
                audio_data = init_rec.record(source, duration=5)
                text = init_rec.recognize_google(audio_data)
                print(text)
                try:
                    answer = query_question(
                        "You are a Japanese proffesor at the University of Michigan, translate the following sentence into Japanese: " + text)
                    print(answer)
                except:
                    print("Error")
            except:
                print("error")


if __name__ == "__main__":
    main()