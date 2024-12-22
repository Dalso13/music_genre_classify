FROM python:3.9-slim

SHELL ["/bin/bash", "-c"]
WORKDIR /root

RUN apt update
RUN apt install git -y
RUN apt install ffmpeg -y
RUN mkdir project

WORKDIR /root/project
RUN git clone https://github.com/Dalso13/music_genre_classify.git .

RUN python -m venv venv
RUN source venv/bin/activate

RUN pip install -r ./requirements.txt

COPY music_genre_classify.h5 .

CMD ["python","main.py"]