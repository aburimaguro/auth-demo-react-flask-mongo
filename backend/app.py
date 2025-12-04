import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
from auth_utils import (
    hash_password, check_password,
    create_access_token, create_refresh_token, decode_token
)

load_dotenv()

app = Flask(__name__)
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": FRONTEND_URL}})

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/auth_demo")
client = MongoClient(MONGO_URI)
db = client.get_default_database()
users_col = db["users"]
# Ensure unique index on email
users_col.create_index("email", unique=True)

COOKIE_NAME = "refresh_token"

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    email = (data.get("email") or "").strip().lower()
    password = data.get("password", "")
    name = data.get("name", "")

    if not email or not password:
        return jsonify({"error": "email and password required"}), 400

    hashed = hash_password(password)
    doc = {"email": email, "password": hashed, "name": name, "created_at": None}
    try:
        result = users_col.insert_one(doc)
    except Exception:
        return jsonify({"error": "email already registered"}), 409

    user_id = str(result.inserted_id)
    access_token = create_access_token(user_id)
    refresh_token = create_refresh_token(user_id)

    resp = jsonify({"message": "registered", "access_token": access_token})
    resp.set_cookie(
        COOKIE_NAME,
        refresh_token,
        httponly=True,
        samesite="Lax",
        secure=False,  # set True in production under HTTPS
        max_age=int(os.getenv("JWT_REFRESH_EXPIRES_SECONDS", 1209600))
    )
    return resp, 201

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email = (data.get("email") or "").strip().lower()
    password = data.get("password", "")

    user = users_col.find_one({"email": email})
    if not user:
        return jsonify({"error": "invalid credentials"}), 401

    if not check_password(password, user["password"]):
        return jsonify({"error": "invalid credentials"}), 401

    user_id = str(user["_id"])
    access_token = create_access_token(user_id)
    refresh_token = create_refresh_token(user_id)

    resp = jsonify({"message": "logged in", "access_token": access_token})
    resp.set_cookie(
        COOKIE_NAME,
        refresh_token,
        httponly=True,
        samesite="Lax",
        secure=False,
        max_age=int(os.getenv("JWT_REFRESH_EXPIRES_SECONDS", 1209600))
    )
    return resp

@app.route("/api/refresh", methods=["POST"])
def refresh():
    refresh_token = request.cookies.get(COOKIE_NAME)
    if not refresh_token:
        return jsonify({"error": "no refresh token"}), 401

    payload = decode_token(refresh_token)
    if not payload or payload.get("type") != "refresh":
        return jsonify({"error": "invalid refresh token"}), 401

    user_id = payload.get("sub")
    user = users_col.find_one({"_id": ObjectId(user_id)})
    if not user:
        return jsonify({"error": "user not found"}), 404

    access_token = create_access_token(user_id)
    return jsonify({"access_token": access_token})

@app.route("/api/logout", methods=["POST"])
def logout():
    resp = jsonify({"message": "logged out"})
    resp.set_cookie(COOKIE_NAME, "", httponly=True, samesite="Lax", secure=False, max_age=0)
    return resp

def get_current_user_from_auth_header():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return None
    token = auth.split(" ", 1)[1]
    payload = decode_token(token)
    if not payload or payload.get("type") != "access":
        return None
    user_id = payload.get("sub")
    user = users_col.find_one({"_id": ObjectId(user_id)}, {"password": 0})
    return user

@app.route("/api/me", methods=["GET"])
def me():
    user = get_current_user_from_auth_header()
    if not user:
        return jsonify({"error": "unauthorized"}), 401
    user["_id"] = str(user["_id"])
    return jsonify({"user": user})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=(os.getenv("FLASK_ENV")=="development"))

