from openai import OpenAI
import json

import tools.classifier as classifier
import tools.extractor as extractor 
import tools.recommendor as recommendor

from pydantic import BaseModel


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Ticket (BaseModel):
    text: str|None = ''


@app.get('/')
def homePage ():
    return "Medical Ticket Classifier"

@app.post('/ticket/')
def analyze_ticket(ticket:Ticket):
    if not ticket.text:
        ticket.text = 'Enter some valid text'
        return ticket 
    
    classification = classifier.classify_ticket(ticket.text)
    info =extractor.extract_info(ticket.text)
    next_steps =recommendor.recommend_next_steps(classification, info)

    return [classification, info, next_steps]



if __name__=='__main__':
        ticket =Ticket(text="Patient attempted to walk unassisted, fell near bedside, ")

        classification, info, next_steps = analyze_ticket(ticket=ticket)

        print (f'{classification=}, \n\n {info=}, \n\n {next_steps=}')

