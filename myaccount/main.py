import argparse
import asyncio
import logging
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
    # setup views and routes
    setup_routes(app)
    setup_static_routes(app)
    setup_middlewares(app)
    setup_listener(app)

    return app


def main(argv):
    # init logging
    logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()

    app = init(loop, argv)
    web.run_app(app,
                host=app['config']['host'],
                port=app['config']['port'])


if __name__ == '__main__':
    main(sys.argv[1:])