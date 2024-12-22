import numpy as np
import pandas as pd

from tensorflow.keras import Sequential
from tensorflow.keras.losses import sparse_categorical_crossentropy
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from sklearn.model_selection import train_test_split

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

dataset = pd.read_csv('metadata/genre_dataset.csv', header=None)

X = np.load("wav_to_mel_spectrogram.npy")
y = dataset.iloc[:, -1].astype(np.int64)

label = len(np.unique(y))
label_str = ["Electronic", "Experimental", "Folk", "Hip-Hop", "Instrumental", "International", "Pop", "Rock"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

cnn = Sequential([
    Input(shape=X[0].shape),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dropout(0.5),
    Dense(128, activation='relu'),
    Dense(8, activation='softmax')
])

cnn.compile(loss=sparse_categorical_crossentropy,
            optimizer='adam',
            metrics=['acc'])

result = cnn.fit(X, y,
                 validation_split=0.2,
                 batch_size=64,
                 epochs=10)

# print(cnn.evaluate(X_test, y_test))
#
# pred_proba = cnn.predict(X_test)
#
# pred_label = np.argmax(pred_proba, axis=1)
#
# incor_ind = np.argwhere(y_test != pred_label)
# print(incor_ind.shape[0]/y_test.shape[0])

cnn.save('music_genre_classify.h5')
