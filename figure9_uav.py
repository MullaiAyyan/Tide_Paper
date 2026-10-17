import gdown
import cv2, os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Step 1: Download video from Google Drive
file_id = "1lkBFCYyZ2yF8lDC3LtH65R0QTiy9cDzi"
url = f"https://drive.google.com/uc?id={file_id}"
output = "UAV_Cuddalore.mp4"
gdown.download(url, output, quiet=False)

# Step 2: Extract frames
cap = cv2.VideoCapture(output)
os.makedirs("frames", exist_ok=True)
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if count % (frame_rate * 2) == 0:  # every 2 seconds
        cv2.imwrite(f"frames/frame_{count}.jpg", frame)
    count += 1
cap.release()

# Step 3: Create UAV Zonal Accuracy Panel (c)
frame = mpimg.imread("frames/frame_0.jpg")
plt.figure(figsize=(10,6))
plt.imshow(frame)
plt.title("(c) UAV Zonal Accuracy Gradient")
plt.text(50,50,"Interior‑Core 98.5 ± 0.5%", color='lime', fontsize=12, weight='bold')
plt.text(50,100,"Fringe‑Zone 91.2 ± 2.3%", color='orange', fontsize=12, weight='bold')
plt.axis('off')
plt.savefig("Figure9c_UAVZonalAccuracy.png", dpi=300)
plt.show()

# Step 4: Stitch Panels (a), (b), (c)
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Panel (a) - Statistical Validation
stats = mpimg.imread("Figure9a_Stats.png")  # replace with your bar chart PNG
axes[0].imshow(stats); axes[0].axis('off'); axes[0].set_title("(a) Statistical Validation")

# Panel (b) - Spatial Agreement Map
agreement = mpimg.imread("Figure9b_SpatialAgreement.png")  # replace with your GEE map PNG
axes[1].imshow(agreement); axes[1].axis('off'); axes[1].set_title("(b) Pontius/Fuzzy Kappa Agreement")

# Panel (c) - UAV Zonal Accuracy Map
zonal = mpimg.imread("Figure9c_UAVZonalAccuracy.png")
axes[2].imshow(zonal); axes[2].axis('off'); axes[2].set_title("(c) UAV Zonal Accuracy Gradient")

plt.tight_layout()
plt.savefig("Figure9_Combined.png", dpi=300)
plt.show()
