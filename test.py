import whisper

model = whisper.load_model("base")
result = model.transcribe("2.wav")
print(result["text"])