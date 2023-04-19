from transformers import Wav2Vec2CTCTokenizer, Wav2Vec2FeatureExtractor,Wav2Vec2Processor,Wav2Vec2ForCTC,TrainingArguments,Trainer
from ..rex import search_pattern
import torchaudio
import torch

#load pretrained processor and model
processor = Wav2Vec2Processor.from_pretrained("/Users/watcharak/BAY/voiceAnalystic/Backend/core/API/Algolithm/Speech_Reconiz")
model = Wav2Vec2ForCTC.from_pretrained("/Users/watcharak/BAY/voiceAnalystic/Backend/core/API/Algolithm/Speech_Reconiz")

def speech_text(wavfile,idx) : 
#get 2 examples as sample input
    wavfile,sr = torchaudio.load(wavfile)
    re_sr = torchaudio.transforms.Resample(sr,16000)
    exi = re_sr(wavfile)[0].numpy()

    inputs = processor(exi, sampling_rate=16000, return_tensors="pt", padding=False) #padding=True
    #s.replace(" ", "") ][ช่องว่างของ text]
    #infer
    with torch.no_grad():
        logits = model(inputs.input_values,).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    text = processor.batch_decode(predicted_ids)   
    clean_text = [x.replace(' ', '') for x in text]

    # print(str(idx) + " output wav2vec2 Transcript : ", text[0].replace(" ",""))
    print(str(idx) + " output wav2vec2 Transcript : ", clean_text[0])

    # print(f"Output math regx: {search_pattern(text[0])}")
    print(f"Output math regx: {search_pattern(clean_text[0])}")


    return clean_text[0]
    
    # print(f"output sentiment dataframe : {senti}")



