async function runScan() {
    const url = document.getElementById('urlInput').value;
    if(!url) return;

    const res = await fetch('/scan', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({url: url})
    });
    const data = await res.json();
    
    document.getElementById('results').style.display = 'grid';
    document.getElementById('vText').innerText = data.verdict;
    document.getElementById('vText').className = data.verdict;
    document.getElementById('csp').innerText = data.potholes.csp;
    document.getElementById('sec').innerText = data.potholes.csrf;
    document.getElementById('kra').innerText = data.revenue;

    // --- ADD THIS LINE BELOW ---
    document.getElementById('idor').innerText = data.idor;
}
