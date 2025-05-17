import os
import logging
from deepgram.utils import verboselogs
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os 
from fastapi import FastAPI
from deepgram import (
    DeepgramClient,
    SpeakOptions,
)

load_dotenv()

app = FastAPI()

def gemini_response(prompt):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are my English teacher. Identify the grammar mistakes that I made, and give me detailed feedback including corrections and explanations. "),
        contents=prompt
    )
    return response.text
     
def text_to_speech(llm_response):
    SPEAK_TEXT = {"text": llm_response}
    filename = "test.mp3"
    try:
        # STEP 1 Create a Deepgram client using the API key from environment variables
        deepgram = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))

        # STEP 2 Call the save method on the speak property
        options = SpeakOptions(
            model="aura-2-thalia-en",
        )

        response = deepgram.speak.rest.v("1").save(filename, SPEAK_TEXT, options)
        return response.to_json(indent=4)

    except Exception as e:
        print(f"Exception: {e}")

@app.post("/generate")
def generate_response(text: str):
    llm_response = gemini_response(text)
    text_to_speech(llm_response)

