import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from collections import Counter
import json

# Clone the YOLOv5 repository
!git clone https://github.com/ultralytics/yolov5.git
%cd yolov5
%pip install -r requirements.txt  # Install dependencies

!python /content/yolov5/detect.py --weights 'Path to your weight.pt'  --source 'Path to your input.jpg or etc' --img-size 320 --conf-thres 0.50 --save-txt --save-conf

# Path to the detection results in .txt files
results_dirs = ["Path to the detection results in .txt files"]  # Add multiple directories here
detected_items = []

# Define class names based on your custom dataset (from the YAML file)
class_names = [
    'Define class names based on your custom dataset'
]

# Loop through all result directories
for results_dir in results_dirs:
    # Read each .txt file in the current result directory
    for filename in os.listdir(results_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(results_dir, filename), 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    class_id = int(parts[0])  # Class ID
                    # Check if class_id is within the range of class_names
                    if 0 <= class_id < len(class_names):
                        detected_items.append(class_names[class_id])  # Map ID to class name
                    else:
                        print(f"Warning: Skipping out-of-range class ID {class_id} (class_id might be higher than expected)")

# Count each item detected
item_counts = Counter(detected_items)
print("Detected Items and Counts:", item_counts)

# If Counter is empty, check if any items were detected
if not item_counts:
    print("No items detected or class ID mismatch.")

# Path to your recipes JSON file
recipes_file = 'Path to your recipes JSON file'

# Load the recipes from the JSON file
with open(recipes_file, 'r') as file:
    recipes_data = json.load(file)

# Print out the recipes data to check its structure
print(recipes_data)

detected_ingredients = set(detected_items)  # Unique detected ingredients
fully_matching_recipes = []
partially_matching_recipes = []

for recipe in recipes_data:
    recipe_ingredients = set(recipe['ingredients'])
    # Check if all ingredients match
    fully_matching_ingredients = recipe_ingredients.issubset(detected_ingredients)
    # Check if any ingredients match
    matching_ingredients = detected_ingredients.intersection(recipe_ingredients)
    missing_ingredients = recipe_ingredients.difference(detected_ingredients)

    if fully_matching_ingredients:
        fully_matching_recipes.append({
            'name': recipe['name'],
            'ingredients': recipe['ingredients'],
            'instructions': recipe['instructions'],
        })
    elif matching_ingredients:
        partially_matching_recipes.append({
            'name': recipe['name'],
            'ingredients': recipe['ingredients'],
            'instructions': recipe['instructions'],
            'missing_ingredients': missing_ingredients
        })

# Print out the fully matching recipes
if fully_matching_recipes:
    print("\nFully Matching Recipes (All Ingredients Detected):")
    for recipe in fully_matching_recipes:
        print(f"Recipe: {recipe['name']}")
        print("Ingredients:", recipe['ingredients'])
        print("Instructions:", recipe['instructions'])
        print("-" * 50)

# Print out the partially matching recipes
if partially_matching_recipes:
    print("\nPartially Matching Recipes (Some Ingredients Detected):")
    for recipe in partially_matching_recipes:
        print(f"Recipe: {recipe['name']}")
        print("Ingredients:", recipe['ingredients'])
        print("Instructions:", recipe['instructions'])
        print("Missing Ingredients:", recipe['missing_ingredients'])
        print("-" * 50)

# If no recipes match at all
if not fully_matching_recipes and not partially_matching_recipes:
    print("\nNo matching recipes found based on the detected ingredients.")

