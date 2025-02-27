function updateMap(lat, lng) {
    let map = document.getElementById("map");
    map.innerHTML = `Location: ${lat}, ${lng}`;
}

function setDroneDestination(lat, lng) {
    fetch(`http://drone-api/navigate?lat=${lat}&lng=${lng}`, { method: "POST" })
        .then(res => res.json())
        .then(data => console.log("Navigating to: ", data));
}