from flask import Flask, request, jsonify
from uuid import uuid4
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ingredients = {}

@app.route("/")
def home():
    return "Ingredient Service is running!"

@app.route("/ingredients", methods=["GET"])
def get_ingredients():
    return jsonify(list(ingredients.values()))

@app.route("/ingredients/<ingredient_id>", methods=["GET"])
def get_ingredient(ingredient_id):
    return jsonify(ingredients.get(ingredient_id, {"error": "Ingredient not found"}))

@app.route("/ingredients", methods=["POST"])
def add_ingredient():
    data = request.get_json()
    ing_id = str(uuid4())
    ing = {"id": ing_id, "name": data.get("name"), "quantity": data.get("quantity")}
    ingredients[ing_id] = ing
    return jsonify(ing), 201

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok", "service": "ingredient-service"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)