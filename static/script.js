document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("user-input").addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});

function sendMessage() {
    let inputField = document.getElementById("user-input");
    let query = inputField.value.trim();
    if (!query) return;

    let chatBox = document.getElementById("chat-box");

    // Append user message
    let userMessage = document.createElement("div");
    userMessage.classList.add("message", "user");
    userMessage.innerText = query;
    chatBox.appendChild(userMessage);

    // Show typing indicator
    let typingIndicator = document.createElement("div");
    typingIndicator.classList.add("message", "bot", "typing-indicator");
    typingIndicator.innerText = "Thinking...";
    chatBox.appendChild(typingIndicator);

    inputField.value = ""; // Clear input field

    // Send request to backend
    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: query })
    })
    .then(response => response.json())
    .then(data => {
        // Remove typing indicator
        typingIndicator.remove();

        // Append bot response
        let botMessage = document.createElement("div");
        botMessage.classList.add("message", "bot");
        botMessage.innerText = data.response;
        chatBox.appendChild(botMessage);

        // Append sources in a smaller font
        if (data.sources.length > 0) {
            let sourcesMessage = document.createElement("div");
            sourcesMessage.classList.add("message", "bot");
            sourcesMessage.innerHTML = `<small>Sources: ${data.sources.join(", ")}</small>`;
            chatBox.appendChild(sourcesMessage);
        }

        // Auto-scroll to latest message
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error("Error:", error));
}
