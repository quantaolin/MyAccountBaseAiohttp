from myaccount.routes import routes
'''
Created on 2018-04-25 11:08:35

@author: linqt
'''

@routes.get('/openacc')
async def openacc(request):
    sqlstr="insert into bus.user (user_id,user_name,sex,card_num) values (%s,%s,%s,%s)"
    param=('42aq','Tom','02','4444444')
    async with request.app['db'].acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sqlstr,param)
            r= cur.rowcount
            print(r)
    data = {'result': r}
    return data