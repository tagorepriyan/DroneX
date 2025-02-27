function controlDrone(command) {
    fetch(`http://localhost:5000/${command}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => console.log(`Drone Command (${command}):`, data.message))
    .catch(error => console.error("Error:", error));
}

// Example: Button event listener
document.getElementById("startDrone").addEventListener("click", () => controlDrone("start"));
document.getElementById("stopDrone").addEventListener("click", () => controlDrone("stop"));
