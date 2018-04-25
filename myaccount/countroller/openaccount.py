from myaccount.routes import routes
from aiohttp import web
'''
Created on 2018-04-25 11:08:35

@author: linqt
'''

@routes.post('/openacc')
async def openacc(request):
    data = {'some': 'data'}
    return web.json_response(data)