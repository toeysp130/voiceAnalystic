import soundfile as sf
import os
from django.http import HttpResponse
from thai_sentiment import get_sentiment
from django.db import connection

from matplotlib import pyplot as plt
import librosa
import numpy as np
from .Algolithm.feature import featureFN  # /API/models.py  /API/Algolithm/feature.py
from .Algolithm.GMM_Training import trainGMM
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, normalize
from .Algolithm.component import n_components
from .Algolithm.chunk_extract import extract_wav_by_label
from pydub import AudioSegment
from .Algolithm.Speech_Reconiz.wav2vec2_fineTune import speech_text #Backend/core/API/Algolithm/Speech_Reconiz
from .Algolithm.rex import search_pattern


# from playsound import playsound
from .Algolithm.VoiceActivityDetection import VoiceActivityDetection   #Backend/core/API/Algolithm/VoiceActivityDetection.py
from .Algolithm.cv_segment_to_Frame import SegmentFrame
from .Algolithm.Speaker_Labels import speakerdiarisationdf
# from .Algolithm.plot_wav import showWav
from django.db import models
from pymongo import MongoClient


class File(models.Model):
    file = models.FileField(upload_to='static/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    res = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.file
    
    def save(self,*args,**kwargs):
        try :
            segLen,frameRate,numMix,sr = 1,50,64,16000
            path = "/Users/watcharak/BAY/voiceAnalystic/Backend/core/static/"
            # print(self.file.path)
            path_complete = path+self.file.name
            print(path_complete)
            wavData,_ = librosa.load(self.file) 
            print("enter function")
            vad = VoiceActivityDetection(wavData,frameRate)
            models,mfcc,vad = featureFN(wavData,sr,frameRate,vad)
            clusterset = trainGMM(wavData, frameRate, segLen, vad, numMix)
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(clusterset)  
            # Normalizing the data so that the data approximately 
            # follows a Gaussian distribution
            X_normalized = normalize(X_scaled)
            cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward') 
            clust=cluster.fit_predict(X_normalized)
            frameClust = SegmentFrame(clust, segLen, frameRate, mfcc.shape[0])
            
            pass1hyp = -1*np.ones(len(vad))
            pass1hyp[vad] = frameClust
            spkdf=speakerdiarisationdf(pass1hyp, frameRate, path_complete)
            spkdf["TimeSeconds"]=spkdf.EndTime-spkdf.StartTime

            # print(extract_wav_by_label(self.file,path))
            chunk_path = os.path.join(path,f"{self.file.name}_chunk")
            os.mkdir(chunk_path)
            os.chdir(chunk_path)
            Transcription = []
            Senti_ment = []
            Regular = []


            for i, row in spkdf.iterrows():
                start_time = row.StartTime * 1000
                end_time = row.EndTime * 1000
                speaker_segment = AudioSegment.from_wav(self.file)[start_time:end_time]
                speaker_segment.export(f'chunk_{i}.wav', format='wav')
                Transcription.append(speech_text(f'chunk_{i}.wav',i))
                Senti_ment.append(get_sentiment(Transcription[i]))
                Regular.append(search_pattern(Transcription[i]))
            spkdf["Transcription"] = Transcription
            spkdf["Sentiment"] = Senti_ment
            spkdf["RegularExpression"] = Regular

            spkdf.style.set_properties(**{'text-align' : 'right'},subset=["Sentiment"])
            # print(spkdf.to_string())
            print(spkdf)

            print("successfuly process")

            print(spkdf.to_dict('records'))

            # # sent to mongo db
            # client =  MongoClient('mongodb+srv://watcharak:toey2543@cluster.9w68pty.mongodb.net/?retryWrites=true&w=majority')
            # db = client['voiceDB']
            # collection = db['voiceDetailPallaelle']
            # # spkdf.reset_index(inplace=True)
            # data_dict = spkdf.to_dict("records")
            # # Insert collection
            # # collection.insert_many(data_dict)
            # collection.insert_one({'data': data_dict})
            self.res = spkdf.to_dict('records')



        except Exception as e :
            print("Error :",e)
            return HttpResponse("Error occurred while processing the file", status=500)
        print()
        return super().save(*args,**kwargs)
    

    

# class Result(models.Model):
#     speaker = models.CharField(max_length=100)
#     transcript = models.CharField(max_length=100)
#     def __str__(self):
#         return self.transcript
    
    

