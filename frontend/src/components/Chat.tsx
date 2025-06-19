// Chat component
import { useState } from "react";
export default function Chat() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");
  const ask = async () => {
    const res = await fetch("/ask", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ question: input })
    });
    const data = await res.json();
    setResponse(data.response);
  };
  return (<div><input value={input} onChange={e => setInput(e.target.value)} /><button onClick={ask}>Ask</button><p>{response}</p></div>);
}