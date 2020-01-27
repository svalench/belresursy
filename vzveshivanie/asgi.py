"""
ASGI config for vzveshivanie project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

# import os
#
# from django.core.asgi import get_asgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vzveshivanie.settings')
#
# application = get_asgi_application()


import os
import django
# import uvicorn
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vzveshivanie.settings")
django.setup()
application = get_default_application()

# # if __name__ == '__main__':
#     # from socketio.server import Socket
# import socketio
# sio = socketio.AsyncServer(async_mode='asgi')
# # app = socketio.WSGIApp(application)
# application = socketio.ASGIApp(sio, application)
#
#
#
# @sio.on('connect', namespace='/test')
# async def test_connect(sid, environ):
#     print(environ)
#     await sio.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid,
#              namespace='/test')
#
#
# @sio.on('disconnect', namespace='/test')
# async def test_disconnect(sid):
#     print('Client disconnected')