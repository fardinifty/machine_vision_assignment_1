import cv2
from datetime import datetime

MY_NAME = "FARDIN IFTY"
IMAGE_PATH = "robodk_snapshot.png"

img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Snapshot not found!")
    exit()

height, width, channels = img.shape
print("Height:", height)
print("Width:", width)
print("Channels:", channels)

cv2.rectangle(img, (150, 200), (250, 300), (0, 255, 0), 2)
cv2.putText(img, "Object 1", (150, 190),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.circle(img, (400, 250), 60, (255, 0, 0), 2)
cv2.putText(img, "Object 2", (360, 180),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

date_str = datetime.now().strftime("%Y-%m-%d")

cv2.putText(img,
            f"{MY_NAME} - {date_str}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2)

cv2.imwrite("task-b2-output.png", img)

print("Task B2 completed.")
