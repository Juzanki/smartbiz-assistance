from fastapi.websockets import WebSocket
from typing import Dict, List


class WebSocketManager:
    def __init__(self):
        self.active_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, stream_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.setdefault(stream_id, []).append(websocket)

    def disconnect(self, stream_id: int, websocket: WebSocket):
        connections = self.active_connections.get(stream_id)
        if connections and websocket in connections:
            connections.remove(websocket)
            if not connections:
                del self.active_connections[stream_id]

    async def broadcast(self, stream_id: int, message: dict):
        connections = self.active_connections.get(stream_id, [])
        for connection in connections:
            try:
                await connection.send_json(message)
            except Exception:
                self.disconnect(stream_id, connection)
