# Multi-Mode Personal Assistant with Voice, Chat, and Face Detection

## 📌 Overview
This project is a **multi-mode AI-powered personal assistant** that can operate as:
1. **Voice Assistant (Bramii Mode)** – like Alexa/Siri, responds to your voice commands
2. **Text Chatbot Mode** – type queries for instant information
3. **Face Detection Mode** – real-time face tracking and focus detection

It combines **Natural Language Processing**, **Computer Vision**, and **API integration** into one Python application.

---

## 🎯 Purpose
This assistant can be used for:
- **Personal productivity** – quick searches, reminders, and weather updates
- **Education** – instant Wikipedia searches, fun facts, and quotes
- **Entertainment** – play music, tell jokes, or share random facts
- **Surveillance/Monitoring** – detect attention levels via Face Mode
- **Prototype for home automation** – can be extended to control smart devices

---

## 🚀 Features

### 1️⃣ Voice Assistant – Bramii Mode
- 🎤 **Voice commands** for hands-free control
- 🌐 Search **Wikipedia & Google**
- 🎵 Play **YouTube songs** via voice
- ⏸ **Pause**, ▶ **Resume**, and 🔊 **Control volume** of music
- 🌦 **Weather updates** for any city (OpenWeatherMap API)
- 😂 Tell **jokes**, 🧠 share **fun facts**, and 💬 give **motivational quotes**
- 🕒 Tells the **current time**
- 🔄 Switch **between modes by voice**

### 2️⃣ Text Chatbot Mode
- ⌨️ Type queries and get Wikipedia summaries + top Google links
- 📚 Great for research without using a microphone

### 3️⃣ Face Detection Mode
- 📷 Detects faces in real time via webcam
- 🟢 Shows **FOCUSED** or 🔴 **UNFOCUSED** status
- Can be adapted for attention tracking, security, or biometric projects

---

## 🛠 Installation

### Requirements
Install dependencies:
```bash
pip install opencv-python SpeechRecognition pyttsx3 wikipedia googlesearch-python pytube pywhatkit pygame pyjokes requests
```

### Clone Repository
```bash
git clone https://github.com/Bramhendra-C/multi-mode-AI-Computer-Vision-assistant-nature
cd multi-mode-AI-Computer-Vision-assistant-nature
```

---

## ▶ Usage

Run the **main program**:
```bash
python Main.py
```

Choose a mode:
1. **Chatbot Mode** – type your queries
2. **Bramii Mode** – voice-controlled assistant
3. **Face Detection Mode** – webcam-based tracking
4. **Exit** – quit the program

### Voice Commands Examples (Bramii Mode)
- `"time"` → tells the current time  
- `"play despacito on youtube"` → plays song  
- `"weather in London"` → gives current temperature  
- `"tell me a joke"` → tells a joke  
- `"fun fact"` → gives a random fun fact  
- `"quote of the day"` → motivational quote  
- `"switch to face detection"` → opens Face Mode  
- `"switch to chat mode"` → returns to text chatbot

---

## 📌 Notes
- Requires **microphone** for voice mode
- Requires **webcam** for face detection
- Internet connection needed for Wikipedia, Google, YouTube, and Weather

---

## 🛡 License
This project is open-source under the MIT License.

---

## 👨‍💻 Author
Developed by **Bramhendra** as a demonstration of combining **AI voice assistants** with **computer vision**.
