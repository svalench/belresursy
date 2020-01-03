# from channels.routing import route_pattern_match
#
# channel_routing = [
#     route_pattern_match('http.request', 'vesovay.consumers.http_request_consumer')
# ]
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
import apps.vesovay.routing

from apps.vesovay.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            apps.vesovay.routing.websocket_urlpatterns
        )
    ),
})