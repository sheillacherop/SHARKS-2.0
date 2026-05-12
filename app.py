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
        # 1. Forensic Handshake (Identity Check)
        parsed = urlparse(target_url)
        domain = parsed.netloc.lower()
        verdict = "SAFE"
        if any(bad in domain for bad in ['.xyz', '.top', 'verify', 'win', 'bonus']):
            verdict = "MALICIOUS"

      

        # 3. KRA Revenue Integrity
        content = response.text.lower()
        has_pay = any(m in content for m in ['ipay', 'pesapal', 'daraja', 'stk'])
        has_kra = any(m in content for m in ['kra.go.ke', 'etims', 'gavaconnect'])
        
        rev_status = "CLEAN"
        if has_pay and not has_kra:
            rev_status = "REVENUE LEAKAGE DETECTED"

        # 4. IDOR / Parameter Audit (The Bundle Theft Detector)
        query_params = parsed.query
        has_id_param = any(key in query_params.lower() for key in ['id', 'user', 'account', 'order'])
        
        idor_verdict = "STABLE"
        if has_id_param:
            idor_verdict = "VULNERABLE TO PARAMETER SWAPPING (IDOR)"

        return jsonify({
            "verdict": verdict,
            "potholes": potholes,
            "revenue": rev_status,
            "idor": idor_verdict,  # Send this to the frontend
            "url": target_url
        })

    except Exception as e:
        return jsonify({"error": f"Site unreachable: {str(e)}"}), 400

# --- UPDATED START BLOCK FOR RENDER ---
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
