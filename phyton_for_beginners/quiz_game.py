
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        questions = [
            {"prompt": "What does CPU stand for?\n(a) Central Processing Unit\n(b) Central Program Unit\n(c) Central Processor Unit\n\n", "answer": "a"},
            {"prompt": "What does GPU stand for?\n(a) Graphics Processing Unit\n(b) Graphics Program Unit\n(c) Graphics Processor Unit\n\n", "answer": "a"},
            {"prompt": "What does RAM stand for?\n(a) Random Access Memory\n(b) Random Allocation Memory\n(c) Random Access Memory\n\n", "answer": "a"},
            {"prompt": "What does PSU stand for?\n(a) Power Supply Unit\n(b) Power System Unit\n(c) Power Supply Unit\n\n", "answer": "a"}
        ]
    
    def check_answer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    
    def run_quiz(self):
        for question in self.questions:
            answer = input(question.prompt)
            if question.check_answer(answer):
                self.score += 1
        print(f"You got {self.score} / {len(self.questions)} correct")

class QuizGame:
    def __init__(self):
        self.questions = [
            Question("What does CPU stand for?\n(a) Central Processing Unit\n(b) Central Program Unit\n(c) Central Processor Unit\n\n", "a"),
            Question("What does GPU stand for?\n(a) Graphics Processing Unit\n(b) Graphics Program Unit\n(c) Graphics Processor Unit\n\n", "a"),
            Question("What does RAM stand for?\n(a) Random Access Memory\n(b) Random Allocation Memory\n(c) Random Access Memory\n\n", "a"),
            Question("What does PSU stand for?\n(a) Power Supply Unit\n(b) Power System Unit\n(c) Power Supply Unit\n\n", "a")
        ]
        self.quiz = Quiz(self.questions)
    
    def run(self):
        self.quiz.run_quiz()

q = QuizGame()
q.run()