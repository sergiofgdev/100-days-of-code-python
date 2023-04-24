# class User:
#
#     # pass #Nos permite continuar con el codigo si no hemos escrito nada
#
#     # Funcion init es la funcion que inicializa una clase, va a ser llamada cada vez que se crea un objeto de esta clase
#     # Self hace referencia al objeto que esta siendo creado o inicializado
#     def __init__(self, user_id, username):
#         self.user_id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
# # Cada vez que creo ub objeto de esta clase se inicia el constructor (def __init__)
#
#
# user_1 = User("001", "Sergio")  # Los () inicializan el objeto
# user_2 = User ("002", "Oscar")


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)

# Inicializamos quiz_brain

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
