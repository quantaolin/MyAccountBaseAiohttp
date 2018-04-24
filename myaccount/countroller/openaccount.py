from myaccount.routes import routes
from aiohttp import web
'''
Created on 2018Äê4ÔÂ24ÈÕ

@author: linqt
'''

@routes.post('/openacc')
async def openacc(request):
    data = {'some': 'data'}
    return web.json_response(data)