def create_matrix(n):
    matrix = []
    for _ in range(n):
        row = list(input())
        matrix.append(row)
    return matrix


def find_the_snake(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'S':
                return row, col


def burrow_pass(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'B':
                return row, col


def make_move(matrix, vertical_move, horizontal_move):
    global food_eaten

    s_row, s_col = find_the_snake(matrix)
    matrix[s_row][s_col] = '.'

    if s_row + vertical_move in range(len(matrix)) \
            and s_col + horizontal_move in range(len(matrix[s_row])):

        s_row += vertical_move
        s_col += horizontal_move

        if matrix[s_row][s_col] == '-':
            matrix[s_row][s_col] = 'S'

        elif matrix[s_row][s_col] == '*':
            food_eaten += 1
            matrix[s_row][s_col] = 'S'
            if food_eaten >= 10:
                return 'You won'

        else:
            matrix[s_row][s_col] = '.'
            b_row, b_col = burrow_pass(matrix)
            matrix[b_row][b_col] = 'S'
    else:
        return 'Game over'


def print_matrix(matrix):
    for row in range(len(matrix)):
        print(''.join(matrix[row]))
    return


def printing_result(value, matrix):
    if value:
        print(f'You won! You fed the snake.\nFood eaten: {food_eaten}')
        print_matrix(matrix)
    else:
        print(f'Game over!\nFood eaten: {food_eaten}')
        print_matrix(matrix)


def play(matrix):
    while True:
        move = input()
        if move == 'up':
            move_result = make_move(matrix, -1, 0)

        elif move == 'down':
            move_result = make_move(matrix, +1, 0)

        elif move == 'left':
            move_result = make_move(matrix, 0, -1)

        else:
            move_result = make_move(matrix, 0, +1)

        if move_result == 'You won':
            printing_result(True, matrix)
            break
        elif move_result == 'Game over':
            printing_result(False, matrix)
            break


rows_count = int(input())
board = create_matrix(rows_count)
food_eaten = 0
play(board)
