
class Bingo:
    count = 0
    isWinner = False

    def __init__(self, board: []):
        self.board = board

    def get_score(self, winning_number):
        score = 0
        for item in self.board:
            if False in list(item.values()): score += list(item)[0]

        return score * winning_number


def check_for_winner(bingo):
    if bingo.count < 5: return None
    if check_rows(bingo.board) or check_columns(bingo.board): return bingo


def check_rows(board):
    for i in range(0, len(board), 5):
        count = 0
        for j in range(5):
            if True in list(board[i + j].values()): count += 1
        if count == 5: return True

    return False


def check_columns(board):
    for i in range(5):
        count = 0
        for j in range(0, len(board), 5):
            if True in list(board[i + j].values()): count += 1
        if count == 5: return True

    return False


with open('data/bingo.txt') as file:
    lines = file.readlines()

    numbers_drawn = lines[0].split(',')
    numbers_drawn = [int(item) for item in numbers_drawn]
    all_boards = []

    for i in range(2, len(lines), 6):
        b = Bingo([])
        for j in range(5):
            line = lines[i + j].split()
            for k in range(len(line)):
                b.board.append({int(line[k]): False})
        all_boards.append(b)

    bingo = None
    last_bingo = None
    # winning_number = 0
    last_winning_number = 0
    winners = 0

    for number in numbers_drawn:
        # if bingo is not None: break
        if last_winning_number != 0: break

        for this_board in all_boards:
            if bingo is not None or this_board.isWinner: continue

            for index, value in enumerate(this_board.board):
                key = list(value)[0]

                if key == number:
                    this_board.board[index] = {key: True}
                    this_board.count += 1
                bingo = check_for_winner(this_board)

                if bingo is not None:
                    print('winner! ' + str(list(bingo.board[0])[0]))
                    winners += 1
                    bingo.isWinner = True

                    if winners == len(all_boards):
                        last_winning_number = number
                        last_bingo = bingo
                        break
                    break
            bingo = None
                    # winning_number = number
                    # break

    print(last_bingo.get_score(last_winning_number))
