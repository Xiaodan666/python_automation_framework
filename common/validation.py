# import re
# str = "exists()"
# str_1 = re.search(r'[(](.*?)[)]', str)
# # print(str_1.group()[1:-1])
#
# print(str.split("(")[1].split(")")[0])
#
# after_str = str.split("(")[1].split(")")[0]
#
# if after_str == "":
#     print("None")
# else:
#     print(after_str)
from jsonpath import jsonpath

response_data = {"Date": "Fri, 25 Nov 2022 06:51:14 GMT", "Content-Type": "application/json; charset=UTF-8", "Content-Length": "277", "Connection": "keep-alive", "Server": "nginx", "Error-Code": "0", "Error-Msg": "ok"}
json_path = 'Content-Type'
actual_value = jsonpath(response_data, json_path)[0]
print(actual_value)