import logging
'''
Created on  2018-05-07 15:41:49

@author: quantaolin
'''
async def writeredis(request,userId):
    with await request.app['redis'] as conn:
        logging.info('lpush redis')
        await conn.execute('lpush','py:account:test:openaccid',userId)