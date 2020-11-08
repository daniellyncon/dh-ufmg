from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from tasks.consumers import TaskConsumer
from channels.auth import AuthMiddlewareStack


application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('notifications/', TaskConsumer),
            path('', AsgiHandler)
        ])
    ),

})
