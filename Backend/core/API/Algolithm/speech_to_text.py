# import speech_recognition as sr  #Google ASR
# def speech_to_thai(wav):
#     Transcription = ""
#     r = sr.Recognizer()
#     with sr.WavFile(wav) as source:              # ใช้ "test.wav"  เป็นแหล่งให้ข้อมูลเสียง
#         audio = r.record(source)                        # ส่งข้อมูลเสียงจากไฟล์
#     try:
#         Transcription = r.recognize_google(audio,language = "th-TH")
#     except :    
#         print("Unknown")
    
#     print("Transcription: " + Transcription )   # แสดงข้อความจากเสียงด้วย Google Speech Recognition
#     return Transcription


from transformers import pipeline
import torch

MODEL_NAME = "biodatlab/whisper-medium-th-combined-v2"  # specify the model name
lang = "th"  

device = 0 if torch.cuda.is_available() else "cpu"
pipe = pipeline(task="automatic-speech-recognition",model=MODEL_NAME,device=device)

def speech_to_thai(wav):
  

    pipe.model.config.forced_decoder_ids = pipe.tokenizer.get_decoder_prompt_ids(language=lang,task="transcribe")

    text = pipe(wav)["text"] # give audio mp3 and transcribe text
    print(text)
    return text
