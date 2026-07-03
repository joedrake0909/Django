from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Adding the created room to our channel layer
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        print("Websocket connection accepted")

    async def disconnect(self):
        await self.channel_layer.group_discard( self.room_group_name, self.channel_name )
