class BingoBoard:
    def __init__(self, board:list[list[int]], numbers: list[int]):
        self.board = board
        self.numbers = numbers
    
    @property
    def win(self) -> bool:
        for row in self.board:
            if all( (i in self.numbers) for i in row ):
                return True
        for row_i in range(len(self.board)):
            if all( (self.board[col_i][row_i] in self.numbers) for col_i in range(len(self.board[row_i])) ):
                return True
        return False
    
    @property
    def unused_numbers(self) -> list[int]:
        return [ num for row in self.board for num in row if num not in self.numbers ]


def preprocess(data: str, numbers: str) -> tuple[list[BingoBoard], list[int]]:
    raw_data: list[str] = data.split('\n')
    raw_numbers = [int(num) for num in raw_data.pop(0).split(',')]
    raw_data.pop(0)
    boards = []
    board_data = []
    for line in raw_data:
        if line == '':
            continue
        board_data.append([int(number) for number in line.split()])
        if len(board_data) == 5:
            boards.append(BingoBoard(board_data, numbers))
            board_data = []
    return boards, raw_numbers

def process(boards: list[BingoBoard], numbers: list[int], unused_numbers: list[int]) -> int:
    win_board = None
    win_number = None
    for num in unused_numbers:
        numbers.append(num)
        if all(board.win for board in boards):
            win_number = num
            numbers.pop()
            win_board = (board for board in boards if not board.win).send(None)
            break
    print('Winning Number:', win_number)
    print('Sum of Unused Numbers:', s := (sum(win_board.unused_numbers) - win_number))
    print('Result:', result := (s * win_number))
    return result


if __name__ == '__main__':
    numbers = []
    with open('.\\Input-1.txt', 'r') as f:
        inp = f.read()
    boards, unused_numbers = preprocess(inp, numbers)
    process(boards, numbers, unused_numbers)
