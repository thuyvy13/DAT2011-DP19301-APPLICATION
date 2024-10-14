# 3. Sinh viên(Mã, Tên, Ngày sinh, Email, Lớp, Bộ môn)
"""------------------------------------
Module3 này quản lý thông tin của sinh viên.
Bao gồm các thuộc tính:
- Mã: Mã số sinh viên (ID)
- Tên: Họ và tên của sinh viên
- Ngày sinh: Ngày sinh của sinh viên
- Email: Địa chỉ email của sinh viên
- Lớp: Lớp mà sinh viên đang theo học
- Bộ môn: Bộ môn hoặc khoa mà sinh viên thuộc về
------------------------------------"""
from my_package.modules.student.utils_student import validate_ma_sinh_vien, validate_ngay_sinh, validate_email, \
    validate_lop, exit_chuc_nang3


# class Student:
#     def __init__(self, student_id, name, birth_date, email, class_name, department):
#         """
#         student_id: mã sinh viên
#         name: tên sinh viên
#         birth_date: ngày sinh của sinh viên
#         email: email của sinh viên
#         class_name: lớp của sinh viên
#         department: bộ môn của sinh viên
#         """
#         self.student_id = student_id
#         self.name = name
#         self.birth_date = birth_date
#         self.email = email
#         self.class_name = class_name
#         self.department = department

# Lớp Student đại diện cho một sinh viên
class Student:
    def __init__(self, ma_sinh_vien, ten, ngay_sinh, email, lop, bo_mon):
        """
        Khởi tạo đối tượng sinh viên với các thuộc tính:
        - ma_sinh_vien: mã sinh viên
        - ten: tên sinh viên
        - ngay_sinh: ngày sinh của sinh viên
        - email: email của sinh viên
        - lop: lớp sinh viên đang theo học
        - bo_mon: bộ môn của sinh viên
        """
        self.ma_sinh_vien = ma_sinh_vien
        self.ten = ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.lop = lop
        self.bo_mon = bo_mon

# Danh sách lưu trữ các đối tượng sinh viên
students = [
    Student('PH00001', 'Nguyen Van A', '10/05/2000', 'nguyenvana@example.com', 'CNTT1', 'Công nghệ thông tin'),
    Student('PH00002', 'Tran Thi B', '12/08/2001', 'tranthib@example.com', 'KT2', 'Kinh tế'),
    Student('PH00003', 'Le Van C', '22/03/1999', 'levanc@example.com', 'CNTT2', 'Công nghệ thông tin')
]


def cap_nhat_file_csv(file_name='students.csv'):
    try:
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Ghi tiêu đề các cột
            writer.writerow(['Mã SV', 'Họ và Tên', 'Ngày sinh', 'Email', 'Lớp', 'Bộ môn'])
            
            # Ghi dữ liệu sinh viên
            for student in students:
                writer.writerow([student.ma_sinh_vien, student.ten, student.ngay_sinh, student.email, student.lop, student.bo_mon])
        print(f"Dữ liệu đã được cập nhật vào file '{file_name}'.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi cập nhật file CSV: {e}")

# Chức năng 1: Hiển thị danh sách sinh viên
def chuc_nang_1():
    print('Hiển thị danh sách sinh viên:')
    
    if len(students) == 0:
        print("Không có sinh viên nào trong danh sách.")
    else:
        # In tiêu đề các cột bằng tiếng Việt
        print(f"{'Mã SV':<10} {'Họ và Tên':<20} {'Ngày sinh':<12} {'Email':<30} {'Lớp':<8} {'Bộ môn'}")
        print('-' * 80)
        
        # Duyệt qua danh sách sinh viên và in thông tin
        for student in students:
            print(f"{student.ma_sinh_vien:<10} {student.ten:<20} {student.ngay_sinh:<12} {student.email:<30} {student.lop:<8} {student.bo_mon}")

# Chức năng 2: Thêm sinh viên mới (bao gồm validate dữ liệu)
# def chuc_nang_2():
#     print('Thêm sinh viên mới:')
#     while True:
#         ma_sinh_vien = input("Nhập mã sinh viên: ").strip()
#         ten = input("Nhập tên sinh viên: ").strip()

