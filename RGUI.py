import base64
import streamlit as st
import csv #  CSV to read the details from the dataset
import os # to access files
from PIL import Image #
import pandas as pd  # Import pandas for DataFrame manipulation

# Nutritional information dictionary (truncated for brevity)
nutritional_info = {
    "egg": {"carbs": 1.1, "fats": 10.6, "protein": 12.6, "calories": 150.2},
    "potato": {"carbs": 17, "fats": 0.1, "protein": 2, "calories": 76.9},
    "garlic": {"carbs": 33, "fats": 0.5, "protein": 6, "calories": 160.5},
    "green chili": {"carbs": 9, "fats": 0.2, "protein": 2, "calories": 45.8},
    "turmeric": {"carbs": 67, "fats": 10, "protein": 9, "calories": 394},
    "salt": {"carbs": 0, "fats": 0, "protein": 0, "calories": 0},
    "flour": {"carbs": 76, "fats": 1, "protein": 10, "calories": 391},
    "water": {"carbs": 0, "fats": 0, "protein": 0, "calories": 0},
    "oil": {"carbs": 0, "fats": 100, "protein": 0, "calories": 900},
    "bread rolls": {"carbs": 50, "fats": 4, "protein": 9, "calories": 290},
    "chicken": {"carbs": 0, "fats": 8, "protein": 27, "calories": 299},
    "yogurt": {"carbs": 4, "fats": 3, "protein": 10, "calories": 73},
    "rice": {"carbs": 28, "fats": 0.3, "protein": 2.7, "calories": 129.8},
    "saffron": {"carbs": 65, "fats": 5.8, "protein": 11.4, "calories": 359.2},
    "paneer": {"carbs": 6, "fats": 21, "protein": 18, "calories": 296},
    "tomato": {"carbs": 4, "fats": 0.2, "protein": 0.9, "calories": 20.4},
    "onion": {"carbs": 9, "fats": 0.1, "protein": 1.1, "calories": 43.4},
    "cumin": {"carbs": 44, "fats": 22, "protein": 18, "calories": 567},
    "coriander": {"carbs": 3.7, "fats": 0.5, "protein": 2.1, "calories": 24.4},
    "ghee": {"carbs": 0, "fats": 100, "protein": 0, "calories": 900},
    "spices": {"carbs": 40, "fats": 20, "protein": 10, "calories": 440}

  # Assuming average values for mixed spices
}

# Function to load recipes from CSV file
def load_recipes_from_csv(file_path):
    recipes = []
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            recipe = {
                "recipe": row['recipe'],
                "ingredients": row['ingredients'].split(', '),
                "steps": row['steps'].split('. '),
                "category": row['category'].strip().lower()
            }
            recipes.append(recipe)
    return recipes

# Function to display recipe details including image
def display_recipe_details(selected_recipe, recipes, img_folder):
    for recipe in recipes:
        if recipe['recipe'] == selected_recipe:
            st.write(f"\n*Recipe Name*: {recipe['recipe']}")

            # Display recipe image if available
            img_path_jpg = os.path.join(img_folder, f"{recipe['recipe']}.jpg")
            img_path_png = os.path.join(img_folder, f"{recipe['recipe']}.png")
            if os.path.exists(img_path_jpg):
                st.image(img_path_jpg, caption=f"{recipe['recipe']}", use_column_width=True)
            elif os.path.exists(img_path_png):
                st.image(img_path_png, caption=f"{recipe['recipe']}", use_column_width=True)
            else:
                st.write("Image not available")

            st.write("*Ingredients*:")
            for ingredient in recipe['ingredients']:
                st.write(f"- {ingredient}")
            st.write("\n*Steps*:")
            for step in recipe['steps']:
                st.write(f"- {step}")
            st.write(f"\n*Category*: {recipe['category'].capitalize()}")

# Function to find recipes by ingredients
def find_recipes_with_ingredients(user_ingredients, recipes):
    matching_recipes = []
    for recipe in recipes:
        ingredients = recipe['ingredients']
        if all(ingredient in ingredients for ingredient in user_ingredients):
            matching_recipes.append(recipe)
    return matching_recipes

# Function to find recipes by category
def find_recipes_by_category(category, recipes):
    matching_recipes = []
    for recipe in recipes:
        if recipe['category'] == category:
            matching_recipes.append(recipe)
    return matching_recipes

