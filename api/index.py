from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from google import genai
from app.services.gemini_service import create_chat, get_chat_response
from app.routers import chat

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Gemini client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Include routers
app.include_router(chat.router, prefix="/api")
