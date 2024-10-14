from my_package.common.constant.constant_score import confirm_exit, menu_view, out_application
from my_package.modules.grade_point.grade_point_check import thoat_chuong_trinh
from my_package.modules.score.controller.score_controller import ScoreController

def menu_controller():
    controller = ScoreController("score.txt")
    while True:
        menu_view()

        choice = input("Chọn một lựa chọn: ").strip()

        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                controller.display_scores()
            elif choice == 2:
                controller.filter_scores()
            elif choice == 3:
                controller.add_score()
            elif choice == 4:
                controller.update_score()
            elif choice == 5:
                controller.delete_score()
            elif choice == 6:
                print("Chức năng chưa hoàn thiện.")
            elif choice == 7:
                controller.search_scores()
            elif choice == 8:
                controller.export_scores()
            elif choice == 9:
                controller.export_average_scores()
            elif choice == 10:
                controller.export_data_to_csv()
            elif choice == 0:
                if out_application():
                    print("Cảm ơn bạn đã sử dụng chức năng !")
                    break
                else:
                    print("Tiếp tục trải nghiệm chức năng này")
            else:
                print("❌ Lựa chọn không hợp lệ. Vui lòng nhập số từ 0 đến 5.")
        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng nhập một số.")


