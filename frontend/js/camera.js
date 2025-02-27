function startLiveFeed() {
    const videoElement = document.getElementById("droneFeed");
    videoElement.src = "http://localhost:5000/live_feed"; // Set the correct live feed URL
}


function detectObjects() {
    fetch("http://localhost:5000/detect") // Ensure correct API endpoint
        .then(res => res.json())
        .then(data => console.log("Detection Data:", data))
        .catch(error => console.error("Error detecting objects:", error));
}

