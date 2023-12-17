"""
ASGI config for chatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack #Project still works regardless of this issue. It's a deprecated version issue but it still works in this version.
from channels.routing import ProtocolTypeRouter, URLRouter #Project still works regardless of this issue. It's a deprecated version issue but it still works in this version.
import room.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )
})
