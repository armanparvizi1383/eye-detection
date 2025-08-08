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


