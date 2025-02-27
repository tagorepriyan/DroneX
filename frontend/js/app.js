// app.js (Main File)
document.addEventListener("DOMContentLoaded", () => {
    console.log("DroneX Dashboard Loaded");

    document.querySelectorAll("nav a").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            document.querySelector(e.target.getAttribute("href")).scrollIntoView({
                behavior: "smooth"
            });
        });
    });
});