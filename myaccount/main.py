import argparse
import asyncio
import logging,logging.handlers
import sys
import jinja2
import aiohttp_jinja2
from aiohttp import web
from myaccount.db import setup_engine
from myaccount.redis import setup_redis
from myaccount.listener import setup_listener
from myaccount.middlewares import setup_middlewares
from myaccount.routes import setup_routes,setup_static_routes
from myaccount.configverify import TRAFARET
from trafaret_config import commandline
from aiojobs.aiohttp import setup
'''
Created on 2018-04-25 11:08:35

@author: linqt
'''

def init(loop, argv):
    ap = argparse.ArgumentParser()
    commandline.standard_argparse_options(ap,
                                          default_config='./config/config.yaml')
    #
    # define your command-line arguments here
    #
    options = ap.parse_args(argv)

    config = commandline.config_from_options(options, TRAFARET)

    # setup application and extensions
    app = web.Application(loop=loop)

    # load config from yaml file in current dir
    app['config'] = config

    # setup Jinja2 template renderer
    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('myaccount', 'templates'))

    setup_engine(app)
    setup_redis(app)
    setup_routes(app)
    setup_static_routes(app)
    setup_middlewares(app)
    setup_listener(app)
    setup(app)
    return app


def main(argv):
    # init logging
    fomstr='%(asctime)s - %(process)d - %(thread)d - %(filename)s - %(module)s - %(funcName)s - %(lineno)d : %(levelname)s -- %(message)s'
    logging.basicConfig(
        level=logging.DEBUG,
        format=fomstr, 
        datefmt='%Y-%m-%d %A %H:%M:%S')
    filehandler = logging.handlers.TimedRotatingFileHandler("./logs/bussiness.log", when='D', interval=1)
    filehandler.suffix="%Y-%m-%d.log"
    filehandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fomstr)
    filehandler.setFormatter(formatter)
    logging.getLogger('').addHandler(filehandler)

    loop = asyncio.get_event_loop()

    app = init(loop, argv)
    web.run_app(app,
                host=app['config']['host'],
                port=app['config']['port'])


if __name__ == '__main__':
    main(sys.argv[1:])