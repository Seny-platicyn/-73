import random

def computer_progress():
    move = ['камень', 'ножницы', 'бумага']
    return random.choice(move)

def user_progress():
    user_choice = input('Какой ваш ход?(камень, ножницы, бумага) :').lower()
    while user_choice not in ['камень', 'ножницы', 'бумага']:
        print('Неверный ввод, попробуйте снова ')
        user_choice = input('Какой ваш ход?(камень, ножницы, бумага) :').lower()
    return user_choice
def winner(user_play, computer_play):
    if user_play == computer_play:
        return 'Ничья'
    elif (user_play == 'камень' and computer_play == 'ножницы') or \
         (user_play == 'ножницы' and computer_play == 'бумага') or \
         (user_play == 'бумага' and computer_play == 'камень'):
        return 'Вы выиграли'
    else:
        return 'Компьютер выиграл!'

def play_game():
    user_play = user_progress()
    computer_play = computer_progress()
    print(f'Ваш выбор: {user_play}')
    print(f'Выбор компьютера: {computer_play}')

    result = winner(user_play, computer_play)
    print(result)

play_game()
