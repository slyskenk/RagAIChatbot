const sendBtn = document.getElementById("send-btn");
const questionInput = document.getElementById("question");
const chatBox = document.getElementById("chat-box");

sendBtn.addEventListener("click", sendQuestion);
questionInput.addEventListener("keypress", function(e) {
    if(e.key === "Enter") sendQuestion();
});

function appendMessage(msg, className) {
    const div = document.createElement("div");
    div.className = `chat-message ${className}`;
    div.innerText = msg;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendQuestion() {
    const question = questionInput.value.trim();
    if (!question) return;
    appendMessage(question, "user-msg");
    questionInput.value = "";

    appendMessage("Typing...", "bot-msg");
    const response = await fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question})
    });
    const data = await response.json();
    chatBox.lastChild.innerText = data.answer;
}
