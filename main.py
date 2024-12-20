import tensorflow as tf
import socket
import json
import mp3_to_wav
import wav_to_mel_spectrogram
import os
import numpy as np
from dotenv import load_dotenv

# predict 및 socket 통신을 위한 파일
if __name__ == '__main__':
    load_dotenv()
    label_str = ["Electronic", "Experimental", "Folk", "Hip-Hop", "Instrumental", "International", "Pop", "Rock"]
    new_model = tf.keras.models.load_model('music_genre_classify.h5')

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 9999

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))

    print(HOST, PORT)

    server_socket.listen()
    try:
        while True:
            print('>> Wait')
            client_socket, addr = server_socket.accept()
            print('>> accept : ', addr)

            data = client_socket.recv(65535)
            data = data.decode('utf-8')
            json_recv_data = json.loads(data[data.index("\r\n\r\n"):].strip())
            print(">> received : ", json_recv_data)
            
            # 파일 wav 아닐경우 변환
            path = os.environ.get("VOLUME_PATH")
            file_name = json_recv_data.get("filename")
            file_path = mp3_to_wav.mp3ToWav(path+file_name)

            # 멜 스펙트로그램으로 변환
            mel = wav_to_mel_spectrogram.wav_to_mel_spectrogram(file_path)
            
            # 모델 예측값 가져오기
            mel = np.array([mel])
            y = new_model.predict(mel)
            pred_label = label_str[np.argmax(y, axis=1)[0]]

            headers = "HTTP/1.1 200 OK\r\n" + "User-Agent: JDW\r\n" + "Content-Type: application/json\r\n\r\n"
            json_send_data = json.dumps({"genre": pred_label})
            send_data = headers + json_send_data
            print(">> send data :", json_send_data)

            client_socket.send(send_data.encode())
            client_socket.close()

            # 사용된 파일 삭제
            mp3_to_wav.delete_files(file_path)
    except Exception as e:
        print('에러 : ', e)
    finally:
        server_socket.close()
