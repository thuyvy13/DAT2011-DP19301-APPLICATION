"""------------------------------------
File này chứa các function tiện ích có thể 
tái sử dụng trong toàn dự án. 
------------------------------------"""
from datetime import datetime
import re

def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return user_input
        else:
            print("Giá trị không hợp lệ. Vui lòng nhập lại!")
    
def get_str_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isalpha():
            return user_input
        else:
            print("Giá trị không hợp lệ. Vui lòng nhập lại!")

def get_date_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            date = datetime.strptime(user_input, "%d/%m/%Y")
            return date
        except ValueError:
            print("Ngày không hợp lệ. Vui lòng nhập theo định dạng dd/mm/yyyy")
            
def is_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def get_email_input(prompt):
    while True:
        user_input = input(prompt)
        if is_email(user_input):
            return user_input
        else: 
            print("Địa chỉ email không hợp lệ. Vui lòng nhập lại!")
            
def check_number_str(input_str_num):
    str = False
    number = False
    
    for char in input_str_num:
        if char.isalpha():
            str = False
        if char.isdigit():
            number = False
            
            