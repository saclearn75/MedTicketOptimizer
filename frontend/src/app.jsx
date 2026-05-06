

import React, { useState } from 'react';
import {analyzeTicket} from '../services/api.jsx'

function App() {

  const [inputText, setInputText] = useState('')
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit= async (e) => { // 1. Add async here
    console.log( ' handleSubmit - received text:'+ inputText)
    e.preventDefault()

    setIsLoading(true);
    setError("");

    try {
      // 2. Add await here to wait for the actual data
      const data = await analyzeTicket(inputText); 
      setResult(data)
      
      // 3. Now 'data' is the actual JSON from FastAPI
      const receivedText = JSON.stringify(data, null, 3);
      console.log(receivedText);
      
    } catch (error) {
        console.error("Error analyzing ticket:", error);
          Error("Error: Could not reach the server.");
        setResult(null);
    }  finally {
        setIsLoading(false);
    }

  }


  return (
    <>


    <div className="container text-left">

      <h1 className='my-10'>Medical Ticket Optimizer</h1>

      <hr />
          

      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="ticket" className="form-label h4">
            Enter ticket text here
          </label>

          <textarea
            id="ticket"
            className="form-control"
            value={inputText}
            rows="10"
            onChange={(e) => {
              setInputText(e.target.value);
              setResult(null);
              setError("");
            }}
            placeholder="Paste the healthcare incident ticket here..."
          />
        </div>

        <button
          type="submit"
          className="btn btn-secondary w-100"
          disabled={!inputText.trim() || isLoading}
        >
          {isLoading ? "Analyzing..." : "Process"}
        </button>
      </form>

      {result && (
        <div className="mt-4">
          <h2>Results</h2>

          <div className="card mb-3">
            <div className="card-body">
              <h3 className="h5">Classification</h3>
              <pre>{JSON.stringify(result.classification, null, 2)}</pre>
            </div>
          </div>

          <div className="card mb-3">
            <div className="card-body">
              <h3 className="h5">Extracted Info</h3>
              <pre>{JSON.stringify(result.extracted_info, null, 2)}</pre>
            </div>
          </div>

          <div className="card mb-3">
            <div className="card-body">
              <h3 className="h5">Recommendation</h3>
              <pre>{JSON.stringify(result.recommendation, null, 2)}</pre>
            </div>
          </div>
        </div>
      )}
  </div>

    </>
  )
}

export default App
