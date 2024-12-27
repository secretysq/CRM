# import allure
# import requests
#
# @allure.title("登录，获取token")
# def list_test():
#     token = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjYzNDM5MDkwNDZENTk4QzYxQTQ3MzA5QjgwQkY1NzVENDY5N0VGMTRSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IlkwT1FrRWJWbU1ZYVJ6Q2JnTDlYWFVhWDd4USJ9.eyJuYmYiOjE3MzUwNDg5MTksImV4cCI6MTczNTA5MjExOSwiaXNzIjoiaHR0cDovLzYwLjIwNC4yNDkuMTc4OjU0MDAiLCJhdWQiOiJNZW1iZXJBZG1pbkFwaSIsImNsaWVudF9pZCI6ImZhYmFvQ3JtQWRtaW4iLCJzdWIiOiIwIiwiYXV0aF90aW1lIjoxNzM1MDQ4OTE5LCJpZHAiOiJsb2NhbCIsIm5hbWUiOiJzdXBlcmFkbWluIiwidXNlck5hbWUiOiLotoXnuqfnrqHnkIblkZgiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiIwIiwiZ3JvdXAiOiIwIiwiYmxvY2siOiIwIiwianRpIjoiRjQxODA0RTZDMTAzOUM0RjIzMjM0RDRBMTc4RTE4NTciLCJpYXQiOjE3MzUwNDg5MTksInNjb3BlIjpbIk1lbWJlckFkbWluQXBpIiwib3BlbmlkIiwicHJvZmlsZSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJjdXN0b20iXX0.BmXLmPEWYZdkEue4Jd18IUE7c68bsUM-9fZF2ZITmK-9EaIZ4CVcIYs2IXT72GajjO6fustcZZTfxHfUG4bcX-n6jfOcWyWRoge7dMxSvAkwUObwvnufzl2A7FyDv6XxbwoFdxnbYLXlbQ-_XC7ndHP7a_YGAVrHJ45KMP_10aw9g437VPMIHG5KYJHnQ6LDdXl8SvY9sJ_9RWVVRg3Gxm4mwyN-3SIS2U9fxR02FG0bHKKTPo2h2Ku5IrkN_iQCuFlimQdZ_rRxalvySBHhADoT8SA9L_1Q_VZJBRydBOmQvsPX0PIa7CyS_t-uIvB0wsvrkk1x58fIaF5eSfPuTA'
#     headers = {"Authorization": token}
#     try:
#         res = requests.post(
#             url="https://workordertest.365lawhelp.com/api/OrderService/WorkOrderType/GetWorkOrderTypeList",
#             headers=headers,
#         )
#         res.raise_for_status()  # 将触发异常，如果状态码不是200
#         return res
#     except requests.exceptions.RequestException as e:
#         print(f"请求失败: {e}")
#         return None
#
# # 调用函数
# response = list_test()
# if response:
#     print(response.json())