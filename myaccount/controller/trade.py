from myaccount.routes import routes
import myaccount.model.models as model
import decimal
import logging

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
            logging.info('start db excute')
            account = model.Account.__table__
            res = await conn.execute(account.update().where(account.c.USER_ID==userId).values(BALANCE=account.c.BALANCE+decimal.Decimal(amount)))
            order = model.Order.__table__
            res = await conn.execute(order.insert().values(ORDER_ID=orderId,ORDER_TYPE="01",AMOUNT=decimal.Decimal(amount),TO_USER_ID=userId))   
            r = res.rowcount
            logging.info('end db excute,r=%s',r)
        except Exception as e:
                logging.error(e)
                print("sql execute fails",e.args)
                await trans.rollback()
                res=0
        else:
                await trans.commit()
    resutl = {'result': r}
    return resutl