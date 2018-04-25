from myaccount.routes import routes
'''
Created on 2018-04-25 11:08:35

@author: linqt
'''

@routes.get('/openacc')
async def openacc(request):
    data = {'some': 'data'}
    return data