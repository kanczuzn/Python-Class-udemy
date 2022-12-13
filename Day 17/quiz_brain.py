import random

class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 1
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        rand_num = self.rand_question()
        curr_q = self.q_list[rand_num]
        user_ans = input(f"Q.{self.q_num}: {curr_q.text} (True/False) ")
        self.check_answer(user_ans, curr_q.answer)
        self.q_list[rand_num] = ""
        self.q_num += 1
        return self.score, self.q_num

    def still_has_questions(self):
        return self.q_num < 11

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower().strip() == correct_answer.lower():
            self.score += 1
        print(f"The correct answer is: {correct_answer}"
              f"\nYour current score is: {self.score}/{self.q_num}\n\n")

    def rand_question(self):
        max = len(self.q_list) - 1
        choose = True
        while choose:
            rand_num = random.randint(0, max)
            if self.q_list[rand_num] != "":
                choose = False
        return rand_num
