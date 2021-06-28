from random import shuffle, choice
from itertools import combinations_with_replacement as com

set = list([list(i) for i in com([i for i in range(7)], 2)])


def play():
    shuffle(set)
    global stock, computer, player, status
    stock = set[:14]
    computer = set[14:21]
    player = set[21:]

def display():
    print(70 * '=')
    print(f'Stock size: {len(stock)}')
    print(f'Computer pieces: {len(computer)}\n')
    if len(snake) <= 6:
        print(''.join([str(piece) for piece in snake]))
    else:
        temp = snake[:3] + ['...'] + snake[-3:]
        print(''.join([str(piece) for piece in temp]))
    print('\nYour pieces:')
    for piece in player:
        print(f'{player.index(piece) + 1}:{piece}')


    if player and computer and stock:
        move()
    else:
        if not stock:
            print("\nStatus: The game is over. It's a draw!")
        elif not player:
            print('\nStatus: The game is over. You won!')
        elif not computer:
            print('\nStatus: The game is over. The computer won!')



def start():
    global snake, turn
    turn = ''
    snake = []
    if not snake:
        try:
            max_computer = [piece for piece in computer if piece[0] == piece[1]]
            max_player = [piece for piece in player if piece[0] == piece[1]]
        except:
            main()
        else:
            double = max(max_computer + max_player)
            snake.append(double)
            if double in computer:
                computer.remove(double)
                turn = 'player'
            else:
                player.remove(double)
                turn = 'computer'


def move():
    global turn, snake
    if turn == 'player':
        print("\nStatus: It's your turn to make a move. Enter your command.")
        valid()
        turn = 'computer'
        display()
    else:
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
        enter = input()
        if enter or enter == '':
            AI()
        turn = 'player'
        display()



def valid():
    while True:
        move = input()
        try:
            move = int(move)
            piece = player[abs(move) - 1]
        except:
            print('Invalid input. Please try again.')
        else:
            if move == 0 and stock:
                player.append(stock.pop())
                break
            elif move < 0 and snake[0][0] in piece:
                if piece[1] == snake[0][0]:
                    snake.insert(0, piece)
                else:
                    snake.insert(0, piece[::-1])
                player.remove(piece)
                break
            elif move > 0 and snake[-1][1] in piece:
                if piece[0] == snake[-1][1]:
                    snake.append(piece)
                else:
                    snake.append(piece[::-1])
                player.remove(piece)
                break
            else:
                print('Illegal move. Please try again.')



def AI():
    digits = [digit for piece in computer + snake for digit in piece]
    count = {digit: digits.count(digit) for digit in sorted(digits)}
    scores = {count[piece[0]] + count[piece[1]]: piece for piece in computer}
    while scores:
        piece = scores.pop(max(scores))
        if snake[0][0] in piece:
            if piece[1] == snake[0][0]:
                snake.insert(0, piece)
            else:
                snake.insert(0, piece[::-1])
            computer.remove(piece)
            break
        elif snake[-1][1] in piece:
            if piece[0] == snake[-1][1]:
                snake.append(piece)
            else:
                snake.append(piece[::-1])
            computer.remove(piece)
            break
    else:
        computer.append(stock.pop())


def main():
    play()
    start()
    display()

main()
