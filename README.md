⭐ Star this repo if you find it useful!

# 🔐 Automated Web Vulnerability Scanner

An intelligent and automated web vulnerability scanning system designed to detect security flaws such as XSS, SQL Injection, IDOR, and Path Traversal using context-aware and adaptive techniques.

🌐 https://recon-and-enum-system-v1.vercel.app/ 🌐
---

## 📌 Overview

This project focuses on improving web application security by automating vulnerability detection.  
Unlike traditional scanners, it uses **context-aware fuzzing and adaptive analysis** to provide more accurate and real-world results.

---

## ✨ Features

- 🔍 Intelligent Reconnaissance
- 🌐 Advanced Attack Surface Mapping
- 🔐 Authentication & Session Analysis
- 🧠 Context-Aware Vulnerability Detection
- ⚡ Adaptive Fuzzing Engine
- 📊 Real-Time Dashboard
- 📄 Automated Report Generation
- 🎯 Reduced False Positives

---

## 🧠 How It Works

1. User provides target URL  
2. System performs reconnaissance (collects endpoints)  
3. Identifies parameters and attack surface  
4. Applies context-aware payloads  
5. Adapts payloads based on responses  
6. Analyzes vulnerabilities  
7. Displays results in dashboard + report  

---
⚙️ Installation & Setup
🔹 1. Clone Repository
    git clone https://github.com/Cy83r80ii/Recon-and-Enum-System-V1.git
    cd Recon-and-Enum-System-V1 
🔹 2. Setup Backend

    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
🔹 3. Setup Frontend

    cd frontend
    npm install
    npm start

## 🧩 Modules

- Intelligent Reconnaissance Engine  
- Attack Surface Mapping  
- Authentication Analysis  
- Vulnerability Decision Engine  
- Context-Aware Fuzzing  
- Adaptive Fuzzing  
- Correlation Analysis  
- Reporting Module  

---

## 🛠️ Technologies Used

### Backend
- Python  
- FastAPI  
- Asyncio  

### Frontend
- React.js  
- HTML  
- CSS  
- JavaScript  

---
▶️ How to Use

    Open the application in browser

    Enter target URL

    Start scan

    Monitor real-time progress

    View results and reports

🤝 Contribution

Feel free to fork, contribute, and improve this project.
📜 License

This project is for educational and research purposes.

## 📚 Libraries & Tools

- requests / httpx → HTTP handling  
- BeautifulSoup / lxml → Parsing  
- Axios → API communication  
- Recharts → Data visualization  
- ReportLab → PDF generation  
- Nuclei → Vulnerability templates  

---

## 📊 Language Usage

```text
Python        ████████████████ 60%
JavaScript    ██████████       25%
HTML/CSS      ██████           15%
