from channels.generic.websocket import AsyncWebsocketConsumer
import json
from . import models
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Connected...")
        await self.channel_layer.group_add("Chats", self.channel_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        chat = database_sync_to_async(models.Chats)(chat_message=json.loads(text_data)['chat_message'])
        chat.save()
        # await database_sync_to_async(models.Chats.objects.create)(chat_message=json.loads(text_data)['chat_message'])
        await self.channel_layer.group_send(
                "Chats",
                {
                    "type": "chat.message",
                    "chat": text_data,
                }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("Chats", self.channel_name)
        await self.close(close_code)
    
    
    async def chat_message(self, event):
        await self.send(json.dumps({
            "msg": f"{event['chat']}"
        }))
