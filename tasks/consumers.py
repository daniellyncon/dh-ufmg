import logging
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.db import close_old_connections

logger = logging.getLogger(__name__)


class TaskConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print('printando channel name')
        print(self.channel_name)
        await self.accept()
        await self.channel_layer.group_add("workflow", self.channel_name)
        logger.info(f'Added {self.channel_name} channel to workflow')
        close_old_connections()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discar("workflow", self.channel_name)
        logger.info(f'Removed {self.channel_name} channel to workflow')
        close_old_connections()

    async def workflow_update(self, event):
        await self.send_json(event)
        logger.info(f'Got message {event} at {self.channel_name}')
        close_old_connections()