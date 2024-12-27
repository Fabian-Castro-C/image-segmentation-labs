import os

# Define dataset configuration
DATASET_NAME = "PASCAL_VOC"
DATASET_PATH = os.path.join(os.getcwd(), "datasets")

# PASCAL VOC specific configurations
PASCAL_VOC_CONFIG = {
    "download": True,
    "year": "2012",
    "split": "trainval",
    "path": os.path.join(DATASET_PATH, "PASCAL_VOC"),
}

# COCO specific configurations
COCO_CONFIG = {
    "download": False,  # Requires manual download
    "path": os.path.join(DATASET_PATH, "COCO"),
    "annotation_type": "instances",
}

# Create dataset folder if it doesn't exist
os.makedirs(DATASET_PATH, exist_ok=True)
