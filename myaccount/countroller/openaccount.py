from myaccount.routes import routes
from aiohttp import web
'''
Created on 2018��4��24��

@author: linqt
'''

@routes.post('/openacc')
async def handler(request):
    data = {'some': 'data'}
    return web.json_response(data)