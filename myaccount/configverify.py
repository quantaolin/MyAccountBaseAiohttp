import trafaret
'''
Created on 2018��4��24��

@author: linqt
'''
TRAFARET = trafaret.Dict({
    trafaret.Key('mysql'):
        trafaret.Dict({
            'database': trafaret.String(),
            'user': trafaret.String(),
            'password': trafaret.String(),
            'host': trafaret.String(),
            'port': trafaret.Int(),
            'minsize': trafaret.Int(),
            'maxsize': trafaret.Int(),
        }),
    trafaret.Key('host'): trafaret.IP,
    trafaret.Key('port'): trafaret.Int(),
})