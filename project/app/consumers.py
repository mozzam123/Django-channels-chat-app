import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("accepted")
        await self.send(text_data=json.dumps({
            'type': "connection established",
            'message': 'You are now connected'
        }))



