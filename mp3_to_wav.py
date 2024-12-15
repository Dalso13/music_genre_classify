#pip install pydub
## install ffmpeg to your computer
# apt-get install ffmpeg
from pydub import AudioSegment


def mp3ToWav(src_file, dest_file):
    sound = AudioSegment.from_mp3(src_file)
    sound.export(dest_file, format="wav")


mp3ToWav(src_file="", dest_file="")
