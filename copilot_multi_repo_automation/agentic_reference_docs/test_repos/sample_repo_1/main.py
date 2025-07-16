#!/usr/bin/env python3
"""
Sample Repository 1 - API Service
A demonstration repository for the Agentic AI Documentation Generator POC
"""

from flask import Flask, jsonify, request
import os
import json
from datetime import datetime

app = Flask(__name__)

# In-memory data store for demonstration
USERS = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "role": "admin"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "role": "user"},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "role": "user"}
]

PRODUCTS = [
    {"id": 1, "name": "Product A", "price": 99.99, "category": "electronics"},
    {"id": 2, "name": "Product B", "price": 49.99, "category": "books"},
    {"id": 3, "name": "Product C", "price": 149.99, "category": "electronics"}
]

# Configuration
DEBUG_MODE = os.environ.get("DEBUG_MODE", "False").lower() == "true"
API_VERSION = "v1"
LOG_FILE = "api_logs.json"

# Middleware for request logging
@app.before_request
def log_request():
    if DEBUG_MODE:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "method": request.method,
            "path": request.path,
            "ip": request.remote_addr,
            "user_agent": request.headers.get("User-Agent", "")
        }
        
        try:
            with open(LOG_FILE, "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        except Exception as e:
            print(f"Error writing to log: {e}")

# API Routes
@app.route(f"/api/{API_VERSION}/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok", "version": API_VERSION})

@app.route(f"/api/{API_VERSION}/users", methods=["GET"])
def get_users():
    """Get all users"""
    return jsonify({"users": USERS})

@app.route(f"/api/{API_VERSION}/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Get user by ID"""
    user = next((u for u in USERS if u["id"] == user_id), None)
    if user:
        return jsonify({"user": user})
    return jsonify({"error": "User not found"}), 404

@app.route(f"/api/{API_VERSION}/users", methods=["POST"])
def create_user():
    """Create a new user"""
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "email", "role")):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_id = max(u["id"] for u in USERS) + 1
    new_user = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"],
        "role": data["role"]
    }
    
    USERS.append(new_user)
    return jsonify({"user": new_user}), 201

@app.route(f"/api/{API_VERSION}/products", methods=["GET"])
def get_products():
    """Get all products"""
    category = request.args.get("category")
    if category:
        filtered_products = [p for p in PRODUCTS if p["category"] == category]
        return jsonify({"products": filtered_products})
    return jsonify({"products": PRODUCTS})

@app.route(f"/api/{API_VERSION}/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """Get product by ID"""
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product:
        return jsonify({"product": product})
    return jsonify({"error": "Product not found"}), 404

@app.route(f"/api/{API_VERSION}/products", methods=["POST"])
def create_product():
    """Create a new product"""
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "price", "category")):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_id = max(p["id"] for p in PRODUCTS) + 1
    new_product = {
        "id": new_id,
        "name": data["name"],
        "price": float(data["price"]),
        "category": data["category"]
    }
    
    PRODUCTS.append(new_product)
    return jsonify({"product": new_product}), 201

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Main entry point
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=DEBUG_MODE)