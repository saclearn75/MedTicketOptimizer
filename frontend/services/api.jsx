// frontend/src/services/api.js
export async function analyzeTicket(ticketText) {
    console.log ('sending text :'+ticketText)
  const response = await fetch("http://localhost:8000/ticket", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ "text": ticketText }),
  });

  if (!response.ok) {
    throw new Error("Failed to analyze ticket");
  }
//   console.log ('received response: '+ response.json())
  return response.json();
}