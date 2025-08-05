import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone

class ChannelActivityConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.channel_id = self.scope['url_route']['kwargs']['channel_id']
        self.channel_group_name = f'channel_{self.channel_id}'
        await self.channel_layer.group_add(self.channel_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.channel_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        await self.channel_layer.group_send(
            self.channel_group_name,
            {
                'type': 'channel_message',
                'message': f'[{timestamp}] {message}',
            }
        )

    async def channel_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))