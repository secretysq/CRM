# import requests
# import json
#
# def send_requests(url, method, data=None, params=None, headers=None):
#     if headers is None:
#         headers = {}
#
#     if method.lower() == "post" and data is not None:
#         # 检查data是否是字典，如果是则直接使用
#         if isinstance(data, dict):
#             headers['Content-Type'] = 'application/json'
#         elif isinstance(data, str):
#             # 如果data是字符串，尝试将其解析为JSON对象
#             try:
#                 data = json.loads(data)
#                 headers['Content-Type'] = 'application/json'
#             except json.JSONDecodeError:
#                 print("Error decoding JSON from data string.")
#                 return None
#         else:
#             print("Data must be a dictionary or a JSON string.")
#             return None
#
#     if method.lower() == "get":
#         res = requests.get(
#             url=url,
#             params=params,
#             headers=headers
#         )
#     elif method.lower() == "post":
#         res = requests.post(
#             url=url,
#             json=data,  # 使用json参数直接传递JSON对象
#             headers=headers
#         )
#     else:
#         res = requests.post(
#             url=url,
#             data=data,  # 使用json参数直接传递JSON对象
#             headers=headers
#         )
#
#     return res