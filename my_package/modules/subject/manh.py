mon_hoc = {
    "Toan": {"Ma mon": "DAT101", "Giao vien": "Co Lan", "So tiet": 4, },
    "Van": {"Ma mon": "DAT102", "Giao vien": "Thay Tuan", "So tiet": 3, },
    "Anh van": {"Ma mon": "DAT103", "Giao vien": "Co Hnh", "So tiet": 2, },
    "Hoa hoc": {"Ma mon": "DAT104", "Giao vien": "Thay Minh", "So tiet": 3, },
}


def xac_nhan():
    while True:
        y_n = input('Ban co muon tiep tuc thao tac khong (Y/N): ').upper()
        if y_n == 'Y':
            return True
        elif y_n == 'N':
            return False
        else:
            print('Lua chon khong hop le, vui long thao tac lai.')


def hien_thi_danh_sach_mon_hoc():
    print("Danh sach mon hoc:")
    for mon, thong_tin in mon_hoc.items():
        print(
            f"Mon: {mon}, Ma mon: {thong_tin['Ma mon']}, Giao vien: {thong_tin['Giao vien']}, So tiet: {thong_tin['So tiet']}")


def tim_kiem_mon():
    ten = input("Nhap ten mon can tim: ")
    if ten in mon_hoc:
        thong_tin = mon_hoc[ten]
        print(
            f"Tim thay mon: {ten}, Ma mon: {thong_tin['Ma mon']}, Giao vien: {thong_tin['Giao vien']}, So tiet: {thong_tin['So tiet']}")
    else:
        print("Khong tim thay mon hoc.")


def them_mon_hoc():
    ten = input("Nhap ten mon hoc moi: ")
    ma_mon = input("Nhap ma mon: ")
    giao_vien = input("Nhap ten giao vien: ")
    so_tiet = int(input("Nhap so tiet: "))
    mon_hoc[ten] = {"Ma mon": ma_mon, "Giao vien": giao_vien, "So tiet": so_tiet}
    print(f"Them mon hoc {ten} thanh cong.")


def cap_nhat_mon():
    ten = input("Nhap ten mon hoc can cap nhat: ")
    if ten in mon_hoc:
        ma_mon = input("Nhap ma mon moi: ")
        giao_vien = input("Nhap giao vien moi: ")
        so_tiet = int(input("Nhap so tiet moi: "))
        mon_hoc[ten] = {"Ma mon": ma_mon, "Giao vien": giao_vien, "So tiet": so_tiet}
        print(f"Cap nhat thong tin mon {ten} thanh cong.")
    else:
        print("Khong tim thay mon hoc.")


def xoa_mon():
    ten = input("Nhap ten mon hoc can xoa: ")
    if ten in mon_hoc:
        if xac_nhan():
            del mon_hoc[ten]
            print(f"Xoa mon hoc {ten} thanh cong.")
    else:
        print("Khong tim thay mon hoc.")


def tinh_tin_chi_tong():
    tong_so_tiet = sum(mon["So tiet"] for mon in mon_hoc.values())
    print(f"Tong so tiet cua tat ca cac mon: {tong_so_tiet}")


def liet_ke_mon_hoc_theo_giao_vien():
    giao_vien = input("Nhap ten giao vien: ")
    ds_mon_hoc = [mon for mon, thong_tin in mon_hoc.items() if thong_tin["Giao vien"] == giao_vien]
    if ds_mon_hoc:
        print(f"Cac mon hoc do giao vien {giao_vien} giang day: {', '.join(ds_mon_hoc)}")
    else:
        print(f"Khong tim thay mon hoc cua giao vien {giao_vien}.")


def sap_xep_mon_hoc_theo_tin_chi():
    mon_sap_xep = sorted(mon_hoc.items(), key=lambda x: x[1]["So tiet"], reverse=True)
    print("Sap xep cac mon hoc theo so tiet:")
    for mon, thong_tin in mon_sap_xep:
        print(f"Mon: {mon}, So tiet: {thong_tin['So tiet']}")


def thong_ke_so_luong_mon_hoc():
    print(f"Co {len(mon_hoc)} mon hoc hien co trong danh sach.")


def kiem_tra_mon_hoc_ton_tai():
    ten = input("Nhap ten mon hoc can kiem tra: ")
    if ten in mon_hoc:
        print(f"Mon hoc {ten} ton tai trong danh sach.")
    else:
        print(f"Mon hoc {ten} khong ton tai trong danh sach.")


def menu_module_4():
    print('----- QUAN LY MON HOC -----')
    print("1. Hien thi danh sach mon hoc")
    print("2. Tim kiem/Loc mon hoc")
    print("3. Them mon hoc moi")
    print("4. Cap nhat mon hoc")
    print("5. Xoa mon hoc")
    print("6. Tinh tong chinh chi")
    print("7. Liet ke mon hoc theo giao vien")
    print("8. Sap xep mon hoc theo so tiet")
    print("9. Thong ke so luong mon hoc")
    print("10. Kiem tra mon hoc ton tai")
    print("0. Thoat")


def main_module_4():
    while True:
        menu_module_4()
        lua_chon = input("Chon mot chuc nang: ")

        if lua_chon == "1":
            hien_thi_danh_sach_mon_hoc()
        elif lua_chon == "2":
            tim_kiem_mon()
        elif lua_chon == "3":
            them_mon_hoc()
        elif lua_chon == "4":
            cap_nhat_mon()
        elif lua_chon == "5":
            xoa_mon()
        elif lua_chon == "6":
            tinh_tin_chi_tong()
        elif lua_chon == "7":
            liet_ke_mon_hoc_theo_giao_vien()
        elif lua_chon == "8":
            sap_xep_mon_hoc_theo_tin_chi()
        elif lua_chon == "9":
            thong_ke_so_luong_mon_hoc()
        elif lua_chon == "10":
            kiem_tra_mon_hoc_ton_tai()
        elif lua_chon == "0":
            if xac_nhan():
                print("Thoat chuong trinh.")
                break
        else:
            print("Lua chon khong hop le, vui long thu lai.")



