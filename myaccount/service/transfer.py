import myaccount.model.models as model
import decimal
import logging
import asyncio
'''
Created on  2018-05-07 16:38:36

@author: quantaolin
'''
async def trade(request):
    data = await request.post()
    orderId = data['orderId']
    fromuserId = data['fromuserId']
    touserId = data['touserId']
    amount = data['amount']
    async with request.app['engine'].acquire() as conn:
        trans = await conn.begin()
        try:
            logging.info('start db excute')
            order = model.Order.__table__
            res = await conn.execute(order.insert().values(ORDER_ID=orderId,ORDER_TYPE="02",AMOUNT=decimal.Decimal(amount),FROM_USER_ID=fromuserId,TO_USER_ID=touserId))
            await asyncio.sleep(10) 
            account = model.Account.__table__
            res = await conn.execute(account.update().where(account.c.USER_ID==fromuserId).values(BALANCE=account.c.BALANCE-decimal.Decimal(amount)))
            res = await conn.execute(account.update().where(account.c.USER_ID==touserId).values(BALANCE=account.c.BALANCE+decimal.Decimal(amount)))
            r = res.rowcount
            logging.info('end db excute,r=%s',r)
        except Exception as e:
                logging.error("sql execute fails:%s",e)
                await trans.rollback()
                res=0
        else:
                await trans.commit()
    return r