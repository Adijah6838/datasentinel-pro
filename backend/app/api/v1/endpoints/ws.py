from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.ws.manager import manager

router = APIRouter()

@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text() # Keep connection open
    except WebSocketDisconnect:
        manager.disconnect(websocket)