import librosa
import numpy as np
from .component import n_components

def featureFN(wavData,sr,frameRate,vad):
    print("Run featureFN.py")
    mfcc = librosa.feature.mfcc(wavData, sr, n_mfcc=20,hop_length=int(16000/frameRate)).T
    vad = np.reshape(vad,(len(vad),))
    print(mfcc)
    print("")
    if mfcc.shape[0] > vad.shape[0]:
        vad = np.hstack((vad,np.zeros(mfcc.shape[0] - vad.shape[0]).astype('bool'))).astype('bool')
    elif mfcc.shape[0] < vad.shape[0]:
        vad = vad[:mfcc.shape[0]]
    mfcc = mfcc[vad,:];
    model = n_components(mfcc)
    print("End featureFN")
    
    return model,mfcc,vad
