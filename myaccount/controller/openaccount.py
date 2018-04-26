from myaccount.routes import routes
import aiomysql
import myaccount.db as db
'''
Created on 2018-04-25 11:08:35

@author: linqt
'''

@routes.get('/openacc')
async def openacc(request):
    sqlstr="insert into bus.user (user_id,user_name,sex,card_num) values (%s,%s,%s,%s)"
    param=('42aqe','Tom','02','4444444')
    r= await db.excute_insertorupdate( request.app['db'],sqlstr,param)
    print(r)
    data = {'result': r}
    return data

@routes.get('/queryacc')
async def queryacc(request):
    sqlstr="select * from bus.user where user_id = %s"
    param=('42aqe')
    r= await db.excute_select_dic(request.app['db'],sqlstr,param)
    print(r)
    data = {'result': r}
    return data