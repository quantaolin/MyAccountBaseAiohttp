import aiomysql
'''
Created on  2018-04-25 11:08:35

@author: quantaolin
'''
async def mysql_engine(app):
    conf = app['config']['mysql']
    pool = await aiomysql.create_pool(
        host=conf['host'], 
        port=conf['port'],
        db=conf['db'],
        user=conf['user'], 
        password=conf['password'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
        connect_timeout=conf['connect_timeout'],
        autocommit=False,
        init_command='select 1 from dual',
        loop=app.loop)
    app['db'] = pool
    yield
    app['db'].close()
    await app['db'].wait_closed()
    
def setup_engine(app):
    app.cleanup_ctx.append(mysql_engine)
    
async def excute_insertorupdate(db,sqlstr,param):
    async with db.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sqlstr,param)
            r=cur.rowcount
            await conn.commit()
    return r

async def excute_select_dic(db,sqlstr,param):
    async with db.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sqlstr,param)
            r= await cur.fetchall()
    return r