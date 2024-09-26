# 5. Học kỳ(Mã, Tên, Ngày bắt đầu, Ngày kết thúc, Ghi chú)
"""------------------------------------
Module5 này quản lý thông tin về học kỳ.
Bao gồm các thuộc tính:
- Mã: Mã học kỳ
- Tên: Tên của học kỳ
- Ngày bắt đầu: Ngày bắt đầu của học kỳ
- Ngày kết thúc: Ngày kết thúc của học kỳ
- Ghi chú: Ghi chú thêm liên quan đến học kỳ
------------------------------------"""


# class Semester:
#     def __init__(self, semester_id, name, start_date, end_date, notes):
#         """
#         semester_id: mã học kỳ
#         name: tên học kỳ
#         start_date: ngày bắt đầu học kỳ
#         end_date: ngày kết thúc học kỳ
#         notes: ghi chú về học kỳ
#         """
#         self.semester_id = semester_id
#         self.name = name
#         self.start_date = start_date
#         self.end_date = end_date
#         self.notes = notes
# 5. Học kỳ(Mã, Tên, Ngày bắt đầu, Ngày kết thúc, Ghi chú)

def hien_thi1():
    print("hiển thị danh sách học kì")

def tim_kiem2():
    print("Tìm kiếm học kỳ ")
    # tk = input("moi nhap thong tin can tim: ")
    # if tk in ds :
    #     print(f"thong tin tim kiem {tk} co trong danh sach: {ds} ")
    # else :
    #     print(f"thong tin tim kiem {tk} khong co trong danh sach: {ds}")
def them_moi3():
    print("Thêm mới học kỳ ")
    # ten_hoc_ky = str(input("mời nhập học kì: "))
    # nam_hoc = int(input("mời nhập năm học kì: "))
    # ds.append((ten_hoc_ky, nam_hoc))
    # print(f"Đã thêm học kỳ: {ten_hoc_ky} - Năm học: {nam_hoc}")
def cap_nhat4():
    print("cập nhật thông tin ")

def xoa_tt5():
    print("xóa thông tin")

def kiem_tra6():
    print("Kiểm tra học kỳ đã kết thúc hay chưa  ")

def tinh_tong7():
    print("Tính tổng số học kỳ")

def thong_ke8():
    print("Thống kê số lượng học kỳ trong một năm")

def ht_ghi_chu9():
    print("Hiển thị tất cả ghi chú  ")

def nhac_nho10():
    print("Nhắc nhở sự kiện trong học kỳ ")

def xac_nhan():
    xn = input("Bạn có chắc chắn muốn thực hiện thao tác này? (Y/N): ").upper()
    if xn == "N":
        hien_thi_menu()
    elif xn == "Y":
        print("Thoát chương trình")



def hien_thi_menu():
    while True :
        print("\n================== Quản lý Học Kỳ ======================")
        print("  ||     1. Hiển thị danh sách học kỳ              ||")
        print("  ||     2. Tìm kiếm học kỳ                        ||")
        print("  ||     3. Thêm mới học kỳ                        ||")
        print("  ||     4. Cập nhật học kỳ                        ||")
        print("  ||     5. Xóa học kỳ                             ||")
        print("  ||     6. Kiểm tra học kỳ đã kết thúc hay chưa   ||")
        print("  ||     7. Tính tổng số học kỳ                    ||")
        print("  ||     8. Thống kê số lượng học kỳ trong một năm ||")
        print("  ||     9. Hiển thị tất cả ghi chú                ||")
        print("  ||     10. Nhắc nhở sự kiện trong học kỳ         ||")
        print("  ||     0. thoát chương trình.                    ||")
        print("==========================================================")
        luaChon = int(input("Mời chọn chức năng (1-10) : "))
        if luaChon == 0 :
            xac_nhan()
            break
        elif luaChon == 1 :
            xn = input("Bạn có chắc chắn muốn thực hiện thao tác này? (Y/N): ").upper()
            if xn == "N":
                hien_thi_menu()
            elif xn == "Y":
                hien_thi1()
        elif luaChon == 2 :
            xn = input("Bạn có chắc chắn muốn thực hiện thao tác này? (Y/N): ").upper()
            if xn == "N":
                hien_thi_menu()
            elif xn == "Y":
                tim_kiem2()
        elif luaChon == 3 :
            xn = input("Bạn có chắc chắn muốn thực hiện thao tác này? (Y/N): ").upper()
            if xn == "N":
                hien_thi_menu()
            elif xn == "Y":
                them_moi3()
        elif luaChon == 4 :
            xn = input("Bạn có chắc chắn muốn thực hiện thao tác này? (Y/N): ").upper()
            if xn == "N":
                hien_thi_menu()
            elif xn == "Y":
                cap_nhat4()
        elif luaChon == 5 :
            xn = input("Bạn có chắc chắn muốn thực hiện thao tác này? (Y/N): ").upper()
            if xn == "N":
                hien_thi_menu()
            elif xn == "Y":
                xoa_tt5()
        elif luaChon == 6 :
            xn = input("Bạn có chắc chắn muốn thực hiện thao tác này? (Y/N): ").upper()
            if xn == "N":
                hien_thi_menu()
            elif xn == "Y":
                kiem_tra6()
        elif luaChon == 7 :
            xn = input("Bạn có chắc chắn muốn thực hiện thao tác này? (Y/N): ").upper()
            if xn == "N":
                hien_thi_menu()
            elif xn == "Y":
                tinh_tong7()
        elif luaChon == 8 :
            xn = input("Bạn có chắc chắn muốn thực hiện thao tác này? (Y/N): ").upper()
            if xn == "N":
                hien_thi_menu()
            elif xn == "Y":
                thong_ke8()
        elif luaChon == 9 :
            xn = input("Bạn có chắc chắn muốn thực hiện thao tác này? (Y/N): ").upper()
            if xn == "N":
                hien_thi_menu()
            elif xn == "Y":
                ht_ghi_chu9()
        elif luaChon == 10 :
            xn = input("Bạn có chắc chắn muốn thực hiện thao tác này? (Y/N): ").upper()
            if xn == "N":
                hien_thi_menu()
            elif xn == "Y":
                nhac_nho10()
        else :
            print("Mời bạn chọn lại (1-10)")

