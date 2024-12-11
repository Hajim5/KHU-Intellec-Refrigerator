The SmartFridge project aims to detect items in a fridge using YOLOv5 and a custom dataset, and recommend recipes based on the detected ingredients. This project integrates object detection, recipe matching, and a user-friendly interface to enhance the cooking experience.

Project Overview
This system leverages computer vision to recognize food items inside the fridge and uses a recipe database to suggest meal ideas based on the available ingredients. The key features of the project include:

Object Detection: Detects food items in the fridge using YOLOv5 and a custom dataset.
Recipe Recommendations: Matches the detected ingredients to recipes stored in a recipe database (JSON format).
Model Training: Utilizes YOLOv5 for object detection and Roboflow for dataset annotation.
API Integration: Uses Roboflow’s API for dataset management and model training.
Google Colab: Provides a convenient platform for training the YOLOv5 model.
Features
Food Item Detection: Automatically detects items inside the fridge with high accuracy using a custom dataset and YOLOv5.
Recipe Suggestion: Suggests recipes based on available ingredients detected in the fridge.
Dynamic Database Integration: Uses a JSON-based recipe database for recipe matching.
Custom Training: Train the YOLOv5 model on a custom dataset using Google Colab.
Annotation and Labeling: Dataset annotations are created using Roboflow API, which is used for training and evaluation.
Requirements
Python 3.x
Google Colab (for training)
YOLOv5
Roboflow API
JSON for recipe database
Dependencies:
torch
opencv-python
roboflow
requests
pandas
