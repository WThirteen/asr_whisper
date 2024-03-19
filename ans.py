import pyttsx3
import speech_recognition as sr
import datetime
import os
import wave
import whisper


# # large
# model = whisper.load_model("large")

# medium
model = whisper.load_model("medium")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def save_as_wav(audio, output_file_path):
    with wave.open(output_file_path, 'wb') as wav_file:
        wav_file.setnchannels(1)  # 单声道
        wav_file.setsampwidth(2)  # 16位PCM编码
        wav_file.setframerate(44100)  # 采样率为44.1kHz
        wav_file.writeframes(audio.frame_data)



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("请说...")
        r.pause_threshold = 1
        audio = r.listen(source)

        output_file_path = "temp_file.wav"
        save_as_wav(audio, output_file_path)

    try:
        print("识别中...")

        # 使用模型
        result = model.transcribe("temp_file.wav", language="chinese")
        query = result['text']
        print(f"输入对话：{query}\n")

    except Exception as e:
        print(e)
        print("请再说一遍...")
        speak("请再说一遍...")
        return "None"
    return query

if __name__ == "__main__":
    print("start:")
    query = takeCommand().lower()
    os.remove("temp_file.wav")