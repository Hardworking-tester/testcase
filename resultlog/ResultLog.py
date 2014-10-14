# encoding:utf-8
import logging
def ResultLog():
    log_path="F:\\resultlog\\resultlog.txt"
    # file_operate=file(log_path,'w')
    # file_operate.truncate()
    log=logging.getLogger("wwg")
    log.setLevel(logging.INFO)
    filehandler=logging.FileHandler(log_path)
    filehandler.setLevel(logging.INFO)
    formatter=logging.Formatter("%(asctime)s:%(module)s- %(funcName)s-%(lineno)d %(message)s","%Y年%m月%d日 %H:%M:%S")
    filehandler.setFormatter(formatter)
    log.addHandler(filehandler)
    return log
