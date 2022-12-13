# This is just a simple quiz game that pulls questions from opentdb API.

from html import unescape
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    question_bank = []
    for item in question_data:
        question_bank.append(Question(unescape(item['question']), item['correct_answer']))
    quiz_brain = QuizBrain(question_bank)
    while quiz_brain.still_has_questions():
        total, num = quiz_brain.next_question()
    print(f"You've completed the quiz. "
          f"Your final score is: {total}/{num - 1}")

if __name__ == "__main__":
    main()
