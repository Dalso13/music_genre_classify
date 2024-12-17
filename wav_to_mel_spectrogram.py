import pandas as pd
import numpy as np
import librosa.effects
import librosa.feature
import librosa.display
import glob

path = "metadata/fma_small/"

wav_path_list = glob.glob(path + "*/*.wav")

wav_list = []
# 최소 사이즈
win_size = 660000

for wav in wav_path_list:
    x, sr = librosa.load(wav)
    x = librosa.effects.time_stretch(x[:win_size], rate=2.0)
    mel = librosa.feature.melspectrogram(y=x)
    mel = librosa.power_to_db(mel)
    mel = mel.reshape(mel.shape[0], mel.shape[1], 1)
    wav_list.append(mel)

wav_list = np.array(wav_list)
print(wav_list.shape)
np.save("wav_to_mel_spectrogram", wav_list)
