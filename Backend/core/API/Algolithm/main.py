import librosa
import numpy as np
import time
from feature import featureFN
from GMM_Training import trainGMM
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, normalize
from component import n_components
from playsound import playsound
from VoiceActivityDetection import VoiceActivityDetection
from cv_segment_to_Frame import SegmentFrame
from Speaker_Labels import speakerdiarisationdf
start = time.time()
print(start)
segLen,frameRate,numMix,sr = 1,50,64,16000

wavData,_ = librosa.load(wavFile)
# print(_)
vad = VoiceActivityDetection(wavData,frameRate)
# print(vad)
# print(f"after define{np.shape(vad)}")

#*********************************
print("Run featureFN.py")
mfcc = librosa.feature.mfcc(wavData, sr, n_mfcc=20,hop_length=int(16000/frameRate)).T

vad = np.reshape(vad,(len(vad),))
if mfcc.shape[0] > vad.shape[0]:
    vad = np.hstack((vad,np.zeros(mfcc.shape[0] - vad.shape[0]).astype('bool'))).astype('bool')
elif mfcc.shape[0] < vad.shape[0]:
    vad = vad[:mfcc.shape[0]]
mfcc = mfcc[vad,:];
print("featured")
# print(f"result fn feature {mfcc[0]}")
model = n_components(mfcc)
print("End featureFN")
#*********************************


models,mfcc,vad = featureFN(wavData,sr,frameRate,vad)
# print("comback main.py")
# print(f"value of mfcc{mfcc}")
# print(mfcc.shape)
# print(f"before pass fn train{np.shape(vad)}")

clusterset = trainGMM(wavFile, frameRate, segLen, vad, numMix)

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
# print(np.shape(pass1hyp))
# print(np.shape(vad))
# print(type(pass1hyp))
# print(np.shape(frameClust))

spkdf=speakerdiarisationdf(pass1hyp, frameRate, wavFile)
spkdf["TimeSeconds"]=spkdf.EndTime-spkdf.StartTime

print(spkdf)

print("finished")
end = time.time()
print((end - start)/60)
# playsound(wavFile)

# #print(to_text(wavFile))


