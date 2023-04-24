import librosa
import numpy as np
from sklearn.mixture import *

def trainGMM(wavData, frameRate, segLen, vad, numMix):

    print("run trainGMM")
    mfcc = librosa.feature.mfcc(wavData, sr=16000, n_mfcc=20,hop_length=int(16000/frameRate)).T
    vad = np.reshape(vad,(len(vad),))
    if mfcc.shape[0] > vad.shape[0]:
        vad = np.hstack((vad,np.zeros(mfcc.shape[0] - vad.shape[0]).astype('bool'))).astype('bool')
    elif mfcc.shape[0] < vad.shape[0]:
        vad = vad[:mfcc.shape[0]]
    mfcc = mfcc[vad,:];
    print("Training GMM..")
    # GMM = GaussianMixture(n_components=1,covariance_type='diag',reg_covar =1e-3).fit(mfcc)
    # GMM = GaussianMixture(n_components=numMix,covariance_type='diag',reg_covar =1e-2).fit(mfcc)
    # GMM = GaussianMixture(n_components=numMix,covariance_type='diag',reg_covar =1e-3).fit(mfcc)
    GMM = GaussianMixture(n_components=numMix,covariance_type='diag',reg_covar =1e-4).fit(mfcc)
    # GMM = GaussianMixture(n_components=numMix,covariance_type='diag',reg_covar =1e-5).fit(mfcc)
    # GMM = GaussianMixture(n_components=numMix,covariance_type='diag',reg_covar =1e-6).fit(mfcc)
    # GMM = GaussianMixture(n_components=numMix,covariance_type='full',reg_covar =1e-7).fit(mfcc)
    print(GMM)
    segLikes = []
    segSize = frameRate*segLen
    for segI in range(int(np.ceil(float(mfcc.shape[0])/(frameRate*segLen)))):
        startI = segI*segSize
        endI = (segI+1)*segSize
        if endI > mfcc.shape[0]:
            endI = mfcc.shape[0]-1
        if endI==startI:    # Reached the end of file
            break
        seg = mfcc[startI:endI,:]
        compLikes = np.sum(GMM.predict_proba(seg),0)
        segLikes.append(compLikes/seg.shape[0])
    print("Training Done")

    return np.asarray(segLikes)