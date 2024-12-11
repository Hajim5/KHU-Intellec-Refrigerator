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

Roboflow Model
The model used in this project was trained and hosted on Roboflow. You can access the dataset and model details using the following link:

https://universe.roboflow.com/capstoneproject-yly17/fridge_roboflow/model/1

Roboflow Model and Dataset

How to Use the Roboflow Model
Visit the link to access the dataset and model.
Follow the steps outlined in the Roboflow documentation to download the dataset or use the model directly via their API.
Use the downloaded dataset or model weights with the provided training and inference scripts in this repository.
API Integration
If you're using the Roboflow API:

Include the Roboflow API key in your environment variables.
Use the API to download the dataset or integrate the model into your application.
Example for downloading the dataset via API:

from roboflow import Roboflow

rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace().project("fridge_roboflow")
dataset = project.version(1).download("yolov5")

This ensures that anyone viewing your repository understands how to access and use the Roboflow model. If you're sharing the model weights or dataset files, ensure you're allowed to distribute them as per Roboflow's terms of use.







