from fastapi import APIRouter, HTTPException
from app.services.gemini_service import create_chat, get_chat_response

router = APIRouter()

# Store active chat sessions
chat_sessions = {}

@router.post("/chat/{session_id}")
async def chat(session_id: str, message: str):
    try:
        # Get or create chat session
        if session_id not in chat_sessions:
            chat_sessions[session_id] = create_chat()
        
        chat = chat_sessions[session_id]
        
        # Get response with thoughts
        result = await get_chat_response(chat, message)
        
        return {
            "thoughts": result["thoughts"],
            "response": result["response"]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 