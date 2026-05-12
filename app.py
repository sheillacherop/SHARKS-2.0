from flask import Flask, render_template, request, jsonify
import requests
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    target_url = data.get('url', '')
    
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url

    try:
        # 1. Forensic Handshake (Identity Check)
        parsed = urlparse(target_url)
        domain = parsed.netloc.lower()
        verdict = "SAFE"
        if any(bad in domain for bad in ['.xyz', '.top', 'verify', 'win', 'bonus']):
            verdict = "MALICIOUS"

        # 2. Pothole Audit (Security Headers)
        response = requests.get(target_url, timeout=5)
        h = response.headers
        
        potholes = {
            "csp": "ACTIVE" if 'Content-Security-Policy' in h else "MISSING",
            "xss": "ACTIVE" if 'X-XSS-Protection' in h else "MISSING",
            "csrf": "SECURE" if 'Set-Cookie' in h and 'httponly' in h.get('Set-Cookie', '').lower() else "INSECURE"
        }

        # 3. KRA Revenue Integrity
        content = response.text.lower()
        has_pay = any(m in content for m in ['ipay', 'pesapal', 'daraja', 'stk'])
        has_kra = any(m in content for m in ['kra.go.ke', 'etims', 'gavaconnect'])
        
        rev_status = "CLEAN"
        if has_pay and not has_kra:
            rev_status = "REVENUE LEAKAGE DETECTED"

        return jsonify({
            "verdict": verdict,
            "potholes": potholes,
            "revenue": rev_status,
            "url": target_url
        })

    except:
        return jsonify({"error": "Site unreachable"}), 400

if __name__ == '__main__':
    app.run(debug=True)