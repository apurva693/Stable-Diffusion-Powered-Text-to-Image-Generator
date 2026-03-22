import os
from flask import Flask, request, render_template, jsonify, redirect, url_for
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from io import BytesIO
from PIL import Image
import base64
from multilang_texttoimg import get_translation, generate_image, initialize_model
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# MongoDB Connection using URI from .env file
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client["texttoimage"]  # Replace with your database name
users_collection = db["users"]  # Replace with your collection name

# Initialize Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Initialize the image generation model globally
image_gen_model = initialize_model()

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email').lower()
        password = request.form.get('password')

        # Ensure all fields are filled
        if not username or not email or not password:
            return "All fields are required!"

        # Check if the username is already taken
        existing_username = users_collection.find_one({"username": username})
        if existing_username:
            return "Username already exists! Please choose another."

        # Check if the email is already registered
        existing_user = users_collection.find_one({"email": email})
        if existing_user:
            return "Email is already registered! Please login."

        # Hash the password before storing it
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Insert the new user into the database
        users_collection.insert_one({
            "username": username,
            "email": email,
            "password": hashed_password  # Store the hashed password
        })
        return redirect(url_for('login'))

    return render_template('signup.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')  # Use 'username' for login
        password = request.form.get('password')

        # Ensure all fields are filled
        if not username or not password:
            return "Both username and password are required!"

        # Fetch user from the database using the username
        user = users_collection.find_one({"username": username})
        if not user:
            return "Invalid credentials! Please try again."

        # Check if the provided password matches the hashed password
        if not bcrypt.check_password_hash(user['password'], password):
            return "Invalid credentials! Please try again."

        # Redirect to the input page upon success
        return render_template('input.html')

    return render_template('login.html')

# Image Generation Route
@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    try:
        # Translate and generate the image
        translation = get_translation(text, "en")
        image = generate_image(translation, image_gen_model)

        # Convert the image to base64 string
        img_io = BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)
        base64_image = base64.b64encode(img_io.getvalue()).decode('utf-8')

        # Render the image on the input page
        return render_template('input.html', image_data=base64_image)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
