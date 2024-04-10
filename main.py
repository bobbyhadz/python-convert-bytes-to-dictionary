# Convert Bytes to Dictionary in Python

from ast import literal_eval

my_bytes = b"{'first': 'bobby', 'last': 'hadz'}"

my_dict = literal_eval(my_bytes.decode('utf-8'))
print(my_dict)  # 👉️ {'first': 'bobby', 'last': 'hadz'}
print(type(my_dict))  # 👉️ <class 'dict'>