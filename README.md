# 👁️ Real-Time Eye Drowsiness Detection System

A **real-time AI-powered system** for detecting eye drowsiness and fatigue using **Convolutional Neural Networks (CNN)** and the **OpenCV library**.
When the system detects that the eyes have been closed for an extended period, it plays an **alarm sound** to alert the user. This project also features a **web interface** for remote monitoring.

---

## ✨ Key Features

- 🎯 **Real-time detection** using OpenCV and Haar Cascades
- 🧠 **CNN model** trained on a dataset of open and closed eye images
- 🔊 **Alarm sound** triggers when eyes remain closed for too long
- 🌐 **Flask web interface** with live video streaming
- 📊 **Score-based system** to reduce false positives
- 🖥️ Compatible with **local cameras** (built-in webcam or USB)

---

## 🛠️ Tech Stack

- **Python**: The core programming language
- **TensorFlow/Keras**: For building and training the deep learning model
- **OpenCV**: For real-time image processing and face/eye detection
- **Flask**: For building the web interface and live video streaming
- **Pygame**: For playing the alarm sound
- **Numpy**: For numerical operations on images

---

## 🚀 Installation and Setup

Follow these steps to run the project:

**1. Clone the Repository:**
```bash
git clone https://github.com/your-username/drowsiness-detection.git
cd drowsiness-detection
```
*(Note: Replace `your-username` with your actual username)*

**2. Install Dependencies:**
It is recommended to create a virtual environment to isolate the packages.
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Then, install the required packages using the following command:
```bash
pip install -r requirements.txt
```

---

## 🔧 Usage

This project can be run in two ways:

**1. Standalone Mode:**
This mode displays the webcam feed directly in a window on your desktop. To run it, enter the following command in your terminal:
```bash
python "drowsiness detection.py"
```
Press the `q` key to quit the application.

**2. Web Application Mode:**
This mode launches a web interface that you can access from your browser. To start the Flask server, use this command:
```bash
python app.py
```
Then, open your browser and navigate to `http://127.0.0.1:5000` to see the live stream.

---

## 🗂 Project Structure

```
EYE-DETECTION/
│
├── data/                  # Image dataset for training and validation
│   ├── train/
│   └── valid/
│
├── haar cascade files/    # Haar Cascade classifier files
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_lefteye_2splits.xml
│   └── haarcascade_righteye_2splits.xml
│
├── models/                # Trained CNN model
│   └── cnnCat2.h5
│
├── templates/             # HTML templates for Flask
│   └── index.html
│
├── alarm.wav              # Alarm sound file
├── app.py                 # Main script for the Flask web application
├── drowsiness detection.py # Standalone script for drowsiness detection
├── model.py               # Script for training the model
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation (this file)
```



## 📸 Demo

![Drowsiness Detection Demo](demo.gif)


