# SmartFridge: Intelligent Recipe Recommendation System

## Overview
The SmartFridge project uses YOLOv5 and a custom dataset to detect items in a fridge and recommend recipes based on the detected ingredients. This system integrates object detection, recipe matching, and a user-friendly interface to enhance the cooking experience.

---

## Features
- **Food Item Detection:** High-accuracy detection of food items inside the fridge using YOLOv5 and a custom dataset.
- **Recipe Recommendation:** Suggests recipes based on available ingredients.
- **Dynamic Database Integration:** JSON-based recipe database for easy expansion.
- **Custom Training:** Training the YOLOv5 model on a custom dataset using Google Colab.
- **Roboflow Integration:** Efficient dataset annotation and management via the Roboflow API.

---

## Dataset and Model
The dataset and model are hosted on Roboflow. You can access them [here](https://universe.roboflow.com/capstoneproject-yly17/fridge_roboflow/model/1).

---

## Demo
Here’s an example of the SmartFridge system in action:

### Step 1: Object Detection in the Fridge
**Center Shelf Detection Result:**
![Center Shelf Detection](demo_result/center_shelf_demo_result.jpg)

---

## How to Use
1. Clone the repository.
2. Follow the steps in the `model_training.py` script to train the YOLOv5 model.
3. Use the `recommendation.py` script to generate recipe suggestions based on detected ingredients.
4. Refer to the [Roboflow Documentation](https://roboflow.com) to access and manage the dataset.

---
