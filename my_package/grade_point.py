# 2. Đầu điểm(Mã, Tên, Trọng số, Môn học, Phân loại)
"""------------------------------------
Module2 này quản lý thông tin về đầu điểm, tức là các thành phần điểm của sinh viên.
Bao gồm các thuộc tính:
- Mã: Mã định danh của đầu điểm
- Tên: Tên của đầu điểm (ví dụ: Thi cuối kỳ, Bài tập, v.v.)
- Trọng số: Tỷ lệ phần trăm của đầu điểm trong tổng điểm
- Môn học: Môn học mà đầu điểm thuộc về
- Phân loại: Loại của đầu điểm (ví dụ: lý thuyết, thực hành, v.v.)
------------------------------------"""


def hien_thi_danh_sach():
    print("Thực hiện hiển thị danh sách Đầu điểm")

def Them_vao_dau_diem():
    print("Thực hiện thêm học sinh")

def Xoa_Dau_diem():
    print("Thực hiện lệnh xóa Đầu điểm") 

def Cap_nhat_dau_diem():
    print("Thực hiện cập nhật Đầu điểm")

def Tim_kiem_Loc():
    print("Thực hiện tìm kiếm / lọc")

def Kiem_tra_dau_diem():
    print('Thực hiện kiểm tra đầu điểm nào có điểm số cao nhất') 

def Thong_ke():
    print("Thực hiện thống kê số lượng đầu điểm theo từng môn học")    

def kiem_tra():
    print("Kiểm tra sự tồn tại của mã đầu điểm")

def kiem_tra_hop_le():
    print("Kiểm tra tính hợp lệ (đủ, thiếu, thừa)")

def Xuat_file():
    print("Xuất file theo môn")


while True:
    print("-----------Đầu-Điểm-----------")
    print("|1. Hiển thị danh sách       |")
    print("|2. Thêm vào đầu điểm        |")
    print("|3. Xóa đầu điểm             |")
    print("|4. Cập nhật đầu điểm        |")
    print("|5. Tìm kiếm / Lọc           |")
    print("|6. Kiểm tra đầu điểm        |")
    print("|7. Kiểm tra mã đầu điểm     |")
    print("|8. Thống kê                 |")
    print("|9. Kiểm tra tính hợp lệ     |")
    print("|10. Xuất file theo môn      |")
    print("|0. Kết thúc chương trình    |")
    print("------------------------------")

    try:
        swap = int(input("Vui lòng chọn chương trình: "))
    except ValueError:
        print("Vui lòng nhập một số nguyên.")
        continue

    if swap == 0:
        print("Kết thúc chương trình.")
        break
    elif swap == 1:
        hien_thi_danh_sach()
    elif swap == 2:
        Them_vao_dau_diem()
    elif swap == 3:
        Xoa_Dau_diem()
    elif swap == 4:
        Cap_nhat_dau_diem()
    elif swap == 5:
        Tim_kiem_Loc()
    elif swap == 6:
        Kiem_tra_dau_diem()
    elif swap == 7:
        kiem_tra()
    elif swap == 8:
        Thong_ke()
    elif swap == 9:
        kiem_tra_hop_le()
    elif swap == 10:
        Xuat_file()
    
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")
