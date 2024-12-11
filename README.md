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
The dataset and model are hosted on Roboflow. You can access them [here](https://universe.roboflow.com/capstoneproject-yly17/fridge_roboflow).

---

## Demo
Here are some examples of the SmartFridge system in action:

### Step 1: Object Detection in the Fridge
**Center Shelf Detection Result:**
![Center Shelf Detection](demo_result/center_shelf_demo_result.jpg)

**Door Shelf Detection Result:**

![Door Shelf Detection](demo_result/door_shelf_demo_result.jpg)

### Step 2: Recipe Matching and Ingredient Recognition
**Ingredient Detection Output:**
![Ingredient Output](demo_result/demo_ingredient_output.png)

### Step 3: Recipe Suggestion Based on Detected Ingredients
**Recipe Suggestion Output:**
![Recipe Output](demo_result/demo_receipe_output.jpg)

---

## How to Use
1. Clone the repository.
2. Follow the steps in the `model_training.py` script to train the YOLOv5 model.
3. Use the `recommendation.py` script to generate recipe suggestions based on detected ingredients.
4. Refer to the [Roboflow Documentation](https://roboflow.com) to access and manage the dataset.

---

## Conclusion and Future Work
The SmartFridge project demonstrates the potential of AI in enhancing daily life through intelligent recipe recommendations. Future improvements include:
- Adding voice assistant integration.
- Supporting additional food item types.
- Improving detection accuracy for small or obscured items.

---

## License
This project is licensed under the GPL-3.0 License.
