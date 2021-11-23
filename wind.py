number_of_sticks = 20
player = 0
game_over = False
def print_wind(n):
    print(('_____' + '   ')* n)
    for _ in range(10):
        print(('|   |' + '   ')* n)
    print(((chr(8254) * 5) + '   ')* n)

def can_take(taken):
    return taken >= 1 and taken <= 3 

print_wind(number_of_sticks)

while not game_over:
    p = player % 2 + 1
    print(f'Ходит игрок {p}. Выберите от 1 до 3 число')
    player += 1 
    taken = int(input())
    if can_take(taken):
        number_of_sticks -= taken 
        print_wind(number_of_sticks)
    else:
        print(f'вы взяли слишком много....или мало:) нужно от 1 до 3, а не {taken}')

    if number_of_sticks <= 0:
        game_over = True
        if player % 2 == 0:
            print('Игрок 1 победил')
        else:
            print('Игрок 2 победил')
