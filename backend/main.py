from openai import OpenAI
import json


import tools.classifier as classifier
import tools.extractor as extractor 
import tools.recommendor as recommendor

from pydantic import BaseModel
from typing import Any
import os
from dotenv import load_dotenv, find_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins=origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Ticket (BaseModel):
    text: str|None = ''

class AnalyzeTicketResponse(BaseModel):
    classification: dict[str, Any]
    extracted_info: dict[str, Any]
    recommendation: dict[str, Any]


@app.get('/')
def homePage ():
    return "Medical Ticket Classifier"


@app.post('/ticket1/')
def analyze_ticket_echo(ticket:Ticket):
     print (f'     received from page: {ticket.text}')
     return ticket


@app.post('/ticket/')
def analyze_ticket(ticket:Ticket):
    if not ticket.text:
        ticket.text = 'Enter some valid text'
        return ticket 
    
    print (f'analyze_ticket: received text: {ticket.text}')
    # return ticket
    classification = classifier.classify_ticket(ticket.text)
    info =extractor.extract_info(ticket.text)
    next_steps =recommendor.recommend_next_steps(classification, info)
    print (f'{classification=}, \n {info=}, \n {next_steps=}')
    return AnalyzeTicketResponse(
        classification=classification,
        extracted_info=info,
        recommendation=next_steps,
    )


if __name__=='__main__':
        ticket =Ticket(text="Patient attempted to walk unassisted, fell near bedside, ")

        classification, info, next_steps = analyze_ticket(ticket=ticket)

        print (f'{classification=}, \n\n {info=}, \n\n {next_steps=}')

