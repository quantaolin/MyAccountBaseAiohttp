from myaccount.routes import routes
import myaccount.db as db
'''
Created on 2018-04-25 11:08:35

@author: linqt
'''

@routes.post('/openacc')
async def openacc(request):
    userId=request.match_info['userId']
    userSqlstr="insert into bus.user (user_id,user_name,sex,card_num) values (%s,%s,%s,%s)"
    userParam=(userId,request.match_info['userName'],request.match_info['sex'],request.match_info['cardNum'])
    accSqlstr="insert into bus.account (ACCOUNT_ID,ACCOUNT_TYPE,USER_ID,BALANCE) values (%s,%s,%s,%s)"
    accParam=(request.match_info['accountId'],request.match_info['accountType'],userId,0)
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
    data = {'result': r}
    return data

@routes.post('/queryacc')
async def queryacc(request):
    sqlstr="select * from bus.user where user_id = %s"
    param=(request.match_info['userId'])
    r= await db.excute_select_dic(request.app['db'],sqlstr,param)
    print(r)
    data = {'result': r}
    return data