# Function to plan meals for a week
def plan_meals(recipes):
    meal_plan = {}
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meal_times = ['Breakfast', 'Lunch', 'Dinner']

    for day in days_of_week:
        meal_plan[day] = {}
        cols = st.columns(len(meal_times))  # Create columns based on meal_times length
        for col, meal_time in zip(cols, meal_times):
            with col:
                options = [recipe['recipe'] for recipe in recipes] # Search and add recipes into the generated table
                selected_recipe = st.selectbox(f"{meal_time} - {day}", options, key=f"{day}-{meal_time}")
                meal_plan[day][meal_time] = selected_recipe

    return meal_plan

# Function to download weekly plan as CSV
def download_weekly_plan_csv(meal_plan):
    csv_content = "Day,Breakfast,Lunch,Dinner\n"
    for day, meals in meal_plan.items():
        csv_content += f"{day},{meals['Breakfast']},{meals['Lunch']},{meals['Dinner']}\n"

    # Generate and save the CSV file
    csv_filename = "weekly_meal_plan.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        file.write(csv_content)

    # Provide download link
    st.markdown(get_download_link(csv_filename), unsafe_allow_html=True)

def get_download_link(file_path):
    """Generates a link to download the given file."""
    with open(file_path, 'rb') as file:
        content = file.read()
    b64 = base64.b64encode(content).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{file_path}">Download CSV file of Weekly Meal Plan</a>'
    return href

# Function to calculate nutrients
def calculate_nutrients(ingredient, weight):
    if ingredient in nutritional_info:
        nutrients = nutritional_info[ingredient]
        carbs = nutrients['carbs'] * weight / 100
        fats = nutrients['fats'] * weight / 100
        protein = nutrients['protein'] * weight / 100
        calories=nutrients['calories'] * weight / 100
        return carbs, fats, protein, calories
    else:
        return None, None, None

# Main program
def main():
    st.title("Dish Dashboard")

    file_path = 'recipes.csv'
    img_folder = 'Img'  # Folder containing recipe images
    if file_path and os.path.exists(file_path):
        recipes = load_recipes_from_csv(file_path)

        choice = st.radio("Do you want to find recipes by ingredients, by category, plan meals for the week, or check nutrients for an ingredient?",
                          ('Find recipee by ingredients', 'Find recipe by category', 'Plan meals for the week', 'Check nutrients for an ingredient'))

        if choice == 'Find recipee by ingredients':
            user_ingredients = st.text_input("Enter ingredients you have, separated by commas:").lower().split(", ")
            if user_ingredients != ['']:
                matching_recipes = find_recipes_with_ingredients(user_ingredients, recipes)
                if matching_recipes:
                    selected_recipe = st.selectbox("Select a recipe to view details", [""] + [recipe['recipe'] for recipe in matching_recipes])
                    if selected_recipe:
                        display_recipe_details(selected_recipe, recipes, img_folder)
                else:
                    st.write("Sorry, we couldn't find any recipes with the ingredients you provided. Try something else.")

        elif choice == 'Find recipe by category':
            category = st.selectbox("Select the category", ["veg", "non-veg"]).lower()
            matching_recipes = find_recipes_by_category(category, recipes)
            if matching_recipes:
                selected_recipe = st.selectbox("Select a recipe to view details", [""] + [recipe['recipe'] for recipe in matching_recipes])
                if selected_recipe:
                    display_recipe_details(selected_recipe, recipes, img_folder)
            else:
                st.write("Sorry, we couldn't find any recipes in the category you provided. Try something else.")

        elif choice == 'Plan meals for the week':
            meal_plan = plan_meals(recipes)

            if st.button("Show Weekly Meal Plan"):
                st.write("\n\n")
                st.write("### Weekly Meal Plan")
                st.write("\n")
                df = pd.DataFrame(meal_plan)
                st.table(df)

                download_weekly_plan_csv(meal_plan)

        elif choice == 'Check nutrients for an ingredient':
            st.write("\nCheck nutrients for an ingredient:")
            nutrient_ingredient = st.text_input("Enter the ingredient you want to check:").lower()
            weight = st.number_input("Enter the weight of the ingredient in grams:", min_value=0.0, step=1.0)
            if nutrient_ingredient and weight:
                carbs, fats, protein,calories = calculate_nutrients(nutrient_ingredient, weight)
                if carbs is not None:
                    st.write(f"\nNutritional information for {weight} grams of {nutrient_ingredient}:")
                    st.write(f"Carbohydrates: {carbs:.2f} grams")
                    st.write(f"Fats: {fats:.2f} grams")
                    st.write(f"Protein: {protein:.2f} grams")
                    st.write(f"Calories: {calories:.2f} calories (approx.)")
                else:
                    st.write("Sorry, nutritional information for this ingredient is not available.")

main()