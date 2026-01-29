import cv2
import os

name = input("Enter your name: ")

save_path = f"dataset/faces/{name}"
os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

print("Press S to save image, Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Register Face", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        img_path = f"{save_path}/{count}.jpg"
        cv2.imwrite(img_path, frame)
        print(f"Saved image {count}")
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Face registration completed")
