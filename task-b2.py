import cv2
import numpy as np
from datetime import datetime

MY_NAME = "FARDIN IFTY"
IMAGE_PATH = "robodk_snapshot.png"

# ---------------------------------------
# Load Image
# ---------------------------------------
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Image not found")
    exit()

img = cv2.resize(img, (900, 650))
output = img.copy()

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Kernel for noise cleaning
kernel = np.ones((5,5), np.uint8)

# =======================================
# FUNCTION TO PROCESS EACH COLOR
# =======================================
def detect_objects(mask, shape_name, draw_color):

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in contours:

        area = cv2.contourArea(cnt)

        # Ignore very small and very large regions
        if area < 2000 or area > 80000:
            continue

        x, y, w, h = cv2.boundingRect(cnt)

        if shape_name == "Box":
            cv2.rectangle(output, (x, y), (x+w, y+h), draw_color, 3)
        else:
            (cx, cy), r = cv2.minEnclosingCircle(cnt)
            cv2.circle(output, (int(cx), int(cy)), int(r), draw_color, 3)

        cv2.putText(
            output,
            shape_name,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,0,255),
            2
        )

# =======================================
# COLOR MASKS
# =======================================

# Yellow (Tall Box)
yellow_mask = cv2.inRange(hsv,
                          np.array([20,100,100]),
                          np.array([35,255,255]))
detect_objects(yellow_mask, "Box", (0,255,0))


# Red (Small Cube) - two ranges
red_mask1 = cv2.inRange(hsv,
                        np.array([0,100,100]),
                        np.array([10,255,255]))

red_mask2 = cv2.inRange(hsv,
                        np.array([170,100,100]),
                        np.array([180,255,255]))

red_mask = red_mask1 | red_mask2
detect_objects(red_mask, "Box", (0,255,0))


# Blue (Sphere)
blue_mask = cv2.inRange(hsv,
                        np.array([100,100,100]),
                        np.array([130,255,255]))
detect_objects(blue_mask, "Sphere", (255,0,0))


# =======================================
# Name + Date
# =======================================
date = datetime.now().strftime("%Y-%m-%d")

cv2.putText(
    output,
    f"{MY_NAME} - {date}",
    (10,30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.9,
    (0,0,255),
    2
)

# Save
cv2.imwrite("task-b2-output.png", output)

print("Detection complete.")
