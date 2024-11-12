# src/services/quiz_service.py
from src.models.quiz_model import QuizModel

# RAVICHANDRA POGAKU, 100784105


class QuizService:
    def create_quiz(self, quiz_data):
        title = quiz_data.get('title')
        questions = quiz_data.get('questions')

        quiz = QuizModel(title, questions)

        quiz.save()
        return quiz.id

    def get_quiz(self, quiz_id):
        quiz = QuizModel.get_quiz(quiz_id)

        return quiz

    def evaluate_quiz(self, quiz_id, user_answers):
        quiz = self.get_quiz(quiz_id)

        if not quiz:
            return None, 'Quiz not found'

        score = sum(
            [1 for i in range(len(quiz.questions))
             if quiz.questions[i]['answer'] == user_answers[i]])

        return score, 'Quiz evaluated'
