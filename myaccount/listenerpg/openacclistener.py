import asyncio
import aiohttp
import logging
'''
Created on  2018-04-25 11:08:35

@author: quantaolin
'''
async def listener_openacc(app):
    try:
        with await app['redis'] as conn:
            while True:   
                msg = await conn.execute('lpop','py:account:test:openaccid')
                print('get msg=',msg)
                if msg == None or msg.strip()=='':
                    await asyncio.sleep(1)
                    continue
                async with aiohttp.ClientSession() as session:
                    async with session.get('http://www.baidu.com') as resp:
                        logging.info('get baidu sucess＝',resp.status)
                        print('get baidu result',resp.status)
                        print('get baidu result',await resp.text())
                await asyncio.sleep(1)   
    except asyncio.CancelledError:
        pass    