#         # Validate ngày sinh
#         while True:
#             ngay_sinh = input("Nhập ngày sinh (DD/MM/YYYY): ").strip()
#             if validate_ngay_sinh(ngay_sinh):
#                 break
#             else:
#                 print("Ngày sinh không hợp lệ. Vui lòng nhập lại.")
        

#         # Validate email
#         while True:
#             email = input("Nhập email sinh viên: ").strip()
#             if validate_email(email):
#                 break
#             else:
#                 print("Email không hợp lệ. Vui lòng nhập lại.")
        
#         lop = input("Nhập lớp: ").strip()
#         bo_mon = input("Nhập bộ môn: ").strip()

#         # Xác nhận trước khi thêm sinh viên
#         if exit_chuc_nang3():
#             sinh_vien_moi = Student(ma_sinh_vien, ten, ngay_sinh, email, lop, bo_mon)
#             students.append(sinh_vien_moi)
#             print(f"Đã thêm sinh viên {ten}.")
#         else:
#             print("Thêm mới sinh viên đã bị hủy.")
#         break

# import re
# from datetime import datetime

# def validate_ngay_sinh(ngay_sinh):
#     # Kiểm tra định dạng ngày sinh DD/MM/YYYY
#     try:
#         datetime.strptime(ngay_sinh, '%d/%m/%Y')
#         # Kiểm tra xem ngày có lớn hơn ngày hiện tại hay không
#         if datetime.strptime(ngay_sinh, '%d/%m/%Y') > datetime.today():
#             return False
#         return True
#     except ValueError:
#         return False

# def validate_email(email):
#     # Tạo regex cho email
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return re.match(pattern, email) is not None

# def validate_ma_sinh_vien(ma_sinh_vien):
#     # Kiểm tra định dạng mã sinh viên PH*****
#     pattern = r'^PH.{5}$'
#     return re.match(pattern, ma_sinh_vien) is not None

# def validate_lop(lop):
#     # Kiểm tra định dạng lớp DP*****
#     pattern = r'^DP.{5}$'
#     return re.match(pattern, lop) is not None

# def exit_chuc_nang3():
#     while True:
#         xac_nhan = input('Mời nhập xác nhận (Y/N): ').upper().strip()
#         if xac_nhan == 'Y':
#             return True
#         elif xac_nhan == 'N':
#             print("Cập nhật thông tin sinh viên đã bị hủy.")
#             return False
#         elif xac_nhan == '':
#             print("Bạn chưa nhập giá trị, vui lòng nhập lại (Y/N).")
#         else:
#             print("Giá trị không hợp lệ, vui lòng nhập lại (Y/N).")

def chuc_nang_2():
    print('Thêm sinh viên mới:')
    while True:
        while True:
            ma_sinh_vien = input("Nhập mã sinh viên (PH12345): ").strip()
            if validate_ma_sinh_vien(ma_sinh_vien):
                break
            else:
                print("Mã sinh viên không hợp lệ. Vui lòng nhập lại.")

        ten = input("Nhập tên sinh viên: ").strip()

        # Validate ngày sinh
        while True:
            ngay_sinh = input("Nhập ngày sinh (DD/MM/YYYY): ").strip()
            if validate_ngay_sinh(ngay_sinh):
                break
            else:
                print("Ngày sinh không hợp lệ. Vui lòng nhập lại.")

        # Validate email
        while True:
            email = input("Nhập email sinh viên: ").strip()
            if validate_email(email):
                break
            else:
                print("Email không hợp lệ. Vui lòng nhập lại.")
        
        while True:
            lop = input("Nhập lớp (DP19301): ").strip()
            if validate_lop(lop):
                break
            else:
                print("Lớp không hợp lệ. Vui lòng nhập lại.")
                
        bo_mon = input("Nhập bộ môn: ").strip()

        # Xác nhận trước khi thêm sinh viên
        if exit_chuc_nang3():
            sinh_vien_moi = Student(ma_sinh_vien, ten, ngay_sinh, email, lop, bo_mon)
            students.append(sinh_vien_moi)
            print(f"Đã thêm sinh viên {ten}.")
            cap_nhat_file_csv()  # Cập nhật file CSV sau khi thêm sinh viên mới
        else:
            print("Thêm mới sinh viên đã bị hủy.")
        break


