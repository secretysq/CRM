import allure
import pytest
import requests
import json
from public.config import *
import random

@pytest.fixture
@allure.title("获取工单列表")
def test_workorder(test_login):
    token=test_login
    data = {
        "page": 1,
        "limit": 10,
        "status":2
    }
    headers = {
        "Authorization": token
    }
    res = requests.post(
        url=f"{PROJECT_URL}/api/OrderAdminService/WorkOrder/GetAdminPageList",
        json=data,
        headers=headers
    )
    order_data = res.text
    allure.attach(res.text)
    return order_data


@allure.title("在线处理")
def test_order_work(test_login,test_workorder):
    token=test_login
    # 将JSON字符串解析为Python字典
    order_data = json.loads(test_workorder)
    # 从data列表中随机选择一个工单
    random_order = random.choice(order_data['data'])
    # 获取该工单的id
    random_id = random_order['id']
    params = {
        "orderId":random_id
    }

    headers={
        "Authorization": token
    }
    res= requests.get(
        params=params,
        url=f"{PROJECT_URL}/api/OrderAdminService/WorkOrderHandle/GetOnlineHandle",
        headers=headers
    )
    allure.attach(res.text)
    handleId = res.json()["data"]["nowHandle"]["handleId"]
    return handleId

# @allure.title("上传文件")
# def test_order_file(test_login,test_order_work):
#     token=test_login
#     handleid = test_order_work
#     data = {
#             "handleId": handleid,
#             "handleFiles": [
#                 {
#                     "fileName": "测试",
#                     "url": "http://nttbhdvtj.rw/viyhlw",
#                     "updateType": 9,
#                     "fileSize": 76
#                 }
#             ]
#     }
#
#     headers={
#         "Authorization": token
#     }
#     res= requests.get(
#         data=data,
#         url=f"{PROJECT_URL}/api/OrderAdminService/WorkOrderHandle/AddHandleFiles",
#         headers=headers
#     )
#     allure.attach(res.text)
