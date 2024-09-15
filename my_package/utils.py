"""------------------------------------
File này chứa các function tiện ích có thể 
tái sử dụng trong toàn dự án. 
------------------------------------"""

# Ví dụ 
def check_number(value):
    """
    Kiểm tra xem giá trị đầu vào có phải là số thực dương hay không.
    
    :param value: Giá trị đầu vào bất kỳ
    :return: True nếu giá trị là số thực dương, False nếu không phải
    """
    try:
        number = float(value)
        return number > 0
    except ValueError:
        return False
