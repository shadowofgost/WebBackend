"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-16 17:15:44
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Logs/settings.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-16 17:40:53
# @Software         : Vscode
"""
import logging
import os
import sys
from pprint import pformat
from types import FrameType
from typing import cast


from loguru import logger
from loguru._defaults import LOGURU_FORMAT



class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentaion.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record: logging.LogRecord):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def format_record(record: dict) -> str:
    """
    这里的代码是copy的，记录日志格式的
    Custom format for loguru loggers.
    Uses pformat for log any data like request/response body during debug.
    Works with logging if loguru handler it.
    Example:
    # >>> payload = [{"users":[{"name": "Nick", "age": 87, "is_active": True}, {"name": "Alex", "age": 27, "is_active": True}], "count": 2}]
    # >>> logger.bind(payload=).debug("users payload")
    # >>> [   {   'count': 2,
    # >>>         'users': [   {'age': 87, 'is_active': True, 'name': 'Nick'},
    # >>>                      {'age': 27, 'is_active': True, 'name': 'Alex'}]}]
    """

    format_string = LOGURU_FORMAT
    if record["extra"].get("payload") is not None:
        record["extra"]["payload"] = pformat(
            record["extra"]["payload"], indent=4, compact=True, width=88
        )
        format_string += "{extra[payload]}"

    format_string += "{exception}"
    return format_string


def make_filter(name):
    # 过滤操作，当日志要选择对应的日志文件的时候，通过filter进行筛选
    def filter_(record):
        return record["extra"].get("name") == name

    return filter_


def init_logging():
    loggers = (
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
        if name.startswith("uvicorn.")
    )
    for uvicorn_logger in loggers:
        uvicorn_logger.handlers = []

    # 这里的操作是为了改变uvicorn默认的logger，使之采用loguru的logger
    # change handler for default uvicorn logger
    intercept_handler = InterceptHandler()
    logging.getLogger("uvicorn").handlers = [intercept_handler]
    # set logs output, level and format
    # logger.add(sys.stdout, level=logging.DEBUG, format=format_record, filter=make_filter('stdout'))
    # 为pity添加一个info log文件，主要记录debug和info级别的日志
    pity_info = os.path.join(Config.LOG_DIR, "pity_info.log")
    # 为pity添加一个error log文件，主要记录warning和error级别的日志
    pity_error = os.path.join(Config.LOG_DIR, "pity_error.log")
    logger.add(
        pity_info,
        enqueue=True,
        rotation="20 MB",
        level="DEBUG",
        filter=make_filter("pity_info"),
    )

    logger.add(
        pity_error,
        enqueue=True,
        rotation="10 MB",
        level="WARNING",
        filter=make_filter("pity_error"),
    )

    # 配置loguru的日志句柄，sink代表输出的目标
    logger.configure(
        handlers=[
            {"sink": sys.stdout, "level": logging.DEBUG, "format": format_record},
            {
                "sink": pity_info,
                "level": logging.INFO,
                "format": format_record,
                "filter": make_filter("pity_info"),
            },
            {
                "sink": pity_error,
                "level": logging.WARNING,
                "format": format_record,
                "filter": make_filter("pity_error"),
            },
        ]
    )
    return logger
