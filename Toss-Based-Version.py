
board = ['#','X','O','X','O','X','O','X','O','X']

from IPython.display import clear_output

def view_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9]+'|')
    print(board[4]+'|'+board[5]+'|'+board[6]+'|')
    print(board[1]+'|'+board[2]+'|'+board[3]+'|')

def win_check(test_board, marker):
    return (
    test_board[1]==test_board[2]==test_board[3]==marker or
    test_board[4]==test_board[5]==test_board[6]==marker or
    test_board[7]==test_board[8]==test_board[9]==marker or

    test_board[1]==test_board[4]==test_board[7]==marker or
    test_board[2]==test_board[5]==test_board[8]==marker or
    test_board[3]==test_board[6]==test_board[9]==marker or

    test_board[1]==test_board[5]==test_board[9]==marker or
    test_board[3]==test_board[5]==test_board[7]==marker)

def intro():
    global k
    k=41
    print('.'*k*3)
    print(' '*k)
    print(' '*k)
    print('Welcome To Tic-Tac-Toe')
    print(' '*k)
    view_board(board)
    print(' '*k)
    print('Designed,')
    print('Developed,')
    print('   &')
    print('Deployed')
    print('         by J Jeevan Roy,')
    print(' '*k)
    print('.'*k*3)
    print(' '*k)
    print(' '*k)

intro()

def players_dont_wanna_play():
    print(' '*k)
    print('.'*k*3)
    print(' '*k)
    print('Thank you! Visit again:)'.upper())
    print(' '*k)
    print('.'*k*3)
    print(' '*k)

def initiation():
    global test_board
    test_board = [' ']*10
    ready=' '
    while ready!='y' and ready!='n':
        ready = input('Are you ready to play? y or n? :').lower()
        if ready=='y':
            ready_bool=True
        elif ready=='n':
            ready_bool=False

    if ready_bool:
        print(' '*k)
        print('The Only Instruction :The numberpad on the keyboard is considered as the 3 by 3 grid.')
        global player1
        print(' '*k)
        player1 = input('Player1 please enter your name: ')

        global player2
        print(' '*k)
        player2 = input('Player2 please enter your name: ')

        print(' '*k)
        print('{} Vs {}'.format(player1,player2))
        print(' '*k)
        print('player1 name:{}'.format(player1))
        print('player2 name:{}'.format(player2))
        return True
    else:
        players_dont_wanna_play()
        return False

def game_logic():
    if initiation():
        import random
        def toss_for_X_or_O():
            global toss_winner
            global toss_loser
            if random.randint(0,1)==0:
                toss_winner,toss_loser = player1,player2
            else:
                toss_winner,toss_loser = player2,player1
            print(' '*k)
            print("* Congragulations {}, you won the toss! *".format(toss_winner))
            print(' '*k)
            print(' '*k)
            print("* Wake up {}, you lost the toss! Doesn't mean you lost the game. Don't lose hope:) *".format(toss_loser))
            print(' '*k)
            return toss_winner

        player = toss_for_X_or_O()

        def marker_assigner(toss_winner):
            marker = ' '
            while True:
                marker = input('{}, choose your marker, X or O? :'.format(toss_winner)).upper()
                if marker=='X' or marker=='O':
                    break
                else:
                    print(' '*k)
                    print('{}, your choice is neither X nor O. Please, choose either X or O.'.format(player))
            return marker

        marker = marker_assigner(toss_winner)

        def marker_fliper(marker):
            if marker=='X':
                return 'O'
            else:
                return 'X'

        def player_fliper(player):
            if player==player1:
                print('     {}, your turn'.format(player2))
                return player2
            else:
                print('     {}, your turn'.format(player1))
                return player1

        def player_fliper_greetings(player):
            if player==player1:
                return player2
            else:
                return player1

        indices_list = list(range(1,10))
        position=0
        while True:# if win_check() returns True this loop will be broken
            while True:#if position is int and in indices_list then this loop will be broken
                position = input('{}, Choose your marker position (1-9): '.format(player))
                try:
                    position = int(position)
                    if position in indices_list:
                        break
                    else:
                        if position in range(1,10):
                            print(' '*k)
                            print('{}, position {} is occupied, choose another possible possible. '.format(player,position))
                        else:
                            print(' '*k)
                            print('{}, position {} is out of range, choose a position (1-9). '.format(player,position))
                except:
                    print(' '*k)
                    print('{}, {} is not an accepted position. Please choose a position (1-9). '.format(player,position))
            indices_list.pop(indices_list.index(position))
            test_board[position]=marker
            view_board(test_board)
            print(' '*k)
            if win_check(test_board,marker):
                print('.'*k)
                print(' '*k)
                print('Congragulations {}!. You Won.'.format(toss_winner))
                print(' '*k)
                print("{}, Loosing isn't always the end, sometimes it becomes the begining:)  -Joseph Duffy".format(player_fliper_greetings(toss_winner)))
                print(' '*k)
                print('.'*k)
                break
            marker = marker_fliper(marker)
            if len(indices_list)!=0:
                player = player_fliper(player)
            if len(indices_list)==0:
                break

        if not win_check(test_board,marker):
            print('.'*k)
            print(' '*k)
            print("*WELL PLAYED! NOBODY LOST:) It's a TIE Game.*")
            print(' '*k)
            print('.'*k)

        def play_again(): #returns True if you wanna play again
            one_more_game = ' '
            while one_more_game!='y' and one_more_game!='n':
                print(' '*k)
                one_more_game=input('Do you want to play again? :y or n? :').lower()
                if one_more_game=='y':
                    return True
                elif one_more_game=='n':
                    return False

        if play_again():
            game_logic()
        else:
            print(' '*k)
            print('.'*k)
            print(' '*k)
            print('  :)  '*10)
            print(' '*k)
            print('Thank you for playing! Visit again:)')
            print(' '*k)
            print('  :)  '*10)
            print(' '*k)
            print('.'*k)
            print(' '*k)

game_logic()
