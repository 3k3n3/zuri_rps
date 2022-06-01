import random

print ('Welcome to ROCK-PAPER-SCISSSORS!')

#players
Player1 = 'CPU' #computer
Player2 = input("What's your name?\n")

#moves
R = 'rock'
P = 'paper'
S = 'scissors'

moves = [R, P, S] #add variables to a list

#funtion for gameplay
def gameplay():
    Player1_move = random.choice(moves)
    Player2_move = input('Pick an option\n"R" = rock, "P" = paper, "S" = scissors\n')
    Player2_move = Player2_move.upper() #convert all entered strings to uppercase to make entries uniform

    #funtion to simply print out player name and their selection
    def scoreboard():
        score = print('%s (%s) : %s (%s)' %(Player2, Player2_move, Player1, Player1_move))

    if Player2_move == 'R':
        Player2_move = R
        scoreboard()

        if Player1_move == R:
            print('Draw! Play Again')
            gameplay()
        elif Player1_move == P:
            print(Player1, 'Wins!')
        else: #there is only one move left, ie. cpu plays S in this case
            print(Player2, 'Wins!')

    elif Player2_move == 'P':
        Player2_move = P
        scoreboard()

        if Player1_move == P:
            print('Draw! Play Again')
            gameplay()
        elif Player1_move == S:
            print(Player1, 'Wins!')
        else:
            print(Player2, 'Wins!')

    elif Player2_move =='S':
        Player2_move = S
        scoreboard()

        if Player1_move == S:
            print('Draw! Play Again')
            gameplay()
        elif Player1_move == P:
            print(Player2, 'Wins!')
        else:
            print(Player1, 'Wins!')

    #Returns error if any other value besides R, P or S is entered
    else:
        print("Error!")
        gameplay()

gameplay()