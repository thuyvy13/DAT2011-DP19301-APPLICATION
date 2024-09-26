import unittest
from datetime import datetime
from my_package.score import Score

class TestScore(unittest.TestCase):
    
    def setUp(self):
        self.score = Score(score_id=1, student="Sinh viên A", subject="Toán", entry_date="01/09/23", score=7.5)
    
    def test_validate_entry_date_valid(self):
        entry_date_str = "01/09/23"
        result = self.score.validate_entry_date(entry_date_str)
        expected = datetime.strptime(entry_date_str, "%d/%m/%y")
        self.assertEqual(result, expected)
    
    def test_validate_entry_date_invalid(self):
        entry_date_str = "32/09/23"
        result = self.score.validate_entry_date(entry_date_str)
        self.assertIsInstance(result, datetime)  
    
    def test_validate_score_valid(self):
        result = self.score.validate_score(9.5)
        self.assertEqual(result, 9.5)
    
    def test_validate_score_invalid(self):
        with self.assertRaises(ValueError):
            self.score.validate_score(11)  
    
    def test_update_score(self):
        self.score.update_score(8.0)
        self.assertEqual(self.score.score, 8.0)
    
    def test_display_info(self):
        self.score.display_info()  
    
if __name__ == "__main__":
    unittest.main()
