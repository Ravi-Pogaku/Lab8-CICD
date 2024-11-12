# tests/test_quiz.py
from unittest.mock import patch, MagicMock
from src.services.quiz_service import QuizService

# RAVICHANDRA POGAKU, 100784105


# Test for creating a new quiz
@patch.object(QuizService, 'create_quiz')
def test_create_quiz(mock_create_quiz, client):
    mock_create_quiz.return_value = 1

    data = {'title': 'Sample Quiz',
            'questions': [{
                'text': 'What is 2+2?',
                'options': ['1', '2', '3', '4'],
                'answer': '4'
                }]
            }
    response = client.post('/api/quizzes', json=data)

    assert response.status_code == 201
    assert response.json['quiz_id'] == 1
    mock_create_quiz.assert_called_once()


# Test for retrieving a quiz by ID
@patch.object(QuizService, 'get_quiz')
def test_get_quiz(mock_get_quiz, client):
    mock_quiz = MagicMock()
    mock_quiz.title = 'Sample Quiz'
    mock_quiz.questions = [{
        'text': 'What is 2+2?',
        'options': ['1', '2', '3', '4'],
        'answer': '4'
        }]

    mock_get_quiz.return_value = mock_quiz

    response = client.get('/api/quizzes/1')

    assert response.status_code == 200
    assert response.json['title'] == 'Sample Quiz'
    mock_get_quiz.assert_called_once()


# Test for submitting answers and evaluating a quiz
@patch.object(QuizService, 'evaluate_quiz')
def test_submit_quiz(mock_evaluate_quiz, client):
    mock_evaluate_quiz.return_value = (1, "Quiz evaluated successfully")

    data = {'answers': ['2']}
    response = client.post('/api/quizzes/1/submit', json=data)

    assert response.status_code == 200
    assert response.json['score'] == 1
    assert response.json['message'] == "Quiz evaluated successfully"
    mock_evaluate_quiz.assert_called_once()
