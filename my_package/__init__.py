# Đây là file khởi tạo cho package `my_package`. 
# File này giúp Python nhận diện thư mục `my_package` như một package.
# Có thể import các module cần thiết ở đây để người dùng dễ sử dụng hơn.
from .score import Score
from .grade_point import GradePoint
from .student import Student
from .subject import Subject
from .semester import Semester


"""
my_package: Thư mục chứa mã nguồn của dự án.

File này để Python nhận diện đây là một package và cho phép import các module từ thư mục này.
"""
