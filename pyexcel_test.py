# import allure
# import pytest
#
# from public.login_test import login_test
# from read_excel import getexcel
# from sendhttp_test import send_requests
#
#
# class Testcase:
#     @allure.title("用例")
#     @pytest.mark.parametrize("case", getexcel())
#     def test_mobile(self, case):
#         token = login_test()
#         url = case[1]
#         method = case[2]
#         data = case[3]
#         params = case[4]
#         headers = {"Authorization": token}
#         res = send_requests(url, method, data, params, headers)
#         allure.attach(res.text)
#         # assert res.json()[case[5]] == case[6]
