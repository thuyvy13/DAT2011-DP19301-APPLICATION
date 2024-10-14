import datetime


# --- Model class ---
class ScoreModel:
    """
    @author: Do Thuy Vy
    Model lưu trữ thông tin điểm sinh viên.
    Gồm các phương thức getter và setter.
    """
    def __init__(self, term, student_id, subject, score, date=None):
        self.term = term
        self.student_id = student_id
        self.subject = subject
        self.score = score
        self.date = date or datetime.datetime.now().strftime("%d/%m/%Y")

    def get_term(self):
        return self.term

    def set_term(self, term):
        self.term = term

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, student_id):
        self.student_id = student_id

    def get_subject(self):
        return self.subject

    def set_subject(self, subject):
        self.subject = subject

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date