# Chức năng 3: Tìm kiếm sinh viên theo mã
# def chuc_nang_3():
#     print('Tìm kiếm sinh viên:')
#     ma_sv = input("Nhập mã sinh viên cần tìm: ").strip()
#     found = False
#     for student in students:
#         if student.ma_sinh_vien == ma_sv:
#             print(f"Tìm thấy sinh viên: {student.ten}, Ngày sinh: {student.ngay_sinh}, Email: {student.email}, Lớp: {student.lop}, Bộ môn: {student.bo_mon}")
#             found = True
#             break
#     if not found:
#         print(f"Không tìm thấy sinh viên với mã {ma_sv}.")

import re

# Hàm tìm kiếm sinh viên bằng Regex
import re

# Hàm tìm kiếm sinh viên
def chuc_nang_3():
    print("Tìm kiếm sinh viên:")
    while True:
        lua_chon = input("Bạn muốn tìm kiếm theo (1) Tên, (2) Mã sinh viên, (3) Email: ").strip()
        
        if lua_chon == '1':
            while True:
                pattern = input("Nhập tên cần tìm: ").strip()
                if pattern:  # Kiểm tra xem pattern có trống không
                    ket_qua = tim_kiem_theo_regex('ten', pattern)
                    if ket_qua:
                        break
                    else:
                        print("Không tìm thấy sinh viên nào phù hợp với tên đã nhập.")
                        if not tiep_tuc_hoac_quay_lai():
                            return
                else:
                    print("Tên tìm kiếm không được để trống. Vui lòng nhập lại.")
        elif lua_chon == '2':
            while True:
                pattern = input("Nhập mã sinh viên cần tìm (PH12345): ").strip()
                if pattern:
                    ket_qua = tim_kiem_theo_regex('ma_sinh_vien', pattern)
                    if ket_qua:
                        break
                    else:
                        print("Không tìm thấy sinh viên nào phù hợp với mã sinh viên đã nhập.")
                        if not tiep_tuc_hoac_quay_lai():
                            return
                else:
                    print("Mã sinh viên tìm kiếm không được để trống. Vui lòng nhập lại.")
        elif lua_chon == '3':
            while True:
                pattern = input("Nhập email cần tìm (khanlv@gmail.com): ").strip()
                if pattern:
                    ket_qua = tim_kiem_theo_regex('email', pattern)
                    if ket_qua:
                        break
                    else:
                        print("Không tìm thấy sinh viên nào phù hợp với email đã nhập.")
                        if not tiep_tuc_hoac_quay_lai():
                            return
                else:
                    print("Email tìm kiếm không được để trống. Vui lòng nhập lại.")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn 1, 2 hoặc 3.")
            continue  # Tiếp tục vòng lặp nếu lựa chọn không hợp lệ

        break  # Thoát vòng lặp chính nếu tìm thấy kết quả

    # Hiển thị kết quả nếu tìm thấy sinh viên
    if ket_qua:
        print(f"Tìm thấy {len(ket_qua)} sinh viên:")
        print(f"{'Mã SV':<10} {'Họ và Tên':<20} {'Ngày sinh':<12} {'Email':<30} {'Lớp':<8} {'Bộ môn'}")
        print('-' * 80)
        for student in ket_qua:
            print(f"{student.ma_sinh_vien:<10} {student.ten:<20} {student.ngay_sinh:<12} {student.email:<30} {student.lop:<8} {student.bo_mon}")
    else:
        print("Không tìm thấy sinh viên nào phù hợp.")

# Hàm tìm kiếm theo thuộc tính sử dụng Regex
def tim_kiem_theo_regex(thuoc_tinh, pattern):
    ket_qua = []
    for student in students:
        gia_tri = getattr(student, thuoc_tinh)
        if re.search(pattern, gia_tri, re.IGNORECASE):  # Tìm kiếm không phân biệt chữ hoa/thường
            ket_qua.append(student)
    return ket_qua

# Hàm hỏi người dùng muốn tìm kiếm tiếp hoặc quay lại menu
def tiep_tuc_hoac_quay_lai():
    while True:
        lua_chon = input("Bạn có muốn tìm kiếm tiếp không? (Y để tiếp tục, N để quay lại menu): ").strip().upper()
        if lua_chon == 'Y':
            return True  # Tiếp tục tìm kiếm
        elif lua_chon == 'N':
            print("Quay lại menu chính.")
            return False  # Quay lại menu
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn Y hoặc N.")


