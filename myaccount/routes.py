from aiohttp import web
'''
Created on 2018年4月21日

@author: quantaolin
'''
routes = web.RouteTableDef()

def setup_routes(app):
    app.add_routes(routes)
    setup_static_routes(app)
    
def setup_static_routes(app):
    pass