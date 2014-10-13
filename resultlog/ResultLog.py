# encoding:utf-8
import logging
def ResultLog():
    log_path="F:\\resultlog\\resultlog.txt"
    log=logging.getLogger("wwg")
    log.setLevel(logging.INFO)
    filehandler=logging.FileHandler(log_path)
    filehandler.setLevel(logging.INFO)
    formatter=logging.Formatter("%(asctime)s: %(message)s","%Y年%m月%d日 %H:%M:%S")
    filehandler.setFormatter(formatter)
    log.addHandler(filehandler)
    rfd=open("F:\\resultlog\\resultlog.txt",'r')
    wfd=file("F:\\resultlog\\resultlog11.txt",'w')
    h={}
    for i in rfd:

        if not h.has_key(i):
            h[i]=1
            wfd.write(i)
    return log