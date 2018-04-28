from myaccount.routes import routes
import myaccount.db as db
'''
Created on 2018-04-25 11:08:35

@author: linqt
'''

@routes.post('/openacc')
async def openacc(request):
    data = await request.post()
    userId=data['userId']
    userSqlstr="insert into bus.user (user_id,user_name,sex,card_num) values (%s,%s,%s,%s)"
    userParam=(userId,data['userName'],data['sex'],data['cardNum'])
    accSqlstr="insert into bus.account (ACCOUNT_ID,ACCOUNT_TYPE,USER_ID,BALANCE) values (%s,%s,%s,%s)"
    accParam=(data['accountId'],data['accountType'],userId,0)
    async with request.app['db'].acquire() as conn:
        async with conn.cursor() as cur:
            conn.begin()
            try:
                await cur.execute(userSqlstr,userParam)
                r=cur.rowcount
                if(r != 1):
                    raise Exception("插入用户表失败")
                await cur.execute(accSqlstr,accParam)
                r=cur.rowcount
                if(r != 1):
                    raise Exception("插入账户表失败")
            except Exception as e:
                print(e.args)
                conn.rollback()
            else:
                conn.commit()      
    print(r)
    resutl = {'result': r}
    return resutl

@routes.post('/queryacc')
async def queryacc(request):
    data = await request.post()
    sqlstr="select * from bus.user where user_id = %s"
    param=(data['userId'])
    r= await db.excute_select_dic(request.app['db'],sqlstr,param)
    print(r)
    data = {'result': r}
    return data