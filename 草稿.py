# import allure
# import pytest
# import requests
# import json
# from public.config import *
# # import json
# import random
# #
# # # 假设这是你的JSON字符串
# # json_str = '''
# # {
# #   "status": 1,
# #   "message": "获取工单列表",
# #   "data": [
# #     {
# #       "id": 12966,
# #       "orderIdNumber": "FBW202412181549447117933",
# #       "name": "12",
# #       "type": 6,
# #       "typeName": "律师函",
# #       "chatName": "测试",
# #       "isUpdateOrder": 0,
# #       "updateStatus": 0,
# #       "estimatedTime": "2025-01-06 15:45:14",
# #       "lawyerId": 0,
# #       "handleMemberId": 394,
# #       "handleMemberName": "王丹"
# #     },
# #     {
# #       "id": 12967,
# #       "orderIdNumber": "FBW202412181549447117934",
# #       "name": "13",
# #       "type": 6,
# #       "typeName": "律师函",
# #       "chatName": "测试",
# #       "isUpdateOrder": 0,
# #       "updateStatus": 0,
# #       "estimatedTime": "2025-01-06 15:45:15",
# #       "lawyerId": 0,
# #       "handleMemberId": 395,
# #       "handleMemberName": "李明"
# #     }
# #   ]
# # }
# # '''
# #
# # # 将JSON字符串解析为Python字典
# # data = json.loads(json_str)
# #
# # # 从data列表中随机选择一个工单
# # random_order = random.choice(data['data'])
# #
# # # 获取该工单的id
# # random_id = random_order['id']
# #
# # print("随机选择的id:", random_id)
#
# def test_workorder(test_login):
#     token=test_login
#     data = {
#         "page": 1,
#         "limit": 10,
#         "status":2
#     }
#     headers = {
#         "Authorization": token
#     }
#     res = requests.post(
#         url=f"{PROJECT_URL}/api/OrderAdminService/WorkOrder/GetAdminPageList",
#         json=data,
#         headers=headers
#     )
#     order_data = res.text
#     allure.attach(res.text)
#     print(order_data)
#
#     data = json.loads(order_data)
#
#     # 从data列表中随机选择一个工单
#     random_order = random.choice(data['data'])
#
#     # 获取该工单的id
#     random_id = random_order['id']
#
#     print("随机选择的id:", random_id)
