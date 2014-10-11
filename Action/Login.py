#encoding:utf-8
import sys
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium import webdriver
from Data import ReadExcel
import xlrd,time
from resultlog import ResultLog
class Login():

    def operate_element(self,br,username,password,locate_element,element):
        """
        该函数主要是在浏览器内对定位到的元素进行操作
        """
        obj=locate_element
        username_send=username
        password_send=password
        log=ResultLog.ResultLog()

        readexcel_class3=ReadExcel.ReadExcel()
        operate_excelpath="F:\\pytest\\testcase\\Data\\operate_method.xls"
        operate_method_sheet=readexcel_class3.getTable(operate_excelpath)
        operate_method_sheet_rows=readexcel_class3.getExcelRows(operate_excelpath)
        operate_method_sheet_cols=readexcel_class3.getExcelCols(operate_excelpath)
        objectname_list=operate_method_sheet.col_values(0)
        # print objname
        if obj in objectname_list:
            for i in range(operate_method_sheet_rows):
                if objectname_list[i]==obj:
                    list5=operate_method_sheet.row_values(i)
                    if list5[1]=='sendkey' and obj=='username':

                        element.clear()
                        try:
                            element.send_keys(username_send)
                            log.info("元素%s 操作成功,传递的数据为:%s" %(obj.encode('utf-8'),username_send.encode('utf-8')))
                        except:
                            log.info("需要操作的元素%s 不存在" %obj.encode('utf-8') )
                        time.sleep(5)
                    elif list5[1]=='sendkey' and obj=='password':
                        element.clear()
                        try:
                            element.send_keys(password_send)
                            log.info("元素%s 操作成功,传递的数据为:%s" %(obj.encode('utf-8'),password_send.encode('utf-8')))
                        except:
                            log.info("需要操作的元素%s 不存在" %obj.encode('utf-8') )
                        time.sleep(5)
                    elif list5[1]=='click':
                        try:
                            element.click()
                            log.info("元素%s 操作成功" %obj.encode('utf-8'))
                        except:
                            log.info("需要操作的元素%s 不存在" %obj.encode('utf-8') )
                        time.sleep(10)
        else:
            log.info("该元素没有在operate_method.xls文件中")


    def operate_alert(self,br):
        log=ResultLog.ResultLog()
        try:
            log.info("弹出框内容为："+(br.switch_to_alert().text).encode("utf-8"))
            br.switch_to_alert().accept()

        except NoAlertPresentException,e:
            log.info("没有找到弹出框")



