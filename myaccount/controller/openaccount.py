from myaccount.routes import routes
'''
Created on 2018-04-25 11:08:35

@author: linqt
'''

@routes.get('/openacc')
async def openacc(request):
    sqlstr="insert into bus.user (user_id,user_name,sex,card_num) values ('123456','Jack','01','124124151233')"
    async with request.app['db'].acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sqlstr)
            r= cur.rowcount
            print(r)
    data = {'result': r}
    return data