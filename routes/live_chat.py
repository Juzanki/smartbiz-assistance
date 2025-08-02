from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List, Dict
import json

router = APIRouter(tags=["Live Chat"])


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[WebSocket, str] = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections[websocket] = username
        await self.broadcast(f"🔵 {username} joined the chat.")

    def disconnect(self, websocket: WebSocket):
        username = self.active_connections.get(websocket, "Unknown")
        self.active_connections.pop(websocket, None)
        return username

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    async def broadcast_json(self, payload: dict):
        for connection in self.active_connections:
            await connection.send_json(payload)


manager = ConnectionManager()


@router.websocket("/ws/live/chat/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    """
    Real-time group chat for live sessions (WebSocket).
    Clients must connect with a username.
    """
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            message = {
                "from": username,
                "text": data,
                "type": "message"
            }
            await manager.broadcast_json(message)
    except WebSocketDisconnect:
        left_user = manager.disconnect(websocket)
        await manager.broadcast(f"🔴 {left_user} left the chat.")
