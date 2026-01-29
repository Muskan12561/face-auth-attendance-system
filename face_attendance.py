import cv2
import os
import numpy as np
from datetime import datetime

# ================= PATHS =================
dataset_path = "dataset/faces"
attendance_file = "attendance.csv"

# ================= FACE SETUP =================
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ================= TRAINING =================
faces = []
labels = []
label_map = {}
label_id = 0

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)
    if not os.path.isdir(person_path):
        continue

    label_map[label_id] = person
    for img_name in os.listdir(person_path):
        img = cv2.imread(os.path.join(person_path, img_name), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            faces.append(img)
            labels.append(label_id)

    label_id += 1

recognizer.train(faces, np.array(labels))

# ================= READ TODAY STATUS =================
today = str(datetime.now().date())
user_status = {}  # name -> last status today

if os.path.exists(attendance_file):
    with open(attendance_file, "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            name, date, time, status = line.strip().split(",")
            if date == today:
                user_status[name] = status

# ================= CAMERA =================
cap = cv2.VideoCapture(0)
marked = False

print("Show your face. Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_detected = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces_detected:
        face_img = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face_img)

        if confidence < 90:
            name = label_map[label]

            if not marked:
                now = datetime.now().strftime("%H:%M:%S")

                if name not in user_status:
                    status = "Punch-In"
                elif user_status[name] == "Punch-In":
                    status = "Punch-Out"
                else:
                    status = None

                if status:
                    with open(attendance_file, "a") as f:
                        f.write(f"{name},{today},{now},{status}\n")
                    marked = True

        else:
            name = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, name, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    cv2.imshow("Face Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
