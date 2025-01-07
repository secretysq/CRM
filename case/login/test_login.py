import allure
import pytest
import requests

@pytest.fixture(scope='session')
@allure.title("登录，获取token")
def test_login():
    data = {"loginName":"王丹","passWord":"Fbw123456"}
    res = requests.post(
        url="https://workordertest.365lawhelp.com/api/MemberAdminService/login/login",
        json=data
    )
    token = "Bearer " + res.json()["data"]["token"]
    allure.attach(res.text)
    return token

