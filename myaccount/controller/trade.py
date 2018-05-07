from myaccount.routes import routes
import myaccount.model.models as model
import decimal
import logging
from aiojobs.aiohttp import atomic, spawn
from myaccount.service.transfer import trade

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
                logging.error("sql execute fails:%s",e)
                await trans.rollback()
                res=0
        else:
                await trans.commit()
    resutl = {'result': r}
    return resutl

@routes.post('/transfer')
@atomic
async def transfer(request):
#     await spawn(request, trade(request))
    r = await trade(request)
    resutl = {'result': r}
    return resutl

@routes.post('/querorder')
async def querorder(request):
    data = await request.post()
    orderId = data['orderId']
    logging.info("begin query order,id=%s",orderId)
    async with request.app['engine'].acquire() as conn:
        order = model.Order.__table__
        res = await conn.execute(order.select().where(order.c.ORDER_ID == orderId))
        r = await res.first()
        logging.info("query sucess,resutl:%s",r)
    resutl = {'AMOUNT': str(r.AMOUNT),'FROM_USER_ID':r.FROM_USER_ID,'TO_USER_ID':r.TO_USER_ID,'ORDER_TYPE':r.ORDER_TYPE}
    return resutl