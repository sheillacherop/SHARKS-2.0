from flask import Flask, render_template, request, jsonify
import requests
from urllib.parse import urlparse
import os

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
        # 1. Forensic Handshake
        parsed = urlparse(target_url)
        domain = parsed.netloc.lower()
        verdict = "SAFE"
        if any(bad in domain for bad in ['.xyz', '.top', 'verify', 'win', 'bonus']):
            verdict = "MALICIOUS"

        # 2. Pothole Audit (Case-Insensitive Fix)
        response = requests.get(target_url, timeout=7, headers={'User-Agent': 'Mozilla/5.0'})
        h = {k.lower(): v for k, v in response.headers.items()} 
        
        potholes = {
            "csp": "ACTIVE" if 'content-security-policy' in h else "MISSING",
            "csrf": "SECURE" if 'set-cookie' in h and 'httponly' in h['set-cookie'].lower() else "INSECURE"
        }

        # 3. KRA Revenue Integrity
        content = response.text.lower()
        has_pay = any(m in content for m in ['ipay', 'pesapal', 'daraja', 'stk'])
        has_kra = any(m in content for m in ['kra.go.ke', 'etims', 'gavaconnect'])
        rev_status = "REVENUE LEAKAGE DETECTED" if (has_pay and not has_kra) else "CLEAN"

        # 4. Access Control (IDOR)
        query_params = parsed.query
        has_id = any(k in query_params.lower() for k in ['id', 'user', 'account', 'order'])
        idor_verdict = "VULNERABLE (IDOR RISK)" if has_id else "STABLE"

        return jsonify({
            "verdict": verdict,
            "csp": potholes["csp"],
            "csrf": potholes["csrf"],
            "revenue": rev_status,
            "idor": idor_verdict
        })

    except Exception as e:
        return jsonify({"error": f"Scan failed: {str(e)}"}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
