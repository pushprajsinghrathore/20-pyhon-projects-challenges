# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s1gjMX9PAuUWd-YpvaEUMBfpynpp4DLl
"""

# 1st  condication  is all  alphabtaic  a to z  charcter are use in  email is small and digit is use 0 to 9
# 2nd condication  only one special character are use  @  , underscore, .
# 3rd minimum length is use in email  6 and grater than 6
# regex ke thorouh kisi bhi srting me se special   character ko search krne ke  liye   hum \ slace ka use kr te he
# ?  use because you use  (. (dot) and (_ under score) at least on time if you use more than  one time it  will be show error
# \w use for  searche  special charcter on string and $ dollar sign use to rverse postion
import re
email_condition= "^[a-z]+[\._]?+[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("enter your email : ")
if re.search(email_condition,user_email):
    print("right email")
else:
    print("wrong email")

import re
email_condition= "^[a-z]+[\._]?+[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("enter your email : ")

if re.search(email_condition,user_email):
    print("right email")
else:
    print("wrong email")

