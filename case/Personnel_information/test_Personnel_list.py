import allure
import requests
from public.config import *

@allure.title("添加人员")
def test_addpersonnel(test_login):
    token= test_login
    data={
            "userName": "pythonone",
            "loginName": "pythonone",
            "userPhone": "13000000009",
            "passWord": "Fbw123456~",
            "remark": "",
            "roleId": 1,
            "confirmPassWord": "Fbw123456~",
    }
    headers = {
        "Authorization": token
    }
    res = requests.post(
        url=f"{PROJECT_URL}/api/MemberAdminService/Member/AddMember",
        json=data,
        headers=headers
    )
    allure.attach(res.text)

@allure.title("人员列表查询")
def test_personnel_list(test_login):
    token = test_login
    data = {
        "page": 1,
        "limit": 20,
        "userName":"python"
    }
    headers = {
        "Authorization": token
    }
    res = requests.post(
        url=f"{PROJECT_URL}/api/MemberAdminService/Member/GetMemberPageList",
        json=data,
        headers=headers
    )
    allure.attach(res.text)
