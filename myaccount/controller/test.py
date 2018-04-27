from myaccount.routes import routes
import aiohttp_jinja2
'''
Created on  2018-04-27 14:02:16

@author: quantaolin
'''


@routes.get('/openacctest')
@aiohttp_jinja2.template('openacctest.html')
def openacc(request):
    return {}

@routes.get('/queryacctest')
@aiohttp_jinja2.template('queryacctest.html')
def queryacc(request):
    return {}