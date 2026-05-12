# SHARK 2.0 | Forensic Sentinel & Revenue Integrity Tool

**SHARK 2.0** is a full-stack forensic application designed to audit web infrastructure for security "potholes" and revenue leakage. Built with a focus on the Kenyan digital landscape, it identifies malicious handshake patterns and verifies KRA (Kenya Revenue Authority) integration integrity.

## 🦈 Core Features
* **Forensic Handshake:** Detects malicious TLDs (.xyz, .top) and phishing patterns in real-time.
* **Pothole Audit:** Scans for missing Security Headers (CSP, XSS-Protection, CSRF).
* **Revenue Integrity:** Identifies merchant sites processing payments (M-Pesa/iPay) without active tax compliance hooks.
* **Bento UI:** A minimalist, high-end dashboard for clear forensic reporting.

## 🛠️ Tech Stack
* **Backend:** Python (Flask)
* **Frontend:** Modern CSS (Bento Grid Layout), Vanilla JavaScript
* **Security:** Forensic URL parsing and Header analysis

## 🚀 Local Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/SHARK_2.0.git](https://github.com/YOUR_USERNAME/SHARK_2.0.git)
