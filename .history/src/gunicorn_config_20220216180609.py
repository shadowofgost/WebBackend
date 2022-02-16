"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-16 17:56:07
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/gunicorn_config.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-16 18:05:18
# @Software         : Vscode
"""
# config.py
from gevent import monkey

monkey.patch_all()  # python 网络接口多进程处理包
import multiprocessing

debug = False
# 监听内网端口5000
bind = "0.0.0.1:9001"
# 监听队列
backlog = 2048
# 并行工作进程数
workers = 3
# 每个进程的开启线程
threads = 2

# workers = multiprocessing.cpu_count() * 2 + 1
# threads = multiprocessing.cpu_count() * 2

# 设置守护进程,将进程交给supervisor管理
daemon = "false"
# 工作模式协程。使用gevent模式，还可以使用sync模式，默认的是sync模式
worker_class = "uvicorn.workers.UvicornWorker"
# #worker_connections最大客户端并发数量，默认情况下这个值为1000。此设置将影响gevent和eventlet工作模式
worker_connections = 2000
# 超时
timeout = 180

# # 进程pid记录文件
# pidfile = 'app_pid.log'
loglevel = "warning"
logfile = "./Logs/gunicorn_debug.log"
accesslog = "./Logs/gunicorn_access.log"
access_log_format = "%(h)s %(t)s %(U)s %(q)s"
errorlog = "./Logs/gun_error.log"
