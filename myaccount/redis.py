import asyncio
import aioredis
'''
Created on  2018-04-25 11:08:35

@author: quantaolin
'''
async def redis_pool(app):
    conf = app['config']['redis']
    pool = await aioredis.create_pool(
        (conf['host'],conf['port']),
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
        create_connection_timeout=None, 
        loop=app.loop)
    app['redis'] = pool
    yield
    app['redis'].close()
    await app['redis'].wait_closed()
    
def setup_redis(app):
    app.cleanup_ctx.append(redis_pool)