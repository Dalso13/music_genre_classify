import numpy as np
import librosa.effects
import librosa.feature
import glob

# 최소 사이즈
win_size = 660000


def wav_to_mel_spectrogram(wav_path):
    x, sr = librosa.load(wav_path)
    # 길이 늘리기
    if x.shape[0] < win_size:
        rate = (win_size+10000) / x.shape[0]
        x = librosa.effects.time_stretch(x, rate=rate)

    x = librosa.effects.time_stretch(x[:win_size], rate=2.0)
    mel = librosa.feature.melspectrogram(y=x)
    mel = librosa.power_to_db(mel)
    mel = mel.reshape(mel.shape[0], mel.shape[1], 1)
    return mel


if __name__ == "__main__":
    path = "metadata/fma_small/"

    wav_path_list = glob.glob(path + "*/*.wav")

    wav_list = []

    for wav in wav_path_list:
        mel = wav_to_mel_spectrogram(wav)
        wav_list.append(mel)

    wav_list = np.array(wav_list)
    print(wav_list.shape)
    np.save("wav_to_mel_spectrogram", wav_list)