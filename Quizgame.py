# quiz_game.py

class Question:
    
    def __init__(self, text, options, answer):
        self.text    = text     
        self.options = options  
        self.answer  = answer   
    
    def check(self, user_input):
        return user_input == self.answer  


class Quiz:
    
    def __init__(self, name):
        self.name      = name  
        self.score     = 0     
        self.questions = []    
    
    def add_question(self, q):
        self.questions.append(q)
    
    def start(self):
        print(f"\n Welcome {self.name}! Quiz is starting!\n")
        
        for i, q in enumerate(self.questions, 1):
            print(f"Q{i}: {q.text}")
            for j, opt in enumerate(q.options, 1):
                print(f"  {j}. {opt}")
            
            answer = int(input("Your answer (1-4): "))
            
            if q.check(answer):
                print(" Correct!\n")
                self.score += 1
            else:
                print(f" Wrong! Correct answer was: {q.answer}\n")
        
        print(f"🏆 {self.name}'s final score: {self.score}/{len(self.questions)}")


name = input("Enter your name: ")
quiz = Quiz(name)

quiz.add_question(Question(
    "What is the capital of France?",
    ["London", "Berlin", "Paris", "Rome"], 3))

quiz.add_question(Question(
    "What does OOP stand for?",
    ["Object Oriented Programming", "Open Office Protocol",
     "Output Operations Pending", "None of these"], 1))

quiz.add_question(Question(
    "Which symbol is used for a list in Python?",
    ["{ }", "( )", "[ ]", "< >"], 3))

quiz.add_question(Question(
    "What is 5 * 5?",
    ["20", "25", "30", "15"], 2))

quiz.start()