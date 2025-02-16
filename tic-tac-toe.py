import sys

#This is a tic tac toe. Player will alternatively choose O and X. 
#It has same rules as normal tic tac toe

# Initial value on the board so that it is easier to find the square 
square = ["1", "2", "3", "4", "5", "6","7","8","9"]

# Globally declaring player and turn so that they can be used in future functions
player = 1
turn = 1

#board() has 3*3 dimensions. It is the board where the game happens. As player choose 
#a square to input, the value will get updated from "1", "2"... to "O" or "X"
def board():
    print("  " + square[0]+"  |  " +square[1]+"  |  "+square[2]+"  ")
    print("-----|-----|-----")
    print("  " + square[3]+"  |  " +square[4]+"  |  "+square[5]+"  ")
    print("-----|-----|-----")
    print("  " + square[6]+"  |  " +square[7]+"  |  "+square[8]+"  ")


# This contains the conditions for winning
def compare():
    global player

    if square[0]==square[1] and square[1]==square[2] or square[0]==square[3] and square[3]==square[6]:
        print("Congratulations player no. " + str(player) + " for winning the game. \n")
        sys.exit(0)

    elif square[0]==square[4] and square[4]==square[8] or square[1]==square[4] and square[4]==square[7]:
        print("Congratulations player no. " + str(player) + " for winning the game. \n")
        sys.exit(0)

    elif [2]==square[5] and square[5]==square[8] or square[3]==square[4] and square[4]==square[5]:
        print("Congratulations player no. " + str(player) + " for winning the game. \n")
        sys.exit(0)

    elif square[6]==square[7] and square[7]==square[8] or square[2]==square[4] and square[4]==square[6]:
        print("Congratulations player no. " + str(player) + " for winning the game. \n")
        sys.exit(0)


#The function which controls the flow of game
def game():

    #Re declaring turn and player as global variables so the initial values of them can be used
    global turn
    global player

    # This ensures that total of 9 turns are played by players 
    while turn<10:
    

        #Try and except are used to ensure that no players input any strings or signs
        try:
            #Taking input from players and ensuring that they are integer
            n = int(input("Player no. " +str(player)+". Select a square: "))

            #Creating a new variable which holds the string version fo the player input
            #This is needed to compare it with the values of square[] later
            user_input = str(n)
     

        except:
            board()
            print("Invalid input. Try again\n")
            game()     
            
        
        #To ensure that the square selected by player has not already been selecte before
        #Or the player has not choosen number bigger than 9 or less than 1
        if square[n-1] == user_input:
            #In each run, the turn is increased
            turn=turn+1
            #Alternating between player 1 and player 2. Player 1 has "O" and player 2 has "X"    
            if player==1:
                square[n-1] = "O"
                board()
                compare()
                player =2
            else:
                square[n-1] = "X"
                board()
                compare()
                player=1
    
            game()
        else:
            print("Invalid input. Try again\n")
            game()
    

#Initial representation for board   
board()
# Actual game taking place      
game()         

