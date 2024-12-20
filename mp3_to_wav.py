#pip install pydub
## install ffmpeg to your computer
# apt-get install ffmpeg
from pydub import AudioSegment
import glob
import os


def mp3ToWav(src_file):
    _, ext = os.path.splitext(src_file)
    if ext != ".wav":
        dest_file = src_file[:-4] + ".wav"
        sound = AudioSegment.from_mp3(src_file)
        sound.export(dest_file, format="wav")
        delete_files(src_file)

        return dest_file
    return src_file


def delete_files(path):
    os.remove(path)


if __name__ == '__main__':
    audio_src = "metadata/fma_small/*/"

    mp3_list = glob.glob(audio_src + "*.mp3")

    for mp3 in mp3_list:
        mp3ToWav(mp3)
