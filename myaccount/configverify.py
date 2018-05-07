import trafaret
'''
Created on 2018-04-25 11:08:35

@author: linqt
'''
TRAFARET = trafaret.Dict({
    trafaret.Key('mysql'):
        trafaret.Dict({
            'user': trafaret.String(),
            'password': trafaret.String(),
            'host': trafaret.String(),
            'port': trafaret.Int(),
            'db': trafaret.String(),
            'minsize': trafaret.Int(),
            'maxsize': trafaret.Int(),
            'connect_timeout': trafaret.Int(),
        }),
    trafaret.Key('redis'):
        trafaret.Dict({
            'host': trafaret.String(),
            'port': trafaret.Int(),
            'minsize': trafaret.Int(),
            'maxsize': trafaret.Int(),
        }),
    trafaret.Key('host'): trafaret.IP,
    trafaret.Key('port'): trafaret.Int(),
})