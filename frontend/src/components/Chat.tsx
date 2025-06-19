import React, { useState } from "react";

const Chat = () => {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    setLoading(true);
    try {
      //use this url for local testing http://localhost:8000/ask
      const res = await fetch("https://weather-api.victorioussea-d774307a.westeurope.azurecontainerapps.io/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: input }),
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (err) {
      setResponse("Error fetching response.");
    }
    setLoading(false);
  };

  return (
    <div className="chat-container">
      <h2>Weather Assistant</h2>
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask a weather question..."
        rows={4}
        className="w-full p-2 border"
      />
      <button onClick={handleAsk} className="mt-2 px-4 py-2 bg-blue-500 text-white">
        {loading ? "Thinking..." : "Ask"}
      </button>
      <div className="mt-4 p-2 border bg-gray-100">
        <strong>Answer:</strong>
        <p>{response}</p>
      </div>
    </div>
  );
};

export default Chat;
