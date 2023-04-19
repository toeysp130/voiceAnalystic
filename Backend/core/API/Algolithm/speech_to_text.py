import speech_recognition as sr  #Google ASR
from thai_sentiment import get_sentiment
def speech_to_thai(wav,index):
    Transcription = ""
    senti = []
    r = sr.Recognizer()
    with sr.WavFile(wav) as source:              # ใช้ "test.wav"  เป็นแหล่งให้ข้อมูลเสียง
        audio = r.record(source)                        # ส่งข้อมูลเสียงจากไฟล์
    try:
        Transcription = r.recognize_google(audio,language = "th-TH")
        senti = get_sentiment(Transcription)
    except :    
        senti = ["Unknown"]                             # ประมวลผลแล้วไม่รู้จักหรือเข้าใจเสียง
        print("Unknown")
    
    print(str(index) + "Transcription: " + Transcription )   # แสดงข้อความจากเสียงด้วย Google Speech Recognition
    print("\nSentiment : " + senti[0])
    # return [Transcription,senti[0]]


