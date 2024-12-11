# Step 1: Clone the YOLOv5 Repository
!git clone https://github.com/ultralytics/yolov5.git
%cd yolov5
%pip install -r requirements.txt  # Install dependencies for YOLOv5

# Step 2: Install Roboflow Python Package
!pip install roboflow

# Step 3: Import and Initialize Roboflow
from roboflow import Roboflow

# Replace "YOUR_API_KEY" with your actual Roboflow API key
rf = Roboflow(api_key="YOUR_API_KEY")

# Replace "NAME_OF_PROJECT" with your Roboflow project name
project = rf.workspace().project("NAME_OF_PROJECT")

# Replace "VERSION_NUMBER" with the version of your dataset
dataset = project.version("VERSION_NUMBER").download("yolov5")

# The dataset will include the YAML file automatically. Locate it in the downloaded folder.

# Step 4: Train the YOLOv5 Model
# Replace "PATH_TO_YAML" with the actual path to your dataset's YAML file
!python train.py \--img 640 \   --batch 16 \   --epochs 50 \   --data "PATH_TO_YAML" \ --weights yolov5s.pt 

!python detect.py --weights path/to/your/weights.pt --img 640 --conf 0.25 --source path/to/your/image.jpg
