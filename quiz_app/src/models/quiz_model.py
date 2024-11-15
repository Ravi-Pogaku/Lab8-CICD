# src/models/quiz_model.py
from src.database import db

# RAVICHANDRA POGAKU, 100784105


class QuizModel(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    questions = db.Column(db.PickleType)

    def __init__(self, title, questions):
        self.title = title
        self.questions = questions

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_quiz(cls, quiz_id):
        return cls.query.get(quiz_id)
