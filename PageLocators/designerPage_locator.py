# -*- coding: utf-8 -*-
# @Time     : 2019/5/27 14:55
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : designerPage_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By
class DesignerPageLocator:
    #按钮====================================================================================================================
    #新建作业+号
    add_job=(By.XPATH,'//img[@id="addBgBac"]')
    #作业名称输入框//input[@id="bisName"]
    job_name_input = (By.XPATH, '//input[@id="bisName"]')
    #修改作业，名称输入
    edit_name_input = (By.XPATH,'//input[@id="editBus"]')
    #修改按钮
    edit_name_button = (By.XPATH,'//a[@id="btn-edit"]')
    #新建作业确认按钮
    job_button = (By.XPATH, '//a[@id="btnBusinessAdd"]')
    #新建完成的作业，列表中的定位 //span[text()="auto_test_2"]
    job_list_new = (By.XPATH, ' //span[text()="auto_test_2222"]')
    # 编辑名称后的作业，列表中的定位 //span[text()="auto_test_3"]
    job_list_new_1 = (By.XPATH, ' //span[text()="auto_test_2223"]')
    # 鼠标悬浮作业，编辑按钮
    edit_job_button = (By.XPATH, '//span[@class="fa fa-edit btn-edit-business"]')
    #鼠标悬浮新建作业，删除按钮
    delete_job_button = (By.XPATH, '//span[@class="fa fa-trash btn-del-business"]')
    #删除作业弹窗 的删除按钮
    dialog_delete_button = (By.XPATH, '//a[@id="btn-delete"]')
    #数据源
    data_source = (By.XPATH, '//span[text()="数据源"]')
    #添加按钮
    add_button = (By.XPATH, '//span[text()="添加"]')
    #保存按钮
    save_button = (By.XPATH,'//span[text()="保存"]')
    #发布按钮
    publish_button = (By.XPATH,'//span[text()="发布"]')
    #取消发布按钮
    unpublish_button = (By.XPATH,'//span[text()="取消发布"]')
    #本地运行按钮
    run_locally = (By.XPATH,'//span[text()="本地运行"]')
    #分布式运行按钮
    run_distributed = (By.XPATH,'//span[text()="分布运行"]')
    #删除节点//a[text()="删除节点"]
    delete_node = (By.XPATH,'//a[text()="删除节点"]')
    #工作流 运行按钮
    run_work_flow = (By.XPATH,'//span[text()="运行"]')
    #TOAST=================================================================================================
    #新建作业成功/名称重复toast提示//div[@class="toast-message"]，下面的toast 共用
    job_toast = (By.XPATH, '//div[@class="toast-message"]')
    #发布成功toast
    toast_pub_success = (By.XPATH,'')
    #取消发布成功toast
    toast_pub_cancel = (By.XPATH, '')
    #重复发布tosat
    toast_pub_re = (By.XPATH, '')
    #作业窗口=========================================================================================
    #作业：not_delete
    select_job_mysql = (By.XPATH,'//div[@class="pull-left session"]//span[text()="not_delete"]')
    #作业：MySQL_text
    select_job_text = (By.XPATH, ' // li[text() = "MySQL_text"]')

    #作业========================================================================
    #作业：MySQL_text
    MySQL_text = (By.XPATH,'//ul[@class="level0 "]//span[text()="MySQL_text"]')
    #作业：MySQL_text目标文件源
    text_name = (By.XPATH,'//span[text()="自动化测试目标文件源一"]')
    #作业：not_delete job
    not_delete_job = (By.XPATH, '//ul[@id="treeDemo"]//span[text()="not_delete"]')
    # 作业========================================================================


    #数据库，树加号，展开作用//span[@id="dataTree_1_switch"]
    data_tree_1 = (By.XPATH,'//span[@id="dataTree_1_switch"]')
    #目标//span[text()="目标"]
    target_source = (By.XPATH,'//span[text()="目标"]')
    #映射关系
    map = (By.XPATH,'//span[text()="映射关系"]')
    #保存，映射配置弹出窗的确定按钮
    map_config_button = (By.XPATH,'//a[@id="btn-relation-add"]')
    #更新映射成功的toast：//div[text()="更新映射成功"]
    toast_message = (By.XPATH,'//div[text()="更新映射成功"]')
    #多表配置
    table_config = (By.XPATH,'//span[text()="多表配置"]')
    #多元配置弹出窗-确定按钮//a[@class="btn btn-primary btn-config-confirm"]
    config_button = (By.XPATH,'//a[@class="btn btn-primary btn-config-confirm"]')



    #MySQL数据库，操作相关========================================================================
    #数据库-MySQL  //span[text()="MySQL"]
    MySQL = (By.XPATH,' //span[text()="MySQL"]')
    #数据库选择后的确认按钮//a[@id="btn-db-type"]
    db_button = (By.XPATH,'//a[@id="btn-db-type"]')
    #新增数据库按钮//form[@name="sameTOMysqlDriver"]//button[@id="addSource"]
    add_source = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//button[@id="addSource"]')
    #源名称输入框//form[@name="sameTOMysqlDriver"]//input[@id="sourceName"]
    source_name = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="sourceName"]')
    #ip输入框//form[@name="sameTOMysqlDriver"]//input[@id="ip"]
    ip = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="ip"]')
    #端口//form[@name="sameTOMysqlDriver"]//input[@id="port"]
    port = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="port"]')
    #用户名//form[@name="sameTOMysqlDriver"]//input[@id="userName"]
    user_name = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//input[@id="userName"]')
    #密码//form[@name="sameTOMysqlDriver"]//input[@id="passWord"]
    pass_word = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="passWord"]')
    #所属系统selection://*[@id="form-fieldset"]//span[@class="select2-selection__arrow"]
    select = (By.XPATH,'//*[@id="form-fieldset"]//span[@class="select2-selection__arrow"]')
    #数据库名称//form[@name="sameTOMysqlDriver"]//input[@id="dbName"]
    db_name = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="dbName"]')
    #环境类型//form[@name="sameTOMysqlDriver"]//select[@id="environmentType"]
    environment_type = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//select[@id="environmentType"]')
    #是否跨域//form[@name="sameTOMysqlDriver"]//select[@id="crossDomain"]
    cross_domain = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//select[@id="crossDomain"]')
    #编码设置//form[@name="sameTOMysqlDriver"]//select[@id="characterEncoding"]
    character_encoding = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//select[@id="characterEncoding"]')
    #备注//form[@name="sameTOMysqlDriver"]//input[@id="remark"]
    mark = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="remark"]')
    #测试连接按钮//form[@name="sameTOMysqlDriver"]//a[@id="test-connect"]
    test_connect = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//a[@id="test-connect"]')
    #测试连接的toast://span[text()="连接成功"]
    test_msg = (By.XPATH,'//span[text()="连接成功"]')
    #上一步按钮//a[text()="上一步"]
    last_step = (By.XPATH,'//a[text()="上一步"]')
    #下一步按钮//a[text()="下一步"]
    next_step = (By.XPATH,'//a[text()="下一步"]')
    #数据库第一个表
    first_tab = (By.XPATH,'//input[@data-name="AUTO_test_01"]')
    #数据库第二个表
    second_tab = (By.XPATH,'//input[@data-name="AUTO_test_02"]')
    #选表后的下一步
    next_step = (By.XPATH,'//a[text()="下一步"]')
    #选字段信息后的下一步
    next_step = (By.XPATH,'//a[text()="下一步"]')
    #最终确定按钮
    confirm_button = (By.XPATH,'//a[text()="确定"]')
    #MySQL数据库，操作相关========================================================================

    #添加成功后的数据源
    source_title = (By.XPATH,'//span[text()="自动化测试数据源一"]')
    # 添加成功后的目标源
    out_source_title = (By.XPATH, '//span[text()="自动化测试目标源一"]')


    #工作流==================================================================================================
    #作业 not_delete的工作流
    work_flow = (By.XPATH,'//span[text()="工作流"]')
    #添加工作流按钮
    add_work_folw_btn = (By.XPATH,'//ul[@id="treeDemo_1_ul"]//span[text()="添加"]')
    #工作流脚本完成的信息 捕捉(几行日志的定位一样)
    work_flow_finished_1 = (By.XPATH,'//span[contains(@class,"loading")][1]')
    # 工作流脚本完成的信息 捕捉(几行日志的定位一样)
    work_flow_finished_2 = (By.XPATH, '//span[contains(@class,"loading")][2]')
    # 工作流脚本完成的信息 捕捉(几行日志的定位一样)
    work_flow_finished_3 = (By.XPATH, '//span[contains(@class,"loading")][3]')
    #工作流名字输入框
    work_flow_input = (By.XPATH,'//input[@id="workflow-name"]')
    #确定按钮
    btn_workflow_add = (By.XPATH,'//a[@class="btn btn-primary btn-workflow-add"]')
    #新增的工作流
    new_work_flow = (By.XPATH,'//span[text()="test_work_flow_01"]')
    #工作流删除test_work_flow_01
    delete_work_flow = (By.XPATH,'//span[text()="test_work_flow_01"]//parent::a//span[text()="删除"]')
    #工作流删除dialog  删除按钮//a[@id="btn-workflow-delete"]
    btn_workflow_delete = (By.XPATH,'//a[@id="btn-workflow-delete"]')