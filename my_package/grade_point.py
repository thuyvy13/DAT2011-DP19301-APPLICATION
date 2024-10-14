# 2. Đầu điểm(Mã, Tên, Trọng số, Môn học, Phân loại)
from grade_point_check import thoat_chuong_trinh
from grade_point_make import display_scores , update_score , add_score , delete_score , check_subject_exists  
from grade_point_make import find_highest_score , Thong_ke , kiem_tra , kiem_tra_thua_thieu, xuat_file_csv


def GradePoint():
   
    while True:
        print("-------------------ĐẦU-ĐIỂM-----------------")
        print("|1. Hiển thị danh sách                      |")
        print("|2. Thêm vào đầu điểm                       |")
        print("|3. Xóa đầu điểm                            |")
        print("|4. Cập nhật đầu điểm                       |")
        print("|5. Tìm kiếm / Lọc                          |")
        print("|6. Kiểm tra đầu điểm có trọng số cao nhất  |")
        print("|7. Kiểm tra mã đầu điểm                    |")
        print("|8. Thống kê                                |")
        print("|9. Kiểm tra Số lượng thiếu đầu điểm        |")
        print("|10. Xuất file theo môn                     |")
        print("|0. Kết thúc chương trình                   |")
        print("--------------------------------------------")

        try:
            swap = int(input("Vui lòng chọn chương trình (0-10): "))
        except ValueError:
            print("Vui lòng nhập một số nguyên trong khoang (0-10).")
            continue 
            
        match swap:
            case 0:
                if thoat_chuong_trinh():
                    print("Cam on ban da su dung chuong trinh")
                    break
                else :
                    print("Chuong trinh duoc tiep tuc")
            case 1:
                display_scores()
            case 2:
                add_score()
            case 3:
                delete_score()
            case 4:
                update_score()
            case 5:
                check_subject_exists()
            case 6:
                find_highest_score()
            case 7:
                kiem_tra()
            case 8:
                Thong_ke()
            case 9:
                kiem_tra_thua_thieu()
            case 10:
                xuat_file_csv()
            case _:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.")

GradePoint()