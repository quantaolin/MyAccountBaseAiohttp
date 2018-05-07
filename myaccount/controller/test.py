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

@routes.get('/opeacclistentest')
def opeacclistentest(request):
    return "sucess"

@routes.get('/queryacctest')
@aiohttp_jinja2.template('queryacctest.html')
def queryacc(request):
    return {}

@routes.get('/rechargetest')
@aiohttp_jinja2.template('rechargetest.html')
def rechargetest(request):
    return {}