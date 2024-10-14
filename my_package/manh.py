def ds_menu():
    print("\n--- QUẢN LÝ Môn HỌC ---")
    print("1. Hiển thị danh sách môn học")
    print("2. Tìm kiếm/Lọc môn ")
    print("3. Thêm môn học mới mới")
    print("4. Cập nhật môn học")
    print("5. Xóa môn học")
    print("6. Tính tổng chính chỉ")
    print("7.Liệt kê môn học theo giáo viên ")
    print("8. Sắp xếp môn học theo tính chỉ")
    print("9. Thống kê số lượng môn hiện có")
    print("10. Kiểm tra số lượng môn học đang tồn tại")
    print("0. Thoát")

def ma_mon():
    print("Hiển thị mã môn học: ")

def ten_mon():
    print("Tìm kiếm/Lọc môn học: ")

def them_mon_hoc():
    print("Thêm mới môn học:")

def cap_nhat_mon():
    print("Cập nhật môn học: ")

def xoa_mon():
    print("Xóa môn học: ")

def tinh_tin_chi_tong():
    print("Tính tổng chính chỉ: ")

def liet_ke_mon_hoc_theo_giao_vien():
    print("Liệt kê môn học theo giáo viên: ")

def sap_xep_mon_hoc_theo_tin_chi():
    print("Sắp xếp môn học theo tính chỉ: ")

def thong_ke_so_luong_mon_hoc():
    print("Thống kê số lượng môn hiện có: ")

def kiem_tra_mon_hoc_ton_tai():
    print("Kiểm tra số lượng môn học đang tồn tại: ")
def main_module4():
    while True:
        ds_menu()
        Lua_chon = input("Chọn một chức năng: ")
        
        if Lua_chon == "1":
            ma_mon()
        elif Lua_chon == "2":
            ten_mon()
        elif Lua_chon == "3":
            them_mon_hoc()
        elif Lua_chon == "4":
            cap_nhat_mon()
        elif Lua_chon == "5":
            xoa_mon()
        elif Lua_chon == "6":
            tinh_tin_chi_tong
        elif Lua_chon == "7":
            liet_ke_mon_hoc_theo_giao_vien
        elif Lua_chon == "8":
            sap_xep_mon_hoc_theo_tin_chi
        elif Lua_chon == "9":
            thong_ke_so_luong_mon_hoc
        elif Lua_chon == "10":
            kiem_tra_mon_hoc_ton_tai
        elif Lua_chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")