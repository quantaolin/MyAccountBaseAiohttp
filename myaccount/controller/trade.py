from myaccount.routes import routes
import myaccount.model.models as model
import decimal

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
    async with request.app['engine'].acquire() as conn:
        trans = await conn.begin()
        try:
            order = model.Order.__table__
            print(order.insert)
            res = await conn.execute(order.insert().values(ORDER_ID=orderId,ORDER_TYPE="01",AMOUNT=decimal.Decimal(amount),TO_USER_ID=userId))   
            print(res.rowcount())
            print('--')
            account = model.Account.__table__
            res = await conn.execute(account.update().returning(*account.c).where(account.c.USER_ID==userId).values(AMOUNT=account.c.AMOUNT+decimal.Decimal(amount)))
            res = res.fetchall()
            print(res)
        except Exception as e:
                print("sql execute fails",e.args)
                await trans.rollback()
                res=0
        else:
                await trans.commit()
    resutl = {'result': res}
    return resutl