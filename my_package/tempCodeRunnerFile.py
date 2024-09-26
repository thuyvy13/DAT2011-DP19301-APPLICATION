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

ds = [("Học kỳ 1", 2022), ("Học kỳ 2", 2022), ("Học kỳ 1", 2023)]
def hien_thi1(hienthi):
    print("danh sach hoc ki la")

def tim_kiem2(tk,ds):
    tk = input("moi nhap thong tin can tim: ")
    if tk in ds :
        print(f"thong tin tim kiem {tk} co trong danh sach: {ds} ")
    else :
        print(f"thong tin tim kiem {tk} khong co trong danh sach: {ds}")
def them_moi3(ten_hoc_ky, nam_hoc):
    ten_hoc_ky = str(input("mời nhập học kì: "))
    nam_hoc = int(input("mời nhập năm học kì: "))
    ds.append((ten_hoc_ky, nam_hoc))
    print(f"Đã thêm học kỳ: {ten_hoc_ky} - Năm học: {nam_hoc}")

def cap_nhat4():
    print("cap nhat thong tin ")

def xoa_tt5():
    print("xoa tt")

def kiem_tra6():
    print("cap nhat thong tin ")

def tinh_tong7():
    print("tinh tong")





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
        print("==========================================================")
        luaChon = int(input("Mời chọn chức năng (1-10) : "))
        if luaChon == 1 :
            print(hien_thi1())
        elif luaChon == 2 :
            print(tim_kiem2())
        elif luaChon == 3 :
            print(them_moi3())
        elif luaChon == 4 :
            print("4. Cập nhật học kỳ")
        elif luaChon == 5 :
            print("5. Xóa học kỳ ")
        elif luaChon == 6 :
            print("6. Kiểm tra học kỳ đã kết thúc hay chưa")
        elif luaChon == 7 :
            print("7. Tính tổng số học kỳ")
        elif luaChon == 8 :
            print("8. Thống kê số lượng học kỳ trong một năm")
        elif luaChon == 9 :
            print("9. Hiển thị tất cả ghi chú")
        elif luaChon == 10 :
            print("10. Nhắc nhở sự kiện trong học kỳ")
        else :
            print("Mời bạn chọn lại (1-10)")

hien_thi_menu()