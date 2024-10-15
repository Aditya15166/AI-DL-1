# Facial Recognition Using OpenCV and Deep Learning (Binary Classification)

import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator

# Use VGG16 model for feature extraction
vgg_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Build a simple binary classifier on top of VGG16
model = Sequential([
    vgg_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Prepare dataset (e.g., faces dataset with two classes: 'person1' and 'person2')
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    'dataset/train', target_size=(224, 224), batch_size=32, class_mode='binary')

# Train the model
model.fit(train_generator, epochs=5)

# Perform facial recognition using OpenCV
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.resize(frame, (224, 224))
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)

    if prediction < 0.5:
        cv2.putText(frame, 'Person 1', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    else:
        cv2.putText(frame, 'Person 2', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Facial Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
