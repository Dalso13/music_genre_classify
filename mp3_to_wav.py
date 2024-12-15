#pip install pydub
## install ffmpeg to your computer
# apt-get install ffmpeg
from pydub import AudioSegment
import glob
import os

def mp3ToWav(src_file, dest_file):
    sound = AudioSegment.from_mp3(src_file)
    sound.export(dest_file, format="wav")


audio_src = "metadata/fma_small/*/"

list = glob.glob(audio_src+"*.mp3")

for mp3 in list:
    mp3ToWav(mp3, mp3[:-4]+".wav")
    os.remove(mp3)