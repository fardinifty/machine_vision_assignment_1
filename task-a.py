import cv2
import matplotlib.pyplot as plt


MY_NAME = "Fardin Ifty"   
IMAGE_PATH = "colorful_image.jpg"

img_bgr = cv2.imread(IMAGE_PATH)

if img_bgr is None:
    print("Error: Could not load image.")
    exit()

img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

r_channel, g_channel, b_channel = cv2.split(img_rgb)

fig, ax = plt.subplots(2, 2, figsize=(12, 8))


ax[0, 0].imshow(img_rgb)
ax[0, 0].set_title(f"Original Image (RGB) - {MY_NAME}")
ax[0, 0].axis("off")

ax[0, 1].imshow(r_channel, cmap='gray')
ax[0, 1].set_title("RED channel")
ax[0, 1].axis("off")

ax[1, 0].imshow(g_channel, cmap='gray')
ax[1, 0].set_title("GREEN channel")
ax[1, 0].axis("off")

ax[1, 1].imshow(b_channel, cmap='gray')
ax[1, 1].set_title("BLUE channel")
ax[1, 1].axis("off")

plt.tight_layout()

plt.savefig("task-a-output.png", dpi=300)

print("Task A completed successfully.")
plt.show()
