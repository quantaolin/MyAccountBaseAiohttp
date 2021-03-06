项目简介
========================

基于py3的aio搭建一个简单的账务demo，提供基础的开户，账户查询，充值，转账，订单查询，后台监控功能。

环境搭建
========================

需要安装3.6以上版本python并安装python包管理工具pip，如果使用eclipse作为ide环境，需要安装PyDev插件。注意：mac默认安装了python2.x版本，在执行本demo时需要指定使用python3

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
   订单查询：http://127.0.0.1:8080/orderquerytest
   
日志
========================

日志打印分为两部分，日志即会打印到控制台，又打印到./logs/bussiness.log文件。bussiness.log是日文件，每天会生成一个新文件，原文件加日期改名

代码简析
========================

* 对外接口都在controller包中
* listenerpg包中实现了一个监听器，监听开户接口中放入redis的一个id，然后请求了一个本地的get地址。该功能模拟一些需要异步实现的一些功能
* 整体框架使用aiohttp，连接数据库使用aiomysql，连接redis使用aioredis
* 开户模块使用的是直接执行sql的方式访问数据库，充值/转账模块使用orm方式访问数据
* 日志模块使用python自带的logging模块
* 加载了拦截器在middlewares.py中，对返回消息中为字典的自动转换为json格式
* model中是sqlalchemy的表描述类

异步执行示例
========================

有些情况下需要先返回结果给前端，后端异步处理一些业务。在openaccount.py文件的38行做了一个示例，这种方式可以启动一个异步task非阻塞的执行::
   
   request.loop.create_task(writeredis(request,userId))
   
原子任务
========================

aiohttp在处理请求时，如果客户端断开，就会在任意一个await处停止处理。这种情况会导致数据丢失／数据不完整的风险。

为应对这种情况，需要引入aiojobs模块，该模块有两种应用方式：

  * trade.py的第42行，该方式与上面的异步执行效果相同，都会启动一个后台异步执行task，前端直接返回结果。所不同的是，采用这种方式启动的task，在系统关闭的时候，会等待执行完成。
  * trade.py的第40行的注解，被该注解标注的方法会一直执行到结束，而不管客户端是否断开

关于ORM生成
========================

sqlalchemy的model可以使用sqlacodegen自动生成

首先安装sqlacodegen包::

    $ pip3 install sqlacodegen

然后执行命令::

    $ sqlacodegen mysql://user:passwor@ip:port/db > models.py
    
关于redis
========================

aioredis现有版本不支持redis cluster。如果生产环境需要使用redis，建议使用redis-py-cluster。
使用redis-py-cluster导致的后果就是在请求redis时，进程会进入block，但是考虑到redis请求的速度较快，效率影响较小。
等待aioredis支持redis cluster后可以考虑改用aioredis。
    
工程化部署
========================  

因为aiohttp是单进程单线程，为了充分利用cpu计算资源，部署到服务器上需要部署成多进程模式，有两种部署方式：

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
   
 Gunicorn启动命令为::
 
  gunicorn myaccount --bind ip:port --worker-class aiohttp.GunicornWebWorker