# Chức năng 4: Cập nhật thông tin sinh viên
def chuc_nang_4():
    print('Cập nhật thông tin sinh viên:')
    
    while True:
        ma_sv = input("Nhập mã sinh viên cần cập nhật: ").strip()
        found_student = None
        
        # Tìm kiếm sinh viên theo mã
        for student in students:
            if student.ma_sinh_vien == ma_sv:
                found_student = student
                break
        
        if found_student:
            print(f"Đang cập nhật thông tin cho sinh viên: {found_student.ten}")
            
            # Cập nhật thông tin sinh viên
            found_student.ten = input(f"Tên hiện tại: {found_student.ten}, Nhập tên mới (hoặc bấm Enter để giữ nguyên): ").strip() or found_student.ten
            found_student.lop = input(f"Lớp hiện tại: {found_student.lop}, Nhập lớp mới (hoặc bấm Enter để giữ nguyên): ").strip() or found_student.lop
            found_student.bo_mon = input(f"Bộ môn hiện tại: {found_student.bo_mon}, Nhập bộ môn mới (hoặc bấm Enter để giữ nguyên): ").strip() or found_student.bo_mon
            
            # Validate email
            while True:
                new_email = input(f"Email hiện tại: {found_student.email}, Nhập email mới (hoặc bấm Enter để giữ nguyên): ").strip() or found_student.email
                if validate_email(new_email):
                    found_student.email = new_email
                    break
                else:
                    print("Email không hợp lệ, vui lòng nhập lại.")
            
            # Validate ngày sinh
            while True:
                new_ngay_sinh = input(f"Ngày sinh hiện tại: {found_student.ngay_sinh}, Nhập ngày sinh mới (DD/MM/YYYY hoặc bấm Enter để giữ nguyên): ").strip() or found_student.ngay_sinh
                if validate_ngay_sinh(new_ngay_sinh):
                    found_student.ngay_sinh = new_ngay_sinh
                    break
                else:
                    print("Ngày sinh không hợp lệ, vui lòng nhập lại.")
            
            print("Thông tin sinh viên đã được cập nhật.")
            cap_nhat_file_csv()
            break  # Thoát khỏi vòng lặp sau khi cập nhật xong
        else:
            print(f"Không tìm thấy sinh viên với mã {ma_sv}.")
            
            # Hỏi người dùng muốn nhập lại hay quay lại menu
            while True:
                lua_chon = input("Bạn có muốn nhập lại mã sinh viên khác không? (Y để tiếp tục, N để quay lại menu): ").strip().upper()
                if lua_chon == 'Y':
                    break  # Cho phép nhập lại mã sinh viên khác
                elif lua_chon == 'N':
                    print("Quay lại menu chính.")
                    return  # Quay lại menu chính
                else:
                    print("Lựa chọn không hợp lệ, vui lòng nhập lại Y hoặc N.")

# Chức năng 5: Xóa sinh viên
def chuc_nang_5():
    print('Xóa sinh viên')
    
    # Kiểm tra nếu danh sách sinh viên rỗng
    if len(students) == 0:
        print("Không có sinh viên nào trong danh sách để xóa.")
        return
    
    # Hiển thị danh sách sinh viên trước khi xóa
    print("Danh sách sinh viên hiện có:")
    print(f"{'Mã SV':<10} {'Họ và Tên':<20} {'Ngày sinh':<12} {'Email':<30} {'Lớp':<8} {'Bộ môn'}")
    print('-' * 80)
    for student in students:
        print(f"{student.ma_sinh_vien:<10} {student.ten:<20} {student.ngay_sinh:<12} {student.email:<30} {student.lop:<8} {student.bo_mon}")
    
    while True:
        # Yêu cầu người dùng nhập mã sinh viên cần xóa
        ma_sv = input("Nhập mã sinh viên muốn xóa: ").strip()
        found_student = None
        
        # Tìm sinh viên có mã phù hợp
        for student in students:
            if student.ma_sinh_vien == ma_sv:
                found_student = student
                break
        
        # Xóa sinh viên nếu tìm thấy
        if found_student:
            if exit_chuc_nang3():
                students.remove(found_student)
                print(f"Đã xóa sinh viên {found_student.ten}.")
                cap_nhat_file_csv()
            else:
                print("Xóa sinh viên đã bị hủy.")
            break  # Thoát khỏi vòng lặp sau khi hoàn thành xóa
        else:
            print(f"Không tìm thấy sinh viên với mã {ma_sv}.")
            
            # Cho người dùng lựa chọn xóa tiếp hoặc quay lại menu
            while True:
                lua_chon = input("Bạn có muốn xóa sinh viên khác không? (Y để tiếp tục, N để quay lại menu): ").strip().upper()
                if lua_chon == 'Y':
                    break  # Cho phép nhập lại mã sinh viên khác
                elif lua_chon == 'N':
                    print("Quay lại menu chính.")
                    return  # Quay lại menu chính
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập lại Y hoặc N.")

