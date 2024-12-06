import numpy as np
import cv2
import math
# import spotipy
from PIL import Image
from tensorflow.keras.preprocessing import image
from keras.models import model_from_json
# from Spotipy import Spotipy
import pandas as pd
import cv2
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cascade_path = os.path.join(BASE_DIR, 'myapp', 'static',
                            'haarcascades', 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cascade_path)
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cv2.ocl.setUseOpenCL(False)
emotion_dict = {0: "Angry",1: "Happy", 2: "Neutral",
                3: "Sad"}
music_dict = {0: 'myapp/songs/angry.csv', 1: 'myapp/songs/happy__labelled_uri.csv', 2: 'myapp/songs/neutral__labelled_uri.csv',
              3: 'myapp/songs/sad__labelled_uri.csv'}
model_path = os.path.join(BASE_DIR, 'myapp', 'models',
                          'emotion_model', 'emotion_model.json')
weight_path = os.path.join(BASE_DIR, 'myapp', 'models',
                           'emotion_model', 'emotion_model.h5')
global last_frame1
last_frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
global cap1
show_text = [0]
class VideoCamera(object):
    def get_frame(self):
        global cap1
        global df1
        json_file = open(model_path, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        # emotion_model.load_weights(weight_path)

        # try:
        #     emotion_model.load_weights(weight_path)
        #     print("Weights loaded successfully.")


        # except Exception as e:
        #     print(f"Error loading weights: {e}")
        # cap1 = cv2.VideoCapture(0)
        cap1 = cv2.VideoCapture(0)


# if not cap1.isOpened():
#     print("Error: Could not open camera.")
# else:
#     print("Camera opened successfully.")

# # Capture frames in a loop
# # while True:
#     ret, frame = cap1.read()
#     if not ret:
#         print("Error: Could not read frame.")
#         break

#     # cv2.imshow('Camera Feed', frame)

#     # Break the loop on 'q' key press
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the camera and close windows
# cap1.release()
# cv2.destroyAllWindows()
        success, frame = cap1.read()
        image = cv2.resize(frame, (600, 500))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
        # emotion_model = model_from_json(loaded_model_json)
        # emotion_model.load_weights("emotion_model.h5")
        emotion_model = model_from_json(loaded_model_json)
        emotion_model.load_weights(weight_path)
        for (x, y, w, h) in face_rects:
            cv2.rectangle(image, (x, y-50), (x+w, y+h+10), (0, 255, 0), 2)
            roi_gray_frame = gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(
                cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
            prediction = emotion_model.predict(cropped_img)

            maxindex = int(np.argmax(prediction))
            show_text[0] = maxindex
            # print("===========================================",music_dist[show_text[0]],"===========================================")
            # print(df1)
            cv2.putText(image, emotion_dict[maxindex], (x+20, y-60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            df1 = music_rec()

        global last_frame1
        last_frame1 = image.copy()
        pic = cv2.cvtColor(last_frame1, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(last_frame1)
        img = np.array(img)
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes(), df1


def music_rec():
    # print('---------------- Value ------------', music_dist[show_text[0]])
    df = pd.read_csv(music_dict[show_text[0]])
    df = df[['uri']]
    random_number = np.random.randint(10, 20)
    df = df.head(random_number)
    return df
