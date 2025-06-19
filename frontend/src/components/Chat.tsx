import React, { useState } from "react";

const Chat = () => {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleAsk = async () => {
    if (!input.trim()) {
      setError("Please enter a question.");
      return;
    }
    setError("");
    setLoading(true);
    try {
      const res = await fetch("http://localhost:8000/ask", {
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
    <div className="chat-container max-w-md mx-auto mt-10 p-6 bg-white shadow-lg rounded-lg">
      <h2 className="text-2xl font-bold mb-4 text-center">Weather Assistant</h2>
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask a weather question..."
        rows={4}
        maxLength={200}
        className="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      {error && <p className="text-red-500 text-sm mt-2">{error}</p>}
      <button
        onClick={handleAsk}
        disabled={loading}
        className={`mt-4 w-full px-4 py-2 rounded-lg text-white ${
          loading ? "bg-blue-300" : "bg-blue-500 hover:bg-blue-600"
        }`}
      >
        {loading ? (
          <span className="flex items-center justify-center">
            <svg
              className="animate-spin h-5 w-5 mr-2"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              ></circle>
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8v8H4z"
              ></path>
            </svg>
            Thinking...
          </span>
        ) : (
          "Ask"
        )}
      </button>
      <div className="mt-6 p-4 border rounded-lg bg-gray-50">
        <strong className="block mb-2 text-gray-700">Answer:</strong>
        <p className="text-gray-800">{response || "Your answer will appear here."}</p>
      </div>
    </div>
  );
};

export default Chat;