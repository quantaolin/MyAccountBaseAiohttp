import asyncio
import aiohttp
'''
Created on  2018-04-25 11:08:35

@author: quantaolin
'''
async def listener_openacc(app):
    try:
        async with app['redis'].acquire() as conn:
            while True:   
                msg = await conn.lpop("py:account:test:openaccid")
                if msg == None or msg.strip()=='':
                    await asyncio.sleep(5)
                    continue
                async with aiohttp.ClientSession() as session:
                    async with session.get('http://www.baidu.com') as resp:
                        print(resp.status)
                        print(await resp.text())
                await asyncio.sleep(5)   
    except asyncio.CancelledError:
        pass    