from flask import Flask, request, jsonify
from uuid import uuid4
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

recipes = {}

@app.route("/")
def home():
    return "Recipe Service is running!"

@app.route("/recipes", methods=["GET"])
def get_recipes():
    return jsonify(list(recipes.values()))

@app.route("/recipes/<recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    return jsonify(recipes.get(recipe_id, {"error": "Recipe not found"}))

@app.route("/recipes", methods=["POST"])
def add_recipe():
    data = request.get_json()
    recipe_id = str(uuid4())
    recipe = {"id": recipe_id, "name": data.get("name"), "instructions": data.get("instructions")}
    recipes[recipe_id] = recipe
    return jsonify(recipe), 201

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok", "service": "recipe-service"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)