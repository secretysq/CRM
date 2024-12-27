# import openpyxl
#
# def getexcel():
#
#     workbook = openpyxl.load_workbook('case/api_case_V1.xlsx')
#     list2 = []
#
#     sheet = workbook['Sheet1']
#
#     for i in sheet.values:
#         if type(i[0]) is int:
#
#             list1 = []
#
#             for j in i:
#                 list1.append(j)
#             list2.append(list1)
#     return list2
#
#
# # getexcel()
# # print(getexcel())