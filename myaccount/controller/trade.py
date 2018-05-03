from myaccount.routes import routes
import myaccount.model.models as model

'''
Created on  2018-05-03 18:28:20

@author: quantaolin
'''

@routes.post('/recharge')
async def recharge(request):
    data = await request.post()
    orderId = data['orderId']
    userId = data['userId']
    amount = data['amount']
    async with request.app['db'].acquire() as conn:
        conn.begin()
        try:
            order = model.Order().metadata
            res = await conn.execute(order.insert().values(ORDER_ID=orderId,ORDER_TYPE='01',AMOUNT=int(amount),TO_USER_ID=userId))   
            print(res.rowcount())                                
            account = model.Account().metadata
            res = await conn.execute(account.update().returning(*account.c).where(USER_ID=userId).values(AMOUNT=account.c.AMOUNT+amount))
            res = res.fetchall()
            print(res)
        except Exception as e:
                print("执行sql出错",e.args)
                await conn.rollback()
                res=0
        else:
                await conn.commit()
    resutl = {'result': res}
    return resutl