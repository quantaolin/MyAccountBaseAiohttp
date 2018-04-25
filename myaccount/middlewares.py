from aiohttp.web import middleware
from aiohttp import web
'''
Created on  2018-04-25 11:47:01

@author: quantaolin
'''
@middleware
async def middleware(request, handler):
    resp = await handler(request)
    if isinstance(resp,dict):
        return web.json_response(resp)
    elif isinstance(resp,str):
        return web.Response(text=resp)
    else :
        return resp
    
def setup_middlewares(app):
    app.middlewares.append(middleware)