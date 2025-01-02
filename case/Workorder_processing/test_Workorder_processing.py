import allure
import requests
from public.config import *

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
    allure.attach(res.text)


@allure.title("在线处理")
def test_order_work(test_login):
    token=test_login
    params = {
        "orderId":13291
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

@allure.title("上传文件")
def test_order_file(test_login,test_order_work):
    token=test_login
    handleid = test_order_work
    data = {
            "handleId": handleid,
            "handleFiles": [
                {
                    "fileName": "测试",
                    "url": "http://nttbhdvtj.rw/viyhlw",
                    "updateType": 9,
                    "fileSize": 76
                }
            ]
    }

    headers={
        "Authorization": token
    }
    res= requests.get(
        data=data,
        url=f"{PROJECT_URL}/api/OrderAdminService/WorkOrderHandle/AddHandleFiles",
        headers=headers
    )
    allure.attach(res.text)
