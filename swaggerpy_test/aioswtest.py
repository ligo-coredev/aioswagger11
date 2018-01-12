import json
import asyncio
import aiohttp

from swaggerpy.client import AsyncSwaggerClient
from swaggerpy.http_client import AsynchronousHttpClient

loop = asyncio.get_event_loop()
http_client = AsynchronousHttpClient('remari', '@rip@$$', loop)

async def listen_ws():
    ws = await ari.events.eventWebsocket(app='hello')
    while True:
        msg = await ws.receive()
        if msg.tp == aiohttp.MsgType.text:
            msg_json = json.loads(msg.data)
            if msg_json['type'] == 'StasisStart':
                channelId = msg_json['channel']['id']
                await ari.channels.answer(channelId=channelId)
                await ari.channels.play(channelId=channelId,
                                  media='sound:hello-world')
                await ari.channels.continueInDialplan(channelId=channelId)

ari = AsyncSwaggerClient(None, None, loop=loop, http_client=http_client,
                         url="http://192.168.254.60:8088/ari/api-docs/resources.json")
loop.run_until_complete(ari.init())
loop.run_until_complete(listen_ws())
loop.run_until_complete(ari.close())
