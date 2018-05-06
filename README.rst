项目简介
========================

基于py3的aio搭建一个简单的账务demo，提供基础的开户，账户查询，充值，转账功能。

环境搭建
========================

需要安装3.6以上版本python并安装python包管理工具pip。注意：mac默认安装了python2.x版本，在执行本demo时需要指定使用python3

执行以下命令以安装相应包::

    $ pip3 install aiohttp
    $ pip3 install aiohttp_jinja2
    $ pip3 install trafaret_config
    $ pip3 install mysql-connector-python
    $ pip3 install aiomysql
    $ pip3 install aioredis
    $ pip3 install aiojobs
    $ pip3 install gunicorn
    $ pip3 install sqlalchemy

配置
========================

配置文件为config/config.yaml。需要将相应的mysql配置和redis配置改成本地环境

数据库
========================

需要在使用的mysql库中执行sql/sql.sql文件

启动
========================

* 如果在eclipse环境中，点开main.py文件，右键Run As->Python Run即可启动

* 在命令行下执行::

    $ python3 myaccount
    
测试
========================

启动后，提供的测试页面如下::
    
   开户：http://127.0.0.1:8080/openacctest
   账户查询：http://127.0.0.1:8080/queryacctest
   充值：http://127.0.0.1:8080/rechargetest
   转账：http://127.0.0.1:8080/transfertest
   订单查询：http://127.0.0.1:8080/ordertest

代码简析
========================

* 对外接口都在controller包中
* listenerpg包中实现了一个监听器，监听开户接口中放入redis的一个id，然后请求了一下百度首页。该功能模拟一些需要异步实现的一些功能
* 整体框架使用aiohttp，连接数据库使用aiomysql，连接redis使用aioredis
* 开户模块使用的是直接执行sql的方式访问数据库，充值/转账模块使用orm方式访问数据
* 日志模块使用python自带的logging模块
* 加载了拦截器在middlewares.py中，对返回消息中为字典的自动转换为json格式
* model中是sqlalchemy的表描述类

关于ORM生成
========================

sqlalchemy的model可以使用sqlacodegen自动生成

首先安装sqlacodegen包::

    $ pip3 install sqlacodegen

然后执行命令::

    $ sqlacodegen mysql://user:passwor@ip:port/db > models.py
    
工程化部署
========================  

因为aiohttp是单进程单线程，因此为了充分利用cpu计算资源，部署到服务器上需要部署成多进程模式，有两种部署方式：

* Nginx+Supervisord

Supervisord是一个进程监控器，可以实现进程自启动的功能，对于一个包可以配置自启动多个进程，但是因为一个进程只能监控一个端口，因此该种部署方式，需要在Supervisord配置的启动命令中传入进程号，
程序根据进程号读取不同配置文件，监控不同端口。这种部署方式的好处是程序运行速度相对较快，但是部署比较复杂.

* Nginx+Gunicorn（推荐）

Gunicorn是一个web容器，本身具有一个master进程，启动多个工作进程。使用Gunicorn部署aiohttp会把aiohttp当作工作进程来启动。这种部署方式的好处是全部监控一个端口，部署维护简单。
缺点是程序运行速度稍慢（ slightly slower）

 如果使用Gunicorn部署，需要修改main.py中的main函数最后一行::
  
  原文:
  web.run_app(app,
                host=app['config']['host'],
                port=app['config']['port'])
                
  改为:
  return app
   
 Gunicorn启动命令为:
  gunicorn myaccount --bind ip:port --worker-class aiohttp.GunicornWebWorker