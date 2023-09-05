DIM = 3

def tic_tac_win(game: list) -> bool:
    for r in range(DIM):
        symbols = []
        for c in range(DIM):
            symbols.append(game[r][c])
        if check_symbols(symbols):
            return True

    for c in range(DIM):
        symbols = []
        for r in range(DIM):
            symbols.append(game[r][c])
        if check_symbols(symbols):
            return True
    
    symbols1 = []
    symbols2 = []
    for r in range(DIM):
        symbols1.append(game[r][r])
        symbols2.append(game[r][DIM-r-1])
    if check_symbols(symbols1) or check_symbols(symbols2):
            return True
    
    return False

def check_symbols(symbols):
    return symbols[0] is not None and symbols.count(symbols[0]) == DIM

if __name__ == '__main__':
    test_game = [['x', 'o', 'x'],
                 ['o', 'x', 'o'],
                 [None, 'o', 'o']]
    print(tic_tac_win(test_game))