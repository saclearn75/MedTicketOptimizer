// frontend/src/services/api.js
export async function analyzeTicket(ticketText) {
  const response = await fetch("http://localhost:5173/analyze-ticket", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ ticket_text: ticketText }),
  });

  if (!response.ok) {
    throw new Error("Failed to analyze ticket");
  }

  return response.json();
}