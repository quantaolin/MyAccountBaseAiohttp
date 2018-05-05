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
    userSqlstr="insert into user (user_id,user_name,sex,card_num) values (%s,%s,%s,%s)"
    userParam=(userId,data['userName'],data['sex'],data['cardNum'])
    accSqlstr="insert into account (ACCOUNT_ID,ACCOUNT_TYPE,USER_ID,BALANCE) values (%s,%s,%s,%s)"
    accParam=(data['accountId'],data['accountType'],userId,0)
    async with request.app['db'].acquire() as conn:
        async with conn.cursor() as cur:
            await conn.begin()
            try:
                await cur.execute(userSqlstr,userParam)
                r=cur.rowcount
                if(r != 1):
                    raise Exception("user sql execute fails")
                await cur.execute(accSqlstr,accParam)
                print(cur.description)
                r=cur.rowcount
                if(r != 1):
                    raise Exception("account sql execute fails")
            except Exception as e:
                print("sql execute fails",e.args)
                await conn.rollback()
                r=0
            else:
                await conn.commit()   
    async with request.app['redis'].acquire() as conn:
        await conn.lpush("py:account:test:openaccid",userId)
    print(r)
    resutl = {'result': r}
    return resutl

@routes.post('/queryacc')
async def queryacc(request):
    data = await request.post()
    sqlstr="select * from user where user_id = %s"
    param=(data['userId'])
    r= await db.excute_select_dic(request.app['db'],sqlstr,param)
    print(r)
    data = {'result': r}
    return data