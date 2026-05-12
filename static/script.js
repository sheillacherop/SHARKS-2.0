async function runScan() {
    const url = document.getElementById('urlInput').value;
    if(!url) return;

    // Reset UI
    document.getElementById('results').style.display = 'none';

    try {
        const res = await fetch('/scan', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({url: url})
        });
        
        const data = await res.json();

        if (data.error) {
            alert(data.error);
            return;
        }

        // Display Results
        document.getElementById('results').style.display = 'grid';
        
        // Match these exactly to the Python return labels
        document.getElementById('vText').innerText = data.verdict || "UNKNOWN";
        document.getElementById('csp').innerText = data.csp || "--";
        document.getElementById('sec').innerText = data.csrf || "--";
        document.getElementById('kra').innerText = data.revenue || "--";
        document.getElementById('idor').innerText = data.idor || "--";

    } catch (err) {
        console.error("Scan Error:", err);
        alert("Server connection lost. Restart your terminal!");
    }
}
