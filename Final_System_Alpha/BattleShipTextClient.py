from GameClient import *

class BattleShipTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [x[:] for x in [[' ']*6]*6] # creates 6x6 game board
        self.role = None # role C (for captain) or G (for general)
        self.capScore = 0
        self.genScore = 0
        
    def clear_board(self):
        self.board = [x[:] for x in [[' ']*6]*6]
        # I added these so that both the score variables are cleared
        self.capScore = 0
        self.genScore = 0  
        #This method also removes the role of both the players
        self.role = None
        
    def input_server(self):
        return input('enter server:')
     
    def input_move(self):
        return input('enter move(0-5,0-5):')
     
    def input_play_again(self):
        return input('play again(y/n):')

    def display_board(self):
        # remove the 'pass' statement and implement this method
        #populating the board
        print()
        print(" __ __"*7+"_")
        for i in range(6):
            print("|",end = " ")
            for k in range(6):
                if k<6:  
                    print("{:>3}   |".format(self.board[i][k]),end = "")
                    if k == 5 and i<6:
                        print()
                    
            
            print(" __ __"*7+"_")    
        print()
        #print()
    
    def handle_message(self,msg):
        """
           #your move
           Whenever it is your move, the player is informed that it is their move
           and then asked to enter the move of their choice by the method --> input_move().
           The message is then sent
           to the sever by the method self.send_message(move)
           
           #your opponents move
           In this case the user is informed that the move is not theirs, so they should wait....!
           There is no point where in which the player is granted permission to play while it's not their turn to play.
           
           #valid move
           The valid move method checks the validity of the message received from the sever, and so when valid, 
           the board is then populated with the appropriate message at each block(represented by row and column).
           
           #invalid move
           If the move is then invalid, the player is informed that the move is invalid and then asked to play again.
           
           #game over
           
           When the game is over, then both players receive the scores(captain and general) and who won the game.
           The game is over when there are no more moves on the board...(all the ships have been sank).
           
           #play again
           after the game is over, both players are asked if they want to play a new game..(yes/no)
           
           #exit
           if a plyer chooses not to start a new game then both players receive a message "press enter to exit"
           """       
        
        # handling message by spliting where there is a comma to get access
        #to all components od the game at each time the message is received from the server
        msg =msg.split(",")
        
        #new game
        #new Game is handled in such a way that whenever the roles are equal to None
        #Then we know that the game is new and no player has been assingned a role,
        # then we are able to assign a role and then print to the screen of each player
        # that it is the new game and then inform each player of their role.
        if self.role == None:
            self.role = msg[-1]
            #print(self.role)
            print(msg[0])
            if msg[1] == "C":
                print("You are the Captain of the ship!"+"\n")
            else:
                print("You are the General of the ship!"+"\n")
            
            self.display_board()
       
            
       #Here when ever now that the roles of the players are not equal to none,
       # since we have assigned roles to each player above, the we know that the game is still continuing
       # and all of the messages will then enter here because the code above will not assesss the message since
       # the condition is not met
       
   
       
       
        else:
           
            if msg[0] == "your move":
                
                print("It's {}.".format(msg[0]))
                self.send_message(self.input_move())
               
                
            elif msg[0]=="opponents move":
                print("It' your {}. Please wait!\n".format(msg[0]))
                
            
            elif msg[0] == "invalid move":
                print("{}! Please try again.".format(msg[0]))
                
            elif msg[0] == "valid move":
                
                if msg[1] == "C" and int(msg[4])> self.capScore:
                    
                    self.board[int(msg[2])][int(msg[3])] = msg[1]
                    self.capScore = int(msg[4])
                    self.display_board()
                    
                    
                elif msg[1] == "C" and int(msg[4])==self.capScore:
                    self.board[int(msg[2])][int(msg[3])] = (msg[1]).lower()
                    self.display_board()
                    
                    
                    
                elif msg[1] == "G" and int(msg[5]) > self.genScore:
                    self.board[int(msg[2])][int(msg[3])] = msg[1]
                    self.genScore = int(msg[5])
                    self.display_board()  
                    
                    
                elif msg[1] == "G" and int(msg[5])== self.genScore:
                    
                    self.board[int(msg[2])][int(msg[3])] = (msg[1]).lower()
                    self.display_board() 
                    
                    
            elif msg[0] =="play again":
               
                newGame = self.input_play_again()
                self.send_message(newGame)
                self.clear_board()
                    
                
            elif msg[0] == "game over":
                self.display_board()
                print(msg[0])
                print("Scores: General: {}; Captein: {}".format(self.genScore,self.capScore))
                if msg[-1]=="C":
                    print("The winner is {} with score: {}".format("the Captein",self.capScore))
                else:
                    print("The winner is {} with score: {}".format("the General",self.genScore))
                    
        
                
                
                
                
    
    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg): self.handle_message(msg)
            else: break
            
def main():
    bstc = BattleShipTextClient()
    while True:
        try:
            bstc.connect_to_server(bstc.input_server())
            break
        except:
            print('Error connecting to server!')
    bstc.play_loop()
    input('Press enter to exit.')
        
main()

