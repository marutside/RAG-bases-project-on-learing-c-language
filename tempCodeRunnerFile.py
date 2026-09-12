import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import whisper 
import json

model = whisper.load_model("base")
result = model.transcribe(audio = "audio/c language video1.mp3", task = "translate" , word_timestamps = False)

print(result["text"])
with open("output.json", "w") as f:
    json.dump(result, f)
