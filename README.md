# 🎨 Stable Diffusion Powered Text-to-Image Generator

Transform your ideas into stunning visuals using AI! This project leverages **Stable Diffusion** and a **Flask-based web interface** to generate images from text prompts, with support for multiple languages.

---

## 🚀 Features

✨ Generate images from text using AI (Stable Diffusion)
🌍 Multi-language input support
🖥️ User-friendly web interface
⚡ Fast and lightweight Flask backend
🎯 Clean UI with responsive design
🔐 Secure API key handling using environment variables

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **AI Model:** Stable Diffusion (via Hugging Face API)
* **Libraries:** Requests, Pillow

---

## 📂 Project Structure

```
texttoimage/
│
├── app.py
├── multilang_texttoimg.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── home.html
│   ├── input.html
│   ├── login.html
│   └── signup.html
│
├── static/
│   └── css/
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```
git clone https://github.com/apurva693/Stable-Diffusion-Powered-Text-to-Image-Generator.git
cd Stable-Diffusion-Powered-Text-to-Image-Generator
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

Create a `.env` file in the root directory:

```
API_KEY=your_huggingface_api_key
```

⚠️ Never upload `.env` to GitHub

---

### 5️⃣ Run the Application

```
python app.py
```

---

### 6️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📸 Preview

*Add screenshots of your application here to showcase UI and functionality*

---

## 🔐 Security Best Practices

* API keys are stored securely using environment variables
* `.env` is excluded using `.gitignore`
* Sensitive data is never pushed to version control


> 🚀 Built with passion using Python, Flask, and AI