# # Hàm validate ngày sinh
# def validate_ngay_sinh(ngay_sinh):
#     from datetime import datetime
#     try:
#         sinh_nhat = datetime.strptime(ngay_sinh, "%d/%m/%Y")
#         if sinh_nhat > datetime.now():
#             return False
#         return True
#     except ValueError:
#         return False

# # Hàm validate email
# import re
# def validate_email(email):
#     email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#     return re.match(email_regex, email) is not None

# # Hàm xác nhận trước khi thực hiện hành động
# def exit_chuc_nang3():
#     while True:
#         xac_nhan = input('Mời nhập xác nhận (Y/N): ').upper().strip()
#         if xac_nhan == 'Y':
#             return True
#         elif xac_nhan == 'N':
#             print("Hành động đã bị hủy.")
#             return False
#         elif xac_nhan == '':
#             print("Bạn chưa nhập giá trị, vui lòng nhập lại (Y/N).")
#         else:
#             print("Giá trị không hợp lệ, vui lòng nhập lại (Y/N).")

           
def chuc_nang_6():
    print('Thống kê số lượng sinh viên theo lớp.')
    
    # Tạo một dictionary để lưu số lượng sinh viên theo lớp
    thong_ke_lop = {}
    for student in students:
        if student.lop in thong_ke_lop:
            thong_ke_lop[student.lop] += 1
        else:
            thong_ke_lop[student.lop] = 1
    
    # Hiển thị kết quả thống kê
    if thong_ke_lop:
        print(f"{'Lớp':<10} {'Số lượng sinh viên':<20}")
        print('-' * 30)
        for lop, so_luong in thong_ke_lop.items():
            print(f"{lop:<10} {so_luong:<20}")
    else:
        print("Hiện không có sinh viên nào.")

def chuc_nang_7():
    print('Sắp xếp sinh viên theo mã.')
    
    # Sắp xếp danh sách sinh viên theo mã sinh viên
    sorted_students = sorted(students, key=lambda x: x.ma_sinh_vien)
    
    # Hiển thị danh sách sinh viên đã được sắp xếp
    print(f"{'Mã SV':<10} {'Họ và Tên':<20} {'Ngày sinh':<12} {'Email':<30} {'Lớp':<8} {'Bộ môn'}")
    print('-' * 80)
    for student in sorted_students:
        print(f"{student.ma_sinh_vien:<10} {student.ten:<20} {student.ngay_sinh:<12} {student.email:<30} {student.lop:<8} {student.bo_mon}")

def chuc_nang_8():
    print('Thống kê sinh viên theo bộ môn.')
    
    # Tạo một dictionary để lưu số lượng sinh viên theo bộ môn
    thong_ke_bo_mon = {}
    for student in students:
        if student.bo_mon in thong_ke_bo_mon:
            thong_ke_bo_mon[student.bo_mon] += 1
        else:
            thong_ke_bo_mon[student.bo_mon] = 1
    
    # Hiển thị kết quả thống kê
    if thong_ke_bo_mon:
        print(f"{'Bộ môn':<20} {'Số lượng sinh viên':<20}")
        print('-' * 40)
        for bo_mon, so_luong in thong_ke_bo_mon.items():
            print(f"{bo_mon:<20} {so_luong:<20}")
    else:
        print("Hiện không có sinh viên nào.")

