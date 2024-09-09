import cv2
import face_recognition
import numpy as np
import os
import urllib.request

# Load known faces
KNOWN_FACES_DIR = "Dataset/known_faces/"
known_face_encodings = []
known_face_names = []

for person in os.listdir(KNOWN_FACES_DIR):
    person_dir = os.path.join(KNOWN_FACES_DIR, person)
    for img_file in os.listdir(person_dir):
        img_path = os.path.join(person_dir, img_file)
        img = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(img)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(person)

# ESP32-CAM URL
url = 'http://<YOUR_IP>/cam-lo.jpg'

cv2.namedWindow("Intruder Detection", cv2.WINDOW_AUTOSIZE)

while True:
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)
    rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Detect faces in the live stream
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Intruder"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(img, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Intruder Detection", img)
    if cv2.waitKey(5) == ord('q'):
        break

cv2.destroyAllWindows()
