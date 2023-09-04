document.addEventListener("DOMContentLoaded", function () {
    const canvas = document.getElementById("drawingCanvas");
    const context = canvas.getContext("2d");
    const predictButton = document.getElementById("predictButton");
    const predictionResult = document.getElementById("predictionResult");

    let isDrawing = false;

    canvas.addEventListener("mousedown", () => {
        isDrawing = true;
        context.beginPath();
    });

    canvas.addEventListener("mousemove", (e) => {
        if (!isDrawing) return;
        context.lineWidth = 20;
        context.lineCap = "round";
        context.strokeStyle = "black";
        context.lineTo(e.clientX - canvas.getBoundingClientRect().left, e.clientY - canvas.getBoundingClientRect().top);
        context.stroke();
    });

    canvas.addEventListener("mouseup", () => {
        isDrawing = false;
        context.closePath();
    });

    predictButton.addEventListener("click", () => {
            console.log("this fucking me");

        const imageData = canvas.toDataURL("image/png"); // Convert canvas content to base64 image data

        fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ image_data: imageData }),
        })
            .then((response) => response.json())
            .then((data) => {
                predictionResult.textContent = `Predicted Digit: ${data.prediction}`;
            });
    });
});
