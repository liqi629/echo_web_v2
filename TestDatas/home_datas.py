# -*- coding: utf-8 -*-
# @Time     : 2019/6/4 13:57
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : home_datas.py
# @Software : PyCharm
operation_system ={
    "zh_name":"功能自动化测试一",
    "code":"123456789",
    "short_zn_name":"自动化测试一",
    "en_name":"uiAutoTestOne",
    "short_en_name":"autoTestOne",
    "sys_remark":"这个业务系统是用来做自动化测试的，请勿删除",
    # "sys_status":"",
    "sys_version":"1.0",
    "dept":"产品质量保障部",
    "contacter":"产品测试员一",
    "mobile":"18610430001",
    "email":"li.qi@yoyosys.com.cn"

}
#脚本名称、绝对路径、脚本内容、执行机ip
script = {
    "name":"auto_script_01.sh",
    "AP": "/opt/auto_script_01.sh",
    "scriptType": "其他",
    "dbType": "其他",
    "content": '#!/usr/bin/bash\
            echo "hello me"\
            echo>/root/testfile_01.txt',
    "ip": "172.16.12.28"

}