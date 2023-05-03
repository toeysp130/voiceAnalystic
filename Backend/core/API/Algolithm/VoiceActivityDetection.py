import librosa
import numpy as np
def VoiceActivityDetection(wavData, frameRate):
    print("detecting activity...")

    # uses the librosa library to compute short-term energy
    # ste = librosa.feature.rms(wavData,hop_length=int(16000/frameRate)).T
    ste = librosa.feature.rms(wavData).T

    print(ste)
    threshold = 0.13*(np.percentile(ste,97.5) + 9*np.percentile(ste,2.5))    # Trim 5% off and set threshold as 0.1x of the ste range
    print("detected")

    return (ste>threshold).astype('bool')