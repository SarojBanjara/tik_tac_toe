def main():
    print('\n\t\t\t\t Welcome to Tik Tak Toe')
    board = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-', ]

    def show(board):
        print('\n\t\t\t\t\t', board[0] + "\t|\t" + board[1] + "\t|\t" + board[2])
        print('\t\t\t\t\t', board[3] + "\t|\t" + board[4] + "\t|\t" + board[5])
        print('\t\t\t\t\t', board[6] + "\t|\t" + board[7] + "\t|\t" + board[8])

    show(board)

    def win_check(board):
        global winner, choice
        winner = False
        row_1 = board[0] == board[1] == board[2] != '-'
        row_2 = board[3] == board[4] == board[5] != "-"
        row_3 = board[6] == board[7] == board[8] != "-"
        column_1 = board[0] == board[3] == board[6] != '-'
        column_2 = board[1] == board[4] == board[7] != "-"
        column_3 = board[2] == board[5] == board[8] != "-"
        diagonal_1 = board[0] == board[4] == board[8] != "-"
        diagonal_2 = board[2] == board[4] == board[6] != "-"

        if row_1 or row_2 or row_3 or column_1 or column_2 or column_3 or diagonal_1 or diagonal_2:  # return the winner
            winner = True
            if row_1 or column_1 or diagonal_1:
                show(board)
                print('\n\t\t\t', board[0], "'s won")
                question = input("\n\t\t\t\tDo you want to play again? If YES, press 'Y' else press 'Enter'")
                if question == 'Y':
                    main()
                else:
                    exit()
            elif row_2 or column_2 or diagonal_2:
                show(board)
                print('\n\t\t\t\t', board[4], "'s won")
                question = input("\n\t\t\t\tDo you want to play again? If YES, press 'Y' else press 'Enter'")
                if question == 'Y':
                    main()
                else:
                    exit()
            elif row_3 or column_3:
                show(board)
                print('\n\t\t\t\t', board[8], "'s won")
                question = input("\n\t\t\t\tDo you want to play again? If YES, press 'Y' else press 'Enter'")
                if question == 'Y':
                    main()
                else:
                    exit()
            elif '-' not in board:
                print('\n\t\t\t\tTIE')

        else:
            return None

    def choose_player(board):
        global valid_move
        valid_move = False
        select = input('\n\t\t\t\tPlease select a number in between 1 - 9 to make a move.  ')
        if select in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            select = int(select) - 1
            if board[select] == '-':
                board[select] = choice
                valid_move = True
            else:
                print('\n\t\t\t\tThe position is already taken!')
                return choose_player(board)
        else:
            print('\n\t\t\t\tInvalid entry.')
            choose_player(board)
        return win_check(board)

    import random
    def choose_computer(board):
        valid_move = False
        while not valid_move:
            random.seed()
            select = random.randint(0, 8)
            if board[select] == '-':
                if choice == 'X':
                    board[select] = 'O'
                elif choice == 'O':
                    board[select] = 'X'
                print('\n\t\t\t\tComputer made a move @ position', select + 1)
                valid_move = True

        return win_check(board)

    player = False
    turn = 0
    try:
        while True:
            choice = input("\n\t\t\t\tDo you want to start with 'X' or 'O'? ")
            if choice in ['X', 'O']:
                if choice == 'X':
                    print("\n\t\t\t\tYou are 'X' and Computer is 'O'.")
                elif choice == 'O':
                    print("\n\t\t\t\tYou are 'O' and Computer is 'X'.")
                break
    except:
        print('\n\t\t\t\tPlease enter X or O')

    # for turn
    while not player and turn < 9:
        if choice == 'X' or choice == 'O':
            if turn % 2 == 0:
                choose_player(board)
            else:
                choose_computer(board)
            turn = turn + 1
            show(board)

    def check_for_tie():
        global winner
        if '-' not in board:
            winner = True
            return True
        else:
            return False

main()