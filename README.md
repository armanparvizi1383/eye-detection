# 👁️ Real-Time Eye Drowsiness Detection System

A **real-time AI-powered system** for detecting eye drowsiness and fatigue using **CNN (Convolutional Neural Networks)** and **OpenCV Haarcascade**.  
When the system detects prolonged eye closure, it triggers an **alarm sound** to alert the user.  
Includes a **Flask web interface** for remote monitoring.

---

## 🚀 Features

- 🎯 **Real-time detection** using OpenCV & Haar Cascade
- 🧠 **CNN model** trained on open/closed eye dataset
- 🔊 **Alarm sound** when eyes remain closed for too long
- 🌐 **Flask web interface** with live video streaming
- 📊 **Score-based detection** to reduce false alarms
- 🖥️ Works with **local camera** (USB / built-in webcam)

---

## 🗂 Project Structure

EYE-DETECTION/
│
├── data/ # Dataset (train & validation images)
│ ├── train/
│ │ ├── closed/
│ │ └── open/
│ └── valid/
│ ├── closed/
│ └── open/
│
├── haar cascade files/ # Haarcascade XML classifiers
│ ├── haarcascade_frontalface_alt.xml
│ ├── haarcascade_lefteye_2splits.xml
│ └── haarcascade_righteye_2splits.xml
│
├── models/ # Trained CNN models
│ └── cnnCat2.h5
│
├── templates/ # Flask HTML templates
│ └── index.html
│
├── alarm.wav # Alarm sound
├── app.py # Flask web app
├── drowsiness detection.py # Standalone detection script
├── model.py # Model training script
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/eye-detection.git
cd eye-detection
2️⃣ Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🏋️‍♂️ Training the Model
If you want to retrain the model:

bash
Copy
Edit
python model.py
The trained model will be saved in:

bash
Copy
Edit
models/cnnCat2.h5
🖥️ Running the Application
Option 1: Run the detection script directly
bash
Copy
Edit
python "drowsiness detection.py"
Opens your webcam and starts real-time detection.

Option 2: Run Flask Web App
bash
Copy
Edit
python app.py
Then open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000/
You can start/stop the camera from the web interface.

🎮 How It Works
Face & Eye Detection

Uses Haarcascade classifiers to locate eyes in the frame.

Eye State Prediction

Each eye image is passed to the CNN model (trained on open/closed eyes).

Drowsiness Scoring

If both eyes are closed, the score increases; if open, the score decreases.

Alert Trigger

When the score exceeds a threshold, an alarm sound is played.

📸 Demo
Eye State	Detection Result
👁️ Open	✅ Safe
😴 Closed	🚨 Alarm Triggered

(Add your own GIFs or screenshots here)

🛠 Tech Stack
Python 3.x

OpenCV

TensorFlow / Keras

Flask

Pygame (for sound alerts)

📄 License
This project is licensed under the MIT License - feel free to use and modify it.

👤 Author
Arman Parvizi
📧 Contact: your-email@example.com
🌐 GitHub: your-username

yaml
Copy
Edit
