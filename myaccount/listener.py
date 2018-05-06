import myaccount.listenerpg as lis
'''
Created on  2018-04-25 11:08:35

@author: quantaolin
'''
async def openacclistener(app):
    app['openacc_listener'] = app.loop.create_task(lis.openacclistener(app))
    yield
    app['openacc_listener'].cancel()
    await app['openacc_listener']

def setup_listener(app):
    app.cleanup_ctx.append(openacclistener)