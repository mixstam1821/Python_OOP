from question_engine import question_engine
game = True
Game = question_engine()
question_number = 1
while(game):
    print(f"Q.{question_number}:{Game.createQuestion()}")
    player_answer = input("True/False?:")
    Game.checkAnswer(player_answer=player_answer)
    print(f"Your Score is: {Game.score}")
    question_number = question_number+1

