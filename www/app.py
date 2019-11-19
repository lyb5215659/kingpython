import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

import orm
from models import User, Blog, Comment


def index(request):
	return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})

async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET','/',index)
	srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000')
	test()
	return srv

def test():
	yield from orm.create_pool(user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

for x in test():
    pass

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()	