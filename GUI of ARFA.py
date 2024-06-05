import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Mock Database
users_db = {}
recipes_db = [
    {
        "name": "Jollof Rice",
        "ingredients": ["rice", "tomatoes", "onions", "pepper", "oil"],
        "instructions": "1. Cook rice. 2. Prepare sauce with tomatoes, onions, and pepper. 3. Mix and cook together.",
        "cuisine": "West African",
        "cooking_time": 45,
        "dietary_restrictions": [],
        "popularity": 5
    },
    {
        "name": "Ugali",
        "ingredients": ["maize flour", "water"],
        "instructions": "1. Boil water. 2. Add maize flour and stir until thick.",
        "cuisine": "East African",
        "cooking_time": 20,
        "dietary_restrictions": ["gluten-free"],
        "popularity": 4
    }
]

# User Registration and Authentication
def register_user(username, password):
    if username in users_db:
        return "Username already exists."
    users_db[username] = {
        "password": password,
        "favorites": [],
        "preferences": []
    }
    return "User registered successfully."

def authenticate_user(username, password):
    if username not in users_db or users_db[username]["password"] != password:
        return False
    return True

# Ingredient Input
def input_ingredients(ingredients):
    return [ingredient.strip().lower() for ingredient in ingredients]

# Recipe Search and Display
def search_recipes(ingredients):
    matched_recipes = []
    for recipe in recipes_db:
        if all(ingredient in recipe["ingredients"] for ingredient in ingredients):
            matched_recipes.append(recipe)
    return matched_recipes

# Filter and Sort
def filter_and_sort_recipes(recipes, criteria):
    if criteria == "popularity":
        return sorted(recipes, key=lambda x: x["popularity"], reverse=True)
    elif criteria == "cooking_time":
        return sorted(recipes, key=lambda x: x["cooking_time"])
    return recipes

# Recipe Details
def get_recipe_details(recipe_name):
    for recipe in recipes_db:
        if recipe["name"].lower() == recipe_name.lower():
            return recipe
    return "Recipe not found."

# GUI Interface
class RecipeFinderApp:
    def _init_(self, root):
        self.root = root
        self.root.title("African Recipe Finder")
        
        # Welcome Label
        self.welcome_label = tk.Label(root, text="Welcome to the African Recipe Finder", font=("Helvetica", 16))
        self.welcome_label.pack(pady=10)
        
        # Register Button
        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.pack(pady=5)
        
        # Login Button
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=5)
        
        # Input Ingredients Button
        self.input_ingredients_button = tk.Button(root, text="Input Ingredients", command=self.input_ingredients)
        self.input_ingredients_button.pack(pady=5)
        
        # Search Recipes Button
        self.search_recipes_button = tk.Button(root, text="Search Recipes", command=self.search_recipes)
        self.search_recipes_button.pack(pady=5)
        
        # View Recipe Details Button
        self.view_recipe_button = tk.Button(root, text="View Recipe Details", command=self.view_recipe_details)
        self.view_recipe_button.pack(pady=5)
        
    def register(self):
        username = simpledialog.askstring("Register", "Enter username:")
        password = simpledialog.askstring("Register", "Enter password:", show="*")
        if username and password:
            message = register_user(username, password)
            messagebox.showinfo("Register", message)
    
    def login(self):
        username = simpledialog.askstring("Login", "Enter username:")
        password = simpledialog.askstring("Login", "Enter password:", show="*")
        if username and password:
            if authenticate_user(username, password):
                messagebox.showinfo("Login", "Login successful.")
            else:
                messagebox.showerror("Login", "Invalid username or password.")
    
    def input_ingredients(self):
        ingredients = simpledialog.askstring("Input Ingredients", "Enter ingredients (comma-separated):")
        if ingredients:
            ingredients = input_ingredients(ingredients.split(','))
            messagebox.showinfo("Ingredients", f"Ingredients entered: {ingredients}")
    
    def search_recipes(self):
        ingredients = simpledialog.askstring("Search Recipes", "Enter ingredients (comma-separated):")
        if ingredients:
            ingredients = input_ingredients(ingredients.split(','))
            matched_recipes = search_recipes(ingredients)
            if matched_recipes:
                result = "\n".join([f"- {recipe['name']} (Cuisine: {recipe['cuisine']}, Time: {recipe['cooking_time']} mins, Popularity: {recipe['popularity']})" for recipe in matched_recipes])
                messagebox.showinfo("Matched Recipes", f"Matched Recipes:\n{result}")
            else:
                messagebox.showinfo("Matched Recipes", "No recipes found with the given ingredients.")
    
    def view_recipe_details(self):
        recipe_name = simpledialog.askstring("View Recipe Details", "Enter recipe name:")
        if recipe_name:
            details = get_recipe_details(recipe_name)
            if details != "Recipe not found.":
                result = (f"Name: {details['name']}\n"
                          f"Ingredients: {', '.join(details['ingredients'])}\n"
                          f"Instructions: {details['instructions']}\n"
                          f"Cuisine: {details['cuisine']}\n"
                          f"Cooking Time: {details['cooking_time']} mins\n"
                          f"Dietary Restrictions: {', '.join(details['dietary_restrictions'])}\n"
                          f"Popularity: {details['popularity']}")
                messagebox.showinfo("Recipe Details", result)
            else:
                messagebox.showinfo("Recipe Details", details)

try: 
    if __name__ == "_main_":
        # The main code block here
        print("This script is being run directly")
except NameError as e:
    # Handle the NameError
    print(f"A NameError occurred: {e}")
    root = tk.Tk()
    app = RecipeFinderApp(root)
    root.mainloop()