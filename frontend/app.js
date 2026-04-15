const API = "http://127.0.0.1:8000";

function addMessage(text, sender) {
  const box = document.getElementById("chat-box");

  const div = document.createElement("div");
  div.className = `message ${sender}`;
  div.innerText = text;

  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
}

function showTyping() {
  const box = document.getElementById("chat-box");

  const div = document.createElement("div");
  div.className = "message horace typing";
  div.id = "typing";
  div.innerText = "Horace is typing...";

  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
}

function removeTyping() {
  const el = document.getElementById("typing");
  if (el) el.remove();
}

async function loadFirstQuestion() {
  const res = await fetch(`${API}/question`);
  const data = await res.json();

  addMessage(data.question, "horace");
}

async function sendMessage() {
  const input = document.getElementById("user-input");
  const text = input.value.trim();

  if (!text) return;

  addMessage(text, "user");
  input.value = "";

  showTyping();

  const res = await fetch(`${API}/answer`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });

  const data = await res.json();

  removeTyping();

  setTimeout(() => {
    if (data.next_question) {
      addMessage(data.next_question, "horace");
    } else {
      addMessage("Interview complete.", "horace");
    }
  }, 400);
}

loadFirstQuestion();