import whisper
import json
import os 


# model = whisper.load_model("large-v2")

audio = os.listdir("audio")

for audio in audios:
    print(audio)
    number = audio.split("_")[0]
    title = 