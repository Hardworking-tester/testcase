# encoding:utf-8

from selenium import webdriver
import unittest,logging,time
def log1():

    logger=logging.getLogger()
    logger.setLevel(logging.INFO)
    filehandle=logging.FileHandler("E:\\wwg\\log.txt")
    filehandle.setLevel(logging.INFO)
    hh='王伟高'
    gg='ff'
    formatter=logging.Formatter("%(asctime)s: %(message)s","%Y年%m月%d日 %H:%M:%S")
    filehandle.setFormatter(formatter)
    logger.addHandler(filehandle)
    logger.info("元素是：%s,%s" %(hh,gg))
def main():
    log1()

if __name__=="__main__":
    main()


