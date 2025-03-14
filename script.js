document.addEventListener("DOMContentLoaded", () => {
    const uploadButton = document.querySelector(".btn");
    
    if (uploadButton) {
        uploadButton.addEventListener("click", (event) => {
            event.stopPropagation(); // Prevent event bubbling

            let fileInput = document.createElement("input");
            fileInput.type = "file";
            fileInput.style.display = "none";  // Hide the input element

            // Append the input element to the body and trigger the click event
            document.body.appendChild(fileInput);
            fileInput.click();

            // Handle file selection
            fileInput.addEventListener("change", () => {
                if (fileInput.files.length > 0) {
                    const file = fileInput.files[0];
                    const fileName = file.name;

                    // Show the file name on the page
                    const fileNameDisplay = document.createElement("p");
                    fileNameDisplay.textContent = "Selected File: " + fileName;
                    fileNameDisplay.classList.add("file-name");  // Optional: Add a class for styling
                    document.body.appendChild(fileNameDisplay);
                }

                // Clean up by removing the file input after use
                fileInput.remove();
            });
        });
    }
});
function sendToFlaskAPI(text) {
    fetch("http://127.0.0.1:5000/summarize", {  
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => document.getElementById("summaryResult").innerText = data.summary)
    .catch(error => alert("Error: " + error));
}
