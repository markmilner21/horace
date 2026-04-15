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

/* =========================
   🎤 Speech Recognition
   ========================= */

let recognition;
let isListening = false;

function startListening() {
  if (isListening) return;

  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

  if (!SpeechRecognition) {
    alert("Speech recognition not supported in this browser");
    return;
  }

  isListening = true;

  recognition = new SpeechRecognition();
  recognition.lang = "en-US";
  recognition.interimResults = false;

  showListening();

  recognition.onresult = function (event) {
    const transcript = event.results[0][0].transcript;

    document.getElementById("user-input").value = transcript;
    sendMessage();
  };

  recognition.onerror = function (event) {
    console.error(event.error);
    isListening = false;
  };

  recognition.onend = function () {
    isListening = false;
  };

  recognition.start();
}

function showListening() {
  addMessage("🎤 Listening...", "horace");
}

/* =========================
   🚀 Chat Flow
   ========================= */

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
    body: JSON.stringify({ text }),
  });

  const data = await res.json();

  removeTyping();

  const finalScore = data.final_score
  ? Math.round(data.final_score * 100)
  : 0;

  const contentScore = data.content_score
  ? Math.round(data.content_score * 100)
  : 0;

  const brevityScore = data.brevity_score
  ? Math.round(data.brevity_score * 100)
  : 0;

  const styleScore =
  data.style_score !== undefined
    ? Math.round(data.style_score * 100)
    : 0;

    setTimeout(() => {
    if (data.model_answer) {
        addMessage(data.model_answer, "horace");
        addMessage(`Overall score: ${finalScore}%`, "horace");
        addMessage(
            `Content: ${contentScore}% | Brevity: ${brevityScore}% | Style: ${styleScore}%`,
            "horace"
        );
    }

    if (data.next_question) {
        addMessage(data.next_question, "horace");
    } else {
        addMessage("Interview complete.", "horace");
  }
  }, 400);
}

loadFirstQuestion();