import logging.config
import os

current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log = os.path.join(current_dir,'logging.conf')


# # 读取日志配置文件
logging.config.fileConfig(log)
# 创建一个日志器logger
logger = logging.getLogger('fileAndConsole')
logger.debug('启动中...')

