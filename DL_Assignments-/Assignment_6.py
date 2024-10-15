#Sentiment Analysis Using LSTM

import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, SpatialDropout1D
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Sample data
texts = ["This is a good movie", "I hated the film", "It was okay", "Amazing storyline"]
labels = [1, 0, 1, 1]

# Tokenize the data
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(texts)
X = tokenizer.texts_to_sequences(texts)
X = pad_sequences(X, maxlen=100)

# Build an LSTM model
model = Sequential([
    Embedding(5000, 128, input_length=100),
    SpatialDropout1D(0.2),
    LSTM(100, dropout=0.2, recurrent_dropout=0.2),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, np.array(labels), epochs=5, batch_size=32)
