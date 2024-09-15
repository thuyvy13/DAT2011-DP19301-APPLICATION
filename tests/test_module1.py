import unittest
from datetime import datetime
from my_package.score import Score

class TestScore(unittest.TestCase):
    
    def setUp(self):
        # Thiết lập đối tượng Score để kiểm tra
        self.score = Score(score_id=1, student="Sinh viên A", subject="Toán", entry_date="01/09/23", score=7.5)
    
    def test_validate_entry_date_valid(self):
        # Kiểm tra với ngày hợp lệ
        entry_date_str = "01/09/23"
        result = self.score.validate_entry_date(entry_date_str)
        expected = datetime.strptime(entry_date_str, "%d/%m/%y")
        self.assertEqual(result, expected)
    
    def test_validate_entry_date_invalid(self):
        # Kiểm tra với ngày không hợp lệ
        entry_date_str = "32/09/23"
        result = self.score.validate_entry_date(entry_date_str)
        self.assertIsInstance(result, datetime)  # Kết quả phải là ngày hiện tại
    
    def test_validate_score_valid(self):
        # Kiểm tra điểm hợp lệ
        result = self.score.validate_score(9.5)
        self.assertEqual(result, 9.5)
    
    def test_validate_score_invalid(self):
        # Kiểm tra điểm không hợp lệ
        with self.assertRaises(ValueError):
            self.score.validate_score(11)  # Điểm phải từ 0 đến 10
    
    def test_update_score(self):
        # Kiểm tra cập nhật điểm
        self.score.update_score(8.0)
        self.assertEqual(self.score.score, 8.0)
    
    def test_display_info(self):
        # Kiểm tra hàm hiển thị thông tin
        self.score.display_info()  # In thông tin, không có lỗi xảy ra
    
if __name__ == "__main__":
    unittest.main()
