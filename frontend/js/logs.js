function fetchFlightLogs() {
    fetch("http://drone-api/logs")
        .then(res => res.json())
        .then(logs => {
            let logContainer = document.getElementById("logs");
            logContainer.innerHTML = logs.map(log => `<p>${log}</p>`).join("\n");
        });
}
