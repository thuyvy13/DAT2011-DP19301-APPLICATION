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

def chuc_nang_1():
    print('Hiển thị danh sách sinh viên.')
def chuc_nang_2():
    print('Tìm kiếm sinh viên.')

def chuc_nang_3():
    print('Thêm mới sinh viên')
    while True:
        xac_nhan = input('Mời nhập xác nhận (Y/N): ').upper().strip()
        if xac_nhan == 'Y':
            print("Đang thêm mới sinh viên...")
            # Code xử lý thêm sinh viên ở đây
            break
        elif xac_nhan == 'N':
            print("Thêm mới sinh viên đã bị hủy.")
            break
        elif xac_nhan == '':
            print("Bạn chưa nhập giá trị, vui lòng nhập lại (Y/N).")
        else:
            print("Giá trị không hợp lệ, vui lòng nhập lại (Y/N).")

def chuc_nang_4():
    print('Cập nhật thông tin sinh viên')
    while True:
        xac_nhan = input('Mời nhập xác nhận (Y/N): ').upper().strip()
        if xac_nhan == 'Y':
            print("Đang cập nhật thông tin sinh viên...")
            # Code xử lý cập nhật sinh viên ở đây
            break
        elif xac_nhan == 'N':
            print("Cập nhật thông tin sinh viên đã bị hủy.")
            break
        elif xac_nhan == '':
            print("Bạn chưa nhập giá trị, vui lòng nhập lại (Y/N).")
        else:
            print("Giá trị không hợp lệ, vui lòng nhập lại (Y/N).")

def chuc_nang_5():
    print('Xóa sinh viên')
    while True:
        xac_nhan = input('Mời nhập xác nhận (Y/N): ').upper().strip()
        if xac_nhan == 'Y':
            print("Đang xóa sinh viên...")
            # Code xử lý xóa sinh viên ở đây
            break
        elif xac_nhan == 'N':
            print("Xóa sinh viên đã bị hủy.")
            break
        elif xac_nhan == '':
            print("Bạn chưa nhập giá trị, vui lòng nhập lại (Y/N).")
        else:
            print("Giá trị không hợp lệ, vui lòng nhập lại (Y/N).")

def chuc_nang_6():
    print('Thống kê số lượng sinh viên theo lớp.')  

def chuc_nang_7():
    print('Sắp xếp sinh viên theo mã.')

def chuc_nang_8():
    print('Thống kê sinh viên theo bộ môn.')

def chuc_nang_9():
    print('Hiển thị sinh viên theo độ tuổi(tăng hoặc giảm).')

def chuc_nang_10():
    print('Xuất dữ liệu.')

def chuc_nang_0():
    
    print('chức năng 0')





def menu_module_3():
    while True:
        print('\n ------------Quản lý sinh viên------------ ')
        print('1. Hiển thị danh sách sinh viên. ')
        print('2. Tìm kiếm sinh viên. ')
        print('3. Thêm mới sinh viên. ')
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

#print('khanlv')
#print("dat2011_gr2")