import aiomysql
'''
Created on  2018-04-25 11:08:35

@author: quantaolin
'''
async def init_mysql(app):
    conf = app['config']['mysql']
    pool = await aiomysql.create_pool(
        host=conf['host'], 
        port=conf['port'],
        user=conf['user'], 
        password=conf['password'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
        connect_timeout=conf['connect_timeout'],
        autocommit=True,
        init_command='select 1 from dual',
        db='mysql', 
        loop=app.loop)
    app['db'] = pool
    
async def close_mysql(app):
    app['db'].close()
    await app['db'].wait_closed()