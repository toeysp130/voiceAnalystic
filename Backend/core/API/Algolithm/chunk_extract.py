from pydub import AudioSegment
from pydub.silence import split_on_silence
from .Speech_Reconiz.wav2vec2_fineTune import speech_text
import os
import numpy as np


# wavFile = "/Users/watcharak/BAY_Project/Testing/main/dataset/t4mon.wav"
# chunk_name = wavFile.split('/')[-1].split('.')[0]
# sound_file = AudioSegment.from_wav(wavFile)
def extract_wav_by_label(wavFile,path):
   print("Enter chunk excececce")
   chunk_name = wavFile.name.split('/')[-1].split('.')[0]
   sound_file = AudioSegment.from_wav(wavFile)
   audio_chunks = split_on_silence(sound_file, min_silence_len=256, silence_thresh=-35 )
   path = os.path.join(path,f"{chunk_name}_chunk")
   os.mkdir(path)
   os.chdir(path)
   for i, chunk in enumerate(audio_chunks):
      out_file = "chunk{0}.wav".format(i)
      print("exporting", out_file)
      chunk.export(out_file, format="wav")
      speech_text(out_file,i)
   return "sucess of chunk"

