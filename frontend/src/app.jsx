import React, { useState } from 'react';


function App() {

  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');

  const handleSubmit= (e) => {
    e.preventDefault()
    setOutputText(inputText)
  }


  return (
    <>


    <div className="container text-left">

      <h1 className='my-10'>Medical Ticket Optimizer</h1>

      <hr />
    
         

      <form onSubmit={handleSubmit}>
        <div className="row">

          <div className="col">
              <label htmlFor="ticket" className="h3">Enter ticket text here:</label> <br />
              {/* <textarea name="" id="ticket" rows="5" cols="40"></textarea> */}
              <textarea 
                id = "ticket"
                value={inputText} 
                rows = "5" cols = "30"
                onChange={(e) => setInputText(e.target.value)} 
                placeholder="Enter Ticket here..."
              />
 

          </div>

          <div className="col">
              <br /> <br />
              <button type="submit" className="btn btn-danger"> Echo </button>
          </div>

        </div>
        <br />
        <hr />
        <div className="row alight-left">
          <div className="col">
            <label htmlFor="Result" className="h3">Result</label> <br />

            <textarea 
              id = "Result"
              value={outputText} 
              rows = "5" cols = "30"
              readOnly 
              placeholder="Read only output"
            />

          </div>
        </div>


      </form>
    </div>

    </>
  )
}

export default App
