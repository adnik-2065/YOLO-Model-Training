import os
import random
import shutil

# Paths
DATASET_PATH = "dataset/PlantVillage_for_object_detection/Dataset"
IMAGES_PATH = os.path.join(DATASET_PATH, "images")
LABELS_PATH = os.path.join(DATASET_PATH, "labels")

# Output folders
TRAIN_IMG = os.path.join(IMAGES_PATH, "train")
VAL_IMG = os.path.join(IMAGES_PATH, "val")
TRAIN_LBL = os.path.join(LABELS_PATH, "train")
VAL_LBL = os.path.join(LABELS_PATH, "val")

# Create folders
os.makedirs(TRAIN_IMG, exist_ok=True)
os.makedirs(VAL_IMG, exist_ok=True)
os.makedirs(TRAIN_LBL, exist_ok=True)
os.makedirs(VAL_LBL, exist_ok=True)

# Get all images
images = [f for f in os.listdir(IMAGES_PATH) if f.endswith((".jpg", ".png", ".jpeg"))]

# Shuffle images
random.shuffle(images)

# Split ratio
split_ratio = 0.8
split_index = int(len(images) * split_ratio)

train_images = images[:split_index]
val_images = images[split_index:]

# Function to move files
def move_files(image_list, dest_img, dest_lbl):
    for img in image_list:
        label = img.rsplit(".", 1)[0] + ".txt"

        # Move image
        shutil.move(os.path.join(IMAGES_PATH, img), os.path.join(dest_img, img))

        # Move label (if exists)
        label_path = os.path.join(LABELS_PATH, label)
        if os.path.exists(label_path):
            shutil.move(label_path, os.path.join(dest_lbl, label))

# Move files
move_files(train_images, TRAIN_IMG, TRAIN_LBL)
move_files(val_images, VAL_IMG, VAL_LBL)

print("Dataset split completed!")
print(f"Train images: {len(train_images)}")
print(f"Val images: {len(val_images)}")