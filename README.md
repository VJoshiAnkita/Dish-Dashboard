
# Dish Dashboard 🍳

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Dish Dashboard** is a user-friendly web application designed to help users discover recipes, plan weekly meals, and analyze nutritional content. Whether you're a home cook or a health enthusiast, this tool simplifies meal management with its intuitive features.

---

## Features ✨

- **Recipe Search by Ingredients**: Find recipes using ingredients you already have.
- **Category Filter**: Browse vegetarian or non-vegetarian recipes.
- **Weekly Meal Planning**: Plan breakfast, lunch, and dinner for the entire week.
- **Nutritional Calculator**: Check carbs, fats, protein, and calories for any ingredient.
- **Recipe Details**: View ingredients, step-by-step instructions, and images (if available).
- **Export Meal Plans**: Download your weekly meal plan as a CSV file.

---

## Tech Stack 🛠️

- **Frontend**: Streamlit
- **Backend**: Python
- **Data Handling**: CSV, Pandas
- **Image Processing**: Pillow (PIL)
- **Nutritional Data**: Custom dictionary-based calculations

---

## Installation and Setup 🚀

### Prerequisites
- Python 3.8+
- pip package manager

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/dish-dashboard.git
   cd dish-dashboard
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Sample `requirements.txt`)*:
   ```
   streamlit
   pandas
   Pillow
   ```

3. **Project Structure**:
   ```
   dish-dashboard/
   ├── RGUI.py          # Main application logic
   ├── recipes.csv      # Recipe database
   ├── Img/             # Folder for recipe images (optional)
   └── README.md
   ```

4. **Run the App**:
   ```bash
   streamlit run RGUI.py
   ```

---

## Usage Guide 📖

1. **Select a Feature**:
   - **Find Recipes by Ingredients**: Enter ingredients (e.g., `egg, rice`).
   - **Find Recipes by Category**: Choose "veg" or "non-veg".
   - **Plan Meals for the Week**: Assign recipes to breakfast, lunch, and dinner.
   - **Check Nutrients**: Enter an ingredient (e.g., `potato`) and weight in grams.

2. **View Recipe Details**: Select a recipe to see ingredients, steps, and images.

3. **Export Meal Plan**: After planning, download the CSV for your weekly schedule.

---

## Project Structure 🗂️

- **`recipes.csv`**: Contains recipe names, ingredients, steps, and categories.
- **`RGUI.py`**: Streamlit app logic for UI, data loading, and calculations.
- **`Img/`**: Stores recipe images (e.g., `Egg Fried Rice.jpg`).

---

## Contributing 🤝

Contributions are welcome! Fork the repository, create a branch, and submit a pull request. For major changes, open an issue first.

---

## License 📜

This project is open-source. Feel free to use, modify, and distribute it.
