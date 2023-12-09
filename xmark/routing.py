from channels.routing import ChannelNameRouter, ProtocolTypeRouter, URLRouter
from django.urls import path
from pomoman import consumers

# websocket_urlpatterns = [
#     path("ws/twitch/", consumers.TwitchConsumer.as_asgi()),
# ]
#
# application = ProtocolTypeRouter(
#     {
#         "websocket": URLRouter(websocket_urlpatterns),
#         "channel": ChannelNameRouter(
#             {
#                 "twitch-listener": consumers.TwitchChatListener.as_asgi(),
#                 "twitch-irc": consumers.TwitchConsumer,
#             }
#         ),
#     }
# )
