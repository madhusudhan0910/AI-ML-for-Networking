# 🛡️ AI-ML-for-Networking: Real-Time SQL Injection & XSS Detection

A real-time machine learning-based detection tool for identifying **SQL Injection (SQLi)** and **Cross-Site Scripting (XSS)** attacks. Built with **FastAPI**, **Scikit-learn**, and **Redis** for asynchronous queue handling and deployed using **Docker**.

---

## 🎯 Overview

This project detects and classifies user inputs (such as URLs or strings) into categories like:

- **Benign**
- **SQL Injection**
- **XSS**
- **Malicious**

It provides both a **single payload tester** and a **file upload scanner**, with results displayed through a web interface in real time.

---

## 📽️ Demo Video

▶️ [Watch the Project Demo](https://drive.google.com/file/d/1_PKCcp-cYHY9LdThUTf281R591DWXcXA/view?usp=sharing)

---

## 🧰 Tech Stack

| Layer          | Technology                   |
|----------------|-------------------------------|
| Web Interface  | HTML, CSS, JavaScript         |
| Backend        | FastAPI (Python)              |
| ML Model       | Scikit-learn (RandomForest)   |
| Queue System   | Redis                         |
| Deployment     | Docker, Docker Compose        |

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/madhusudhan0910/AI-ML-for-Networking.git
cd AI-ML-for-Networking
```

---

### 2. Install Requirements (Optional for local run without Docker)

```bash
pip install -r requirements.txt
```

---

### 3. Train the ML Model

```bash
python app/train_model.py
```

> Make sure `sqlxss_mixed_dataset.csv` exists in the `data/` folder.

---

### 4. Start the Project Using Docker

```bash
docker-compose up --build
```

This will spin up:

- 🚀 FastAPI app at `http://localhost:8000`  
- 🧠 Redis instance  
- 🔁 Background consumer to process threats  

---

## 🌐 Web Interface Usage

Open `http://localhost:8000` in your browser.

You can:

- Paste a string or URL into the single input field to detect threats.
- Upload `.txt` or `.csv` files with multiple payloads.
- View results instantly, color-coded based on the classification.

---

## 📸 

![WhatsApp Image 2025-07-11 at 19 18 31_f007ea01](https://github.com/user-attachments/assets/aa7c8df5-c7ac-45b1-9ec6-5805c8451494)


---

## 🧪 Results

- ✅ Achieved **90%+ detection accuracy**
- ⚡ Real-time classification with low latency
- 🔄 End-to-end pipeline with FastAPI + Redis queue + frontend

---

## 📜 License

This project is licensed under the **MIT License**.


---

> _Secure your web layer with real-time ML-powered threat detection!_ 🛡️