from datetime import datetime

def chuc_nang_9():
    print('Hiển thị sinh viên theo độ tuổi (tăng hoặc giảm).')
    
    # Yêu cầu người dùng nhập tùy chọn sắp xếp
    lua_chon = input("Bạn muốn sắp xếp theo độ tuổi tăng (T) hay giảm (G)? ").upper().strip()
    
    # Chuyển đổi ngày sinh thành độ tuổi
    def tinh_tuoi(ngay_sinh):
        ngay_sinh = datetime.strptime(ngay_sinh, '%d/%m/%Y')
        today = datetime.today()
        return today.year - ngay_sinh.year - ((today.month, today.day) < (ngay_sinh.month, ngay_sinh.day))
    
    # Sắp xếp theo độ tuổi
    if lua_chon == 'T':
        sorted_students = sorted(students, key=lambda x: tinh_tuoi(x.ngay_sinh))
    elif lua_chon == 'G':
        sorted_students = sorted(students, key=lambda x: tinh_tuoi(x.ngay_sinh), reverse=True)
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        return
    
    # Hiển thị danh sách sinh viên đã sắp xếp
    print(f"{'Mã SV':<10} {'Họ và Tên':<20} {'Ngày sinh':<12} {'Email':<30} {'Lớp':<8} {'Bộ môn':<20} {'Tuổi'}")
    print('-' * 100)
    for student in sorted_students:
        print(f"{student.ma_sinh_vien:<10} {student.ten:<20} {student.ngay_sinh:<12} {student.email:<30} {student.lop:<8} {student.bo_mon:<20} {tinh_tuoi(student.ngay_sinh)}")


import csv

def chuc_nang_10():
    print('Xuất dữ liệu sinh viên ra file CSV.')
    file_name = input('Nhập tên file (bao gồm .csv): ')
    
    try:
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Ghi tiêu đề các cột
            writer.writerow(['Mã SV', 'Họ và Tên', 'Ngày sinh', 'Email', 'Lớp', 'Bộ môn'])
            
            # Ghi dữ liệu sinh viên
            for student in students:
                writer.writerow([student.ma_sinh_vien, student.ten, student.ngay_sinh, student.email, student.lop, student.bo_mon])
        
        print(f"Dữ liệu đã được xuất ra file '{file_name}' thành công.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi xuất dữ liệu: {e}")

def chuc_nang_0():
    
    print('chức năng 0')





def menu_module_3():
    while True:
        print('\n ------------Quản lý sinh viên------------ ')
        print('1. Hiển thị danh sách sinh viên. ')
        print('2. Thêm mới sinh viên. ')
        print('3. Tìm kiếm sinh viên. ')
        print('4. Cập nhật thông tin sinh viên. ')
        print('5. Xóa sinh viên. ')
        print('6. Thống kê số lượng sinh viên theo lớp. ')
        print('7. Sắp xếp sinh viên theo mã. ')
        print('8. Thống kê sinh viên theo bộ môn: ')
        print('9. Hiển thị sinh viên theo độ tuổi(tăng hoặc giảm). ')
        print('10. Xuất dữ liệu. ')
        print('0. Thoát. \n')
        chuc_nang = input("Mời chọn chức năng: ")
        if chuc_nang == '1':
            chuc_nang_1()
        elif chuc_nang == '2':
            chuc_nang_2()
        elif chuc_nang == '3':
            chuc_nang_3()
        elif chuc_nang == '4':
            chuc_nang_4()
        elif chuc_nang == '5':
            chuc_nang_5()
        elif chuc_nang == '6':
            chuc_nang_6()
        elif chuc_nang == '7':
            chuc_nang_7()
        elif chuc_nang == '8':
            chuc_nang_8()
        elif chuc_nang == '9':
            chuc_nang_9()
        elif chuc_nang== '10':
            chuc_nang_10()
        elif chuc_nang == '0':
            xac_nhan = input('mời nhập xác nhận(Y/N): ')
            if xac_nhan.upper()=='Y':
                break
            else:
                print('thao tác bị hủy')
        else :
            print('Mời bạn chọn lại chức năng (1 - 10)')

