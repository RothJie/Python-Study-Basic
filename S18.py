# import sys
#
# # 将标准输出重定向到文件
# sys.stdout = open('output.txt', 'w',encoding='utf8')
#
# print("这条消息会被写入文件。")
#
# # 关闭文件并恢复标准输出
# sys.stdout.close()
# sys.stdout = sys.__stdout__


import logging
from idlelib.iomenu import encoding

# 配置日志
logging.basicConfig(
    filename='python_program_log.log',          # 日志文件名
    filemode='a',                # 'a' 表示追加模式
    format='%(asctime)s - %(levelname)s - %(message)s',  # 日志格式
    level=logging.DEBUG,           # 设置日志级别
    encoding= 'utf8'  #这个必须加

)

# 日志记录示例
def main():
    logging.debug("这是调试信息")
    logging.info("这是信息级别的日志")
    logging.warning("这是警告信息")
    logging.error("这是错误信息")
    logging.critical("这是严重错误信息")

if __name__ == "__main__":
    main()