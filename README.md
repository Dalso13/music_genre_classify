# music_genre_classify
음악 데이터를 통해 장르를 분류하는 프로젝트 입니다.<br/>
음악파일을 wav로 변환후 Mel spectrogram화 시켜 CNN 모델을 활용해 학습하였습니다.<br/>
학습결과를 socket 통신을 활용하여 django 서버와 통신가능하게 설계하였습니다.(다른 프레임워크 가능)<br/>
Docker 와 volume 을 활용해 음악파일에 접근할 수 있게 설계하였습니다.(S3, NAS로 교체 가능하게 설계)<br/>

https://github.com/Dalso13/music_genre_classify_site
<br/>
<br/>
데이터셋은 FMA를 활용하였습니다.<br/>
https://github.com/mdeff/fma

## preview
<img src="https://github.com/user-attachments/assets/ea32145b-da52-4ca9-af9f-38687e24f561"/>

## 🗃 Tech stack
Language
- Python 3.9

Library
- tensorflow 2.18.0
- numpy 2.0.2
- pandas 2.2.3
- pydub 0.25.1
- librosa 0.10.2
- scikit-learn 1.6.0
- matplotlib 3.10.0
- python-dotenv 1.0.1
