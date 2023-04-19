import librosa
from matplotlib import pyplot as plt

def showWav(fileData):
    # wavFile="/Users/watcharak/BAY_Project/Testing/main/dataset/t3mon.wav"

    y, sr = librosa.load(fileData)

    plt.plot(y);

    plt.title('Signal');

    plt.xlabel('Time (samples)');

    plt.ylabel('Amplitude');
    plt.show()