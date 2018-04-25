from aiohttp import web
'''
Created on 2018-04-25 11:08:35

@author: quantaolin
'''
routes = web.RouteTableDef()

def setup_routes(app):
    app.add_routes(routes)
    setup_static_routes(app)
    
def setup_static_routes(app):
    pass