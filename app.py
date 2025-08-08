from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import threading
from pygame import mixer

app = Flask(__name__)

# بارگذاری مدل و فایل‌های Haarcascade
model = load_model('models/cnnCat2.h5')
face_cascade = cv2.CascadeClassifier('haar cascade files/haarcascade_frontalface_alt.xml')
leye_cascade = cv2.CascadeClassifier('haar cascade files/haarcascade_lefteye_2splits.xml')
reye_cascade = cv2.CascadeClassifier('haar cascade files/haarcascade_righteye_2splits.xml')

mixer.init()
sound = mixer.Sound('alarm.wav')

cap = cv2.VideoCapture(0)

score = 0
thicc = 2
camera_active = True  # وضعیت دوربین

def gen_frames():
    global score, thicc, camera_active
    while True:
        if not camera_active:
            continue  # وقتی غیرفعال باشد، فریم نفرست

        success, frame = cap.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25))
            left_eye = leye_cascade.detectMultiScale(gray)
            right_eye = reye_cascade.detectMultiScale(gray)

            rpred = [99]
            lpred = [99]

            for (x, y, w, h) in right_eye:
                r_eye = frame[y:y + h, x:x + w]
                r_eye = cv2.cvtColor(r_eye, cv2.COLOR_BGR2GRAY)
                r_eye = cv2.resize(r_eye, (24, 24))
                r_eye = r_eye / 255
                r_eye = r_eye.reshape(24, 24, -1)
                r_eye = np.expand_dims(r_eye, axis=0)
                rpred = np.argmax(model.predict(r_eye), axis=1)
                break

            for (x, y, w, h) in left_eye:
                l_eye = frame[y:y + h, x:x + w]
                l_eye = cv2.cvtColor(l_eye, cv2.COLOR_BGR2GRAY)
                l_eye = cv2.resize(l_eye, (24, 24))
                l_eye = l_eye / 255
                l_eye = l_eye.reshape(24, 24, -1)
                l_eye = np.expand_dims(l_eye, axis=0)
                lpred = np.argmax(model.predict(l_eye), axis=1)
                break

            if rpred[0] == 0 and lpred[0] == 0:
                score += 1
                status = "Closed"
            else:
                score -= 1
                status = "Open"

            if score < 0:
                score = 0

            if score > 15:
                if thicc < 16:
                    thicc += 2
                else:
                    thicc -= 2
                    if thicc < 2:
                        thicc = 2
                cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), thicc)
                try:
                    sound.play()
                except:
                    pass

            cv2.putText(frame, status, (10, frame.shape[0] - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, 'Score: ' + str(score), (100, frame.shape[0] - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                        (255, 255, 255), 1, cv2.LINE_AA)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/toggle_camera', methods=['POST'])
def toggle_camera():
    global camera_active
    camera_active = not camera_active
    return jsonify({'status': 'on' if camera_active else 'off'})

if __name__ == '__main__':
    app.run(debug=True)
