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
                if msg == None or msg.strip()=='':
                    await asyncio.sleep(1)
                    continue
                logging.info('get openacc:%s',msg)
                async with aiohttp.ClientSession() as session:
                    async with session.get('http://127.0.0.1:8080/opeacclistentest') as resp:
                        logging.info('get result status:%s',resp.status)
                        logging.info('get result text:%s',await resp.text())
                await asyncio.sleep(1)   
    except asyncio.CancelledError:
        pass    