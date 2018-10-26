import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import*
from GameLoop import *

class GuiClient(QtGui.QWidget):
    def __init__(self, parent=None):
        super(GuiClient, self).__init__(parent)
        self.setWindowTitle('BattleShipGame')
        self.setFixedSize(800,800)
        
        mainGrid = QtGui.QGridLayout()
        self.buttonGrid = QtGui.QGridLayout()
    
        
        self.palette = QtGui.QPalette()
        self.palette.setBrush(QtGui.QPalette.Background,QBrush(QPixmap("b.png")))
        self.setPalette(self.palette)
        
        
         # creating variables
        self.ipAdress = ""
        self.received_message = ""
        self.myMessageServer = ""
        self.clickedButton = ''
        self.allButtons = {}
        
    
        # Creating text edits
        self.msg_edit = QtGui.QTextEdit()
        self.role_edit = QtGui.QTextEdit()
        self.score_edit = QtGui.QTextEdit()
        
        
        #Creating Buttons
        self.new_game = QtGui.QPushButton("new Game")
        self.exit = QtGui.QPushButton("exit")   
       
        #
        self.button_0_0 = QtGui.QPushButton()
        self.button_0_0 .setStyleSheet("background-color: cyan")
        self.button_0_0.setFixedSize(70,70)
        self.button_0_0.setObjectName('0,0')
        self.button_0_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_0,0,0)
        self.allButtons[self.button_0_0] = '0,0'
        self.button_0_1 = QtGui.QPushButton()
        self.button_0_1.setFixedSize(70,70)
        self.button_0_1 .setStyleSheet("background-color: cyan")
        self.button_0_1.setObjectName('0,1')
        self.button_0_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_1,0,1)
        self.allButtons[self.button_0_1] = '0,1'
        self.button_0_2 = QtGui.QPushButton()
        self.button_0_2 .setStyleSheet("background-color: cyan")
        self.button_0_2.setFixedSize(70,70)
        self.button_0_2.setObjectName('0,2')
        self.button_0_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_2,0,2)
        self.allButtons[self.button_0_2] = '0,2'
        self.button_0_3 = QtGui.QPushButton()
        self.button_0_3 .setStyleSheet("background-color: cyan")
        self.button_0_3.setFixedSize(70,70)
        self.button_0_3.setObjectName('0,3')
        self.button_0_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_3,0,3)
        self.allButtons[self.button_0_3] = '0,3'
        self.button_0_4 = QtGui.QPushButton()
        self.button_0_4 .setStyleSheet("background-color: cyan")
        self.button_0_4.setFixedSize(70,70)
        self.button_0_4.setObjectName('0,4')
        self.button_0_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_4,0,4)
        self.allButtons[self.button_0_4] = '0,4'
        self.button_0_5 = QtGui.QPushButton()
        self.button_0_5 .setStyleSheet("background-color: cyan")
        self.button_0_5.setFixedSize(70,70)
        self.button_0_5.setObjectName('0,5')
        self.button_0_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_5,0,5)
        self.allButtons[self.button_0_5] = '0,5'
        self.button_1_0 = QtGui.QPushButton()
        self.button_1_0 .setStyleSheet("background-color: cyan")
        self.button_1_0.setFixedSize(70,70)
        self.button_1_0.setObjectName('1,0')
        self.button_1_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_0,1,0)
        self.allButtons[self.button_1_0] = '1,0'
        self.button_1_1 = QtGui.QPushButton()
        self.button_1_1 .setStyleSheet("background-color: cyan")
        self.button_1_1.setFixedSize(70,70)
        self.button_1_1.setObjectName('1,1')
        self.button_1_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_1,1,1)
        self.allButtons[self.button_1_1] = '1,1'
        self.button_1_2 = QtGui.QPushButton()
        self.button_1_2 .setStyleSheet("background-color: cyan")
        self.button_1_2.setFixedSize(70,70)
        self.button_1_2.setObjectName('1,2')
        self.button_1_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_2,1,2)
        self.allButtons[self.button_1_2] = '1,2'
        self.button_1_3 = QtGui.QPushButton()
        self.button_1_3 .setStyleSheet("background-color: cyan")
        self.button_1_3.setFixedSize(70,70)
        self.button_1_3.setObjectName('1,3')
        self.button_1_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_3,1,3)
        self.allButtons[self.button_1_3] = '1,3'
        self.button_1_4 = QtGui.QPushButton()
        self.button_1_4 .setStyleSheet("background-color: cyan")
        self.button_1_4.setFixedSize(70,70)
        self.button_1_4.setObjectName('1,4')
        self.button_1_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_4,1,4)
        self.allButtons[self.button_1_4] = '1,4'
        self.button_1_5 = QtGui.QPushButton()
        self.button_1_5 .setStyleSheet("background-color: cyan")
        self.button_1_5.setFixedSize(70,70)
        self.button_1_5.setObjectName('1,5')
        self.button_1_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_5,1,5)
        self.allButtons[self.button_1_5] = '1,5'
        self.button_2_0 = QtGui.QPushButton()
        self.button_2_0 .setStyleSheet("background-color: cyan")
        self.button_2_0.setFixedSize(70,70)
        self.button_2_0.setObjectName('2,0')
        self.button_2_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_0,2,0)
        self.allButtons[self.button_2_0] = '2,0'
        self.button_2_1 = QtGui.QPushButton()
        self.button_2_1 .setStyleSheet("background-color: cyan")
        self.button_2_1.setFixedSize(70,70)
        self.button_2_1.setObjectName('2,1')
        self.button_2_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_1,2,1)
        self.allButtons[self.button_2_1] = '2,1'
        self.button_2_2 = QtGui.QPushButton()
        self.button_2_2 .setStyleSheet("background-color: cyan")
        self.button_2_2.setFixedSize(70,70)
        self.button_2_2.setObjectName('2,2')
        self.button_2_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_2,2,2)
        self.allButtons[self.button_2_2] = '2,2'
        self.button_2_3 = QtGui.QPushButton()
        self.button_2_3 .setStyleSheet("background-color: cyan")
        self.button_2_3.setFixedSize(70,70)
        self.button_2_3.setObjectName('2,3')
        self.button_2_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_3,2,3)
        self.allButtons[self.button_2_3] = '2,3'
        self.button_2_4 = QtGui.QPushButton()
        self.button_2_4 .setStyleSheet("background-color: cyan")
        self.button_2_4.setFixedSize(70,70)
        self.button_2_4.setObjectName('2,4')
        self.button_2_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_4,2,4)
        self.allButtons[self.button_2_4] = '2,4'
        self.button_2_5 = QtGui.QPushButton()
        self.button_2_5 .setStyleSheet("background-color: cyan")
        self.button_2_5.setFixedSize(70,70)
        self.button_2_5.setObjectName('2,5')
        self.button_2_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_5,2,5)
        self.allButtons[self.button_2_5] = '2,5'
        self.button_3_0 = QtGui.QPushButton()
        self.button_3_0 .setStyleSheet("background-color: cyan")
        self.button_3_0.setFixedSize(70,70)
        self.button_3_0.setObjectName('3,0')
        self.button_3_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_0,3,0)
        self.allButtons[self.button_3_0] = '3,0'
        self.button_3_1 = QtGui.QPushButton()
        self.button_3_1 .setStyleSheet("background-color: cyan")
        self.button_3_1.setFixedSize(70,70)
        self.button_3_1.setObjectName('3,1')
        self.button_3_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_1,3,1)
        self.allButtons[self.button_3_1] = '3,1'
        self.button_3_2 = QtGui.QPushButton()
        self.button_3_2 .setStyleSheet("background-color: cyan")
        self.button_3_2.setFixedSize(70,70)
        self.button_3_2.setObjectName('3,2')
        self.button_3_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_2,3,2)
        self.allButtons[self.button_3_2] = '3,2'
        self.button_3_3 = QtGui.QPushButton()
        self.button_3_3 .setStyleSheet("background-color: cyan")
        self.button_3_3.setFixedSize(70,70)
        self.button_3_3.setObjectName('3,3')
        self.button_3_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_3,3,3)
        self.allButtons[self.button_3_3] = '3,3'
        self.button_3_4 = QtGui.QPushButton()
        self.button_3_4 .setStyleSheet("background-color: cyan")
        self.button_3_4.setFixedSize(70,70)
        self.button_3_4.setObjectName('3,4')
        self.button_3_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_4,3,4)
        self.allButtons[self.button_3_4] = '3,4'
        self.button_3_5 = QtGui.QPushButton()
        self.button_3_5 .setStyleSheet("background-color: cyan")
        self.button_3_5.setFixedSize(70,70)
        self.button_3_5.setObjectName('3,5')
        self.button_3_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_5,3,5)
        self.allButtons[self.button_3_5] = '3,5'
        self.button_4_0 = QtGui.QPushButton()
        self.button_4_0 .setStyleSheet("background-color: cyan")
        self.button_4_0.setFixedSize(70,70)
        self.button_4_0.setObjectName('4,0')
        self.button_4_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_0,4,0)
        self.allButtons[self.button_4_0] = '4,0'
        self.button_4_1 = QtGui.QPushButton()
        self.button_4_1 .setStyleSheet("background-color: cyan")
        self.button_4_1.setFixedSize(70,70)
        self.button_4_1.setObjectName('4,1')
        self.button_4_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_1,4,1)
        self.allButtons[self.button_4_1] = '4,1'
        self.button_4_2 = QtGui.QPushButton()
        self.button_4_2 .setStyleSheet("background-color: cyan")
        self.button_4_2.setFixedSize(70,70)
        self.button_4_2.setObjectName('4,2')
        self.button_4_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_2,4,2)
        self.allButtons[self.button_4_2] = '4,2'
        self.button_4_3 = QtGui.QPushButton()
        self.button_4_3 .setStyleSheet("background-color: cyan")
        self.button_4_3.setFixedSize(70,70)
        self.button_4_3.setObjectName('4,3')
        self.button_4_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_3,4,3)
        self.allButtons[self.button_4_3] = '4,3'
        self.button_4_4 = QtGui.QPushButton()
        self.button_4_4 .setStyleSheet("background-color: cyan")
        self.button_4_4.setFixedSize(70,70)
        self.button_4_4.setObjectName('4,4')
        self.button_4_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_4,4,4)
        self.allButtons[self.button_4_4] = '4,4'
        self.button_4_5 = QtGui.QPushButton()
        self.button_4_5 .setStyleSheet("background-color: cyan")
        self.button_4_5.setFixedSize(70,70)
        self.button_4_5.setObjectName('4,5')
        self.button_4_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_5,4,5)
        self.allButtons[self.button_4_5] = '4,5'
        self.button_5_0 = QtGui.QPushButton()
        self.button_5_0 .setStyleSheet("background-color: cyan")
        self.button_5_0.setFixedSize(70,70)
        self.button_5_0.setObjectName('5,0')
        self.button_5_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_0,5,0)
        self.allButtons[self.button_5_0] = '5,0'
        self.button_5_1 = QtGui.QPushButton()
        self.button_5_1 .setStyleSheet("background-color: cyan")
        self.button_5_1.setFixedSize(70,70)
        self.button_5_1.setObjectName('5,1')
        self.button_5_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_1,5,1)
        self.allButtons[self.button_5_1] = '5,1'
        self.button_5_2 = QtGui.QPushButton()
        self.button_5_2 .setStyleSheet("background-color: cyan")
        self.button_5_2.setFixedSize(70,70)
        self.button_5_2.setObjectName('5,2')
        self.button_5_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_2,5,2)
        self.allButtons[self.button_5_2] = '5,2'
        self.button_5_3 = QtGui.QPushButton()
        self.button_5_3 .setStyleSheet("background-color: cyan")
        self.button_5_3.setFixedSize(70,70)
        self.button_5_3.setObjectName('5,3')
        self.button_5_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_3,5,3)
        self.allButtons[self.button_5_3] = '5,3'
        self.button_5_4 = QtGui.QPushButton()
        self.button_5_4 .setStyleSheet("background-color: cyan")
        self.button_5_4.setFixedSize(70,70)
        self.button_5_4.setObjectName('5,4')
        self.button_5_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_4,5,4)
        self.allButtons[self.button_5_4] = '5,4'
        self.button_5_5 = QtGui.QPushButton()
        self.button_5_5 .setStyleSheet("background-color: cyan")
        self.button_5_5.setFixedSize(70,70)
        self.button_5_5.setObjectName('5,5')
        self.button_5_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_5,5,5)
        self.allButtons[self.button_5_5] = '5,5'
        
        # scores (Captain and General)
        self.generalScore = 0
        self.captainScore = 0
        
        self.score_edit.setText('Captein Score: {}\nGeneralScore: {}'.format(self.captainScore,self.generalScore))
     
        #creating labels      
        label1 = QtGui.QLabel('Enter Server:',self)
        label1.setFont(QtGui.QFont('times',20))
        label2 = QtGui.QLabel('Role/Player:',self)
        label2.setFont(QtGui.QFont('times',20))
        label3 = QtGui.QLabel('Game:',self)
        label3.setFont(QtGui.QFont('times',20))
        self.label4 = QtGui.QLabel('Message from server:',self)
        self.label4.setFont(QtGui.QFont('times',18))
        label5 = QtGui.QLabel('Scores:',self) 
        label5.setFont(QtGui.QFont('times',20))
        #
        self.server = QtGui.QLineEdit()
        self.connected = QtGui.QPushButton("Connect")
             
        mainGrid.addWidget(self.server,0,2)
        mainGrid.addWidget(self.connected,0,3)
        mainGrid.addWidget(label1,0,1)
        mainGrid.addWidget(self.label4,8,0)
        mainGrid.addWidget(self.msg_edit,9,0,1,2)
        mainGrid.addWidget(label5,5,0)
        mainGrid.addWidget(self.score_edit,6,0,2,2)
        mainGrid.addWidget(label3,4,4)
        mainGrid.addWidget(label2,2,4)
        mainGrid.addWidget(self.role_edit,4,4,1,1)
        mainGrid.addLayout(self.buttonGrid,7,2,3,3)
        mainGrid.addWidget(self.new_game,11,0)
        mainGrid.addWidget(self.exit,11,1)        

        self.setLayout(mainGrid)                
        # Inserting buttons into the grid
        
        
        #self.box.setLayout(self.buttonGrid)
        self.myGameLoop = GameLoop()
        
        #Loop connections(receiving message from the client text in order to set label text in to the buttons)
       
        self.myGameLoop.updateButtonMessageSignal.connect(self.connectSlot)
        self.new_game.clicked.connect(self.newGameSlot)
        self.exit.clicked.connect(self.cancelbutton)
        #Actions when buttons clicked
        
        self.connected.clicked.connect(self.connect_clicked)
        self.serverMessage = ''
        
        #Defined functions for connecting    
    def connect_clicked(self):
        self.ipAdress = self.server.displayText()
        self.myGameLoop.receiveIPAdress(self.ipAdress)
        self.myGameLoop.start()
        
    def buttonNameSlot(self):
        self.clickedButton = self.sender()
        self.myGameLoop.senda_message(self.sender().objectName())
        
    # The LoopThreadSlot for buttons
    def connectSlot(self,ms):
        s = ms
        
        self.msg_edit.setText(str(s)+"\n")
        newMessage = ms.split(",")
        print(newMessage)
        #self.serverMessage = newMessage
        
        if newMessage[0] == "new game":
            self.myMessageServer += "{}".format(newMessage[0]+"\n")
            self.msg_edit.setText(self.myMessageServer)
            if newMessage[1]=="C":
                
                self.role_edit.setText(newMessage[1]+"---> Captain")
            else:
                self.role_edit.setText(newMessage[1]+"---> General")
        elif newMessage[0]== "your move":
            self.serverMessage = newMessage
            
            self.senderTurnButton = True
            self.turn = newMessage[0]
            print(newMessage[0])
            print("Time to play!")
            
        elif newMessage[0] == "opponents move":
            self.senderTurnButton = False
            self.turn = newMessage[0]
            print("Please wait for your turn")
            
        
            
        elif newMessage[0] == "valid move":
            print(newMessage[0])
            if newMessage[1] =="C":
                
                if newMessage[2] == '0':
                    if self.captainScore<int(newMessage[4]):
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_0_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_0_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_0_2.setText(newMessage[1])
                        elif newMessage[3] == '3':
                            self.button_0_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_0_4.setText(newMessage[1])
                        elif newMessage[3] == '5':
                            self.button_0_5.setText(newMessage[1])
                            
                    else:
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_0_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_0_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_0_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_0_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_0_4.setText(newMessage[1].lower())
                        elif newMessage[3] == '5':
                            self.button_0_5.setText(newMessage[1].lower())                        
                            
                            
                elif newMessage[2] == '1':
                    if self.captainScore<int(newMessage[4]):
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_1_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_1_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_1_2.setText(newMessage[1])
                        elif newMessage[3] == '3':
                            self.button_1_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_1_4.setText(newMessage[1])
                        elif newMessage[3] == '5':
                            self.button_1_5.setText(newMessage[1])
                    else:
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_1_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_1_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_1_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_1_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_1_4.setText(newMessage[1].lower())
                        elif newMessage[3] == '5':
                            self.button_1_5.setText(newMessage[1].lower())                        

                            
                            
                elif newMessage[2] == '2':
                    if self.captainScore<int(newMessage[4]):
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_2_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_2_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_2_2.setText(newMessage[1])
                        elif newMessage[3] == '3':
                            self.button_2_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_2_4.setText(newMessage[1])
                        elif newMessage[3] == '5':
                            self.button_2_5.setText(newMessage[1])
                            
                    else:
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_2_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_2_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_2_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_2_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_2_4.setText(newMessage[1].lower())
                        elif newMessage[3] == '5':
                            self.button_2_5.setText(newMessage[1].lower())                        
                            
                elif newMessage[2] == '3':
                    if self.captainScore<int(newMessage[4]):
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_3_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_3_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_3_2.setText(newMessage[1])
                        elif newMessage[3] == '3':
                            self.button_3_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_3_4.setText(newMessage[1])
                        elif newMessage[3] == '5':
                            self.button_3_5.setText(newMessage[1])
                                                                  
                    else:
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_3_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_3_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_3_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_3_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_3_4.setText(newMessage[1].lower())
                        elif newMessage[3] == '5':
                            self.button_3_5.setText(newMessage[1].lower())                        
                        
                elif newMessage[2] == '4':
                    if self.captainScore<int(newMessage[4]):
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_4_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_4_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_4_2.setText(newMessage[1])
                        elif newMessage[3] == '3':
                            self.button_4_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_4_4.setText(newMessage[1])
                            
                    else:
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_4_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_4_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_4_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_4_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_4_4.setText(newMessage[1].lower())                            
                        elif newMessage[3] == '5':
                            self.button_4_5.setText(newMessage[1].lower())
                                                                
                elif newMessage[2] == '5':
                    if self.captainScore<int(newMessage[4]):
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_5_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_5_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_5_2.setText(newMessage[1])
                        elif newMessage[3] == '3':
                            self.button_5_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_5_4.setText(newMessage[1])
                        elif newMessage[3] == '5':
                            self.button_5_5.setText(newMessage[1])
                    else:
                        self.captainScore = int(newMessage[4])
                        if newMessage[3] == '0':
                            self.button_5_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_5_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_5_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_5_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_5_4.setText(newMessage[1].lower())
                        elif newMessage[3] == '5':
                            self.button_5_5.setText(newMessage[1].lower())                        
                              
            else:
                
                if newMessage[2] == '0':
                    if self.generalScore<int(newMessage[5]):
                        self.generalScore = int(newMessage[5])
                        if newMessage[3] == '0':
                            self.button_0_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_0_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_0_2.setText(newMessage[1])
                        elif newMessage[3] == '3':
                            self.button_0_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_0_4.setText(newMessage[1])
                        elif newMessage[3] == '5':
                            self.button_0_5.setText(newMessage[1])
                            
                    else:
                        self.generalScore = int(newMessage[5])
                        if newMessage[3] == '0':
                            self.button_0_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_0_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_0_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_0_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_0_4.setText(newMessage[1].lower())
                        elif newMessage[3] == '5':
                            self.button_0_5.setText(newMessage[1].lower())                        
                            
                            
                elif newMessage[2] == '1':
                    if self.generalScore <int(newMessage[5]):
                        self.generalScore = int(newMessage[5])
                        if newMessage[3] == '0':
                            self.button_1_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_1_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_1_2.setText(newMessage[1])
                        elif int(newMessage[4]) == '3':
                            self.button_1_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_1_4.setText(newMessage[1])
                        elif newMessage[3] == '5':
                            self.button_1_5.setText(newMessage[1])
                    else:
                        self.generalScore = int(newMessage[5])
                        if newMessage[3] == '0':
                            self.button_1_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_1_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_1_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_1_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_1_4.setText(newMessage[1].lower())
                        elif newMessage[3] == '5':
                            self.button_1_5.setText(newMessage[1].lower())                        
      
                elif newMessage[2] == '2':
                    if self.generalScore<int(newMessage[5]):
                        self.generalScore = int(newMessage[5])
                        if newMessage[3] == '0':
                            self.button_2_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_2_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_2_2.setText(newMessage[1])
                        elif newMessage[3] == '3':
                            self.button_2_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_2_4.setText(newMessage[1])
                        elif newMessage[3] == '5':
                            self.button_2_5.setText(newMessage[1])
                            
                    else:
                        self.generalScore = int(newMessage[5])
                        if newMessage[3] == '0':
                            self.button_2_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_2_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_2_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_2_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_2_4.setText(newMessage[1].lower())
                        elif newMessage[3] == '5':
                            self.button_2_5.setText(newMessage[1].lower())                        
                            
                elif newMessage[2] == '3':
                    if self.generalScore<int(newMessage[5]):
                        self.generalScore = int(newMessage[5])
                        if newMessage[3] == '0':
                            self.button_3_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_3_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_3_2.setText(newMessage[1])
                        elif newMessage[3] == '3':
                            self.button_3_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_3_4.setText(newMessage[1])
                        elif newMessage[3] == '5':
                            self.button_3_5.setText(newMessage[1])
                                       
                    else:
                        self.generalScore = int(newMessage[5])
                        if newMessage[3] == '0':
                            self.button_3_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_3_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_3_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_3_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_3_4.setText(newMessage[1].lower())
                        elif newMessage[3] == '5':
                            self.button_3_5.setText(newMessage[1].lower())                        
                        
                elif newMessage[2] == '4':
                    if self.generalScore<int(newMessage[5]):
                        self.generalScore = int(newMessage[5])
                        if newMessage[3] == '0':
                            self.button_4_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_4_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_4_2.setText(newMessage[1])
                        elif newMessage[3] == '3':
                            self.button_4_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_4_4.setText(newMessage[1])
                            
                    else:
                        self.generalScore = int(newMessage[5])
                        if newMessage[3] == '0':
                            self.button_4_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_4_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_4_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_4_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_4_4.setText(newMessage[1].lower())                            
                        elif newMessage[3] == '5':
                            self.button_4_5.setText(newMessage[1].lower())
                            
                elif newMessage[2] == '5':
                    if self.generalScore<int(newMessage[5]):
                        self.generalScore = int(newMessage[5])
                        if int(newMessage[4]) == '0':
                            self.button_5_0.setText(newMessage[1])
                        elif newMessage[3] == '1':
                            self.button_5_1.setText(newMessage[1])
                        elif newMessage[3] == '2':
                            self.button_5_2.setText(newMessage[1])
                        elif newMessage[3] == '3':
                            self.button_5_3.setText(newMessage[1])
                        elif newMessage[3] == '4':
                            self.button_5_4.setText(newMessage[1])
                        elif newMessage[3] == '5':
                            self.button_5_5.setText(newMessage[1])
                    else:
                        self.generalScore = int(newMessage[5])
                        if newMessage[3] == '0':
                            self.button_5_0.setText(newMessage[1].lower())
                        elif newMessage[3] == '1':
                            self.button_5_1.setText(newMessage[1].lower())
                        elif newMessage[3] == '2':
                            self.button_5_2.setText(newMessage[1].lower())
                        elif newMessage[3] == '3':
                            self.button_5_3.setText(newMessage[1].lower())
                        elif newMessage[3] == '4':
                            self.button_5_4.setText(newMessage[1].lower())
                        elif newMessage[3] == '5':
                            self.button_5_5.setText(newMessage[1].lower()) 
        self.score_edit.setText('Captein Score: {}\nGeneralScore: {}'.format(self.captainScore,self.generalScore))
                            
    def newGameSlot(self):
        
        self.myGameLoop.playAgain("y")
        
        self.button_0_0 = QtGui.QPushButton()
        self.button_0_0 .setStyleSheet("background-color: cyan")
        self.button_0_0.setFixedSize(70,70)
        self.button_0_0.setObjectName('0,0')
        self.button_0_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_0,0,0)
        self.allButtons[self.button_0_0] = '0,0'
        self.button_0_1 = QtGui.QPushButton()
        self.button_0_1.setFixedSize(70,70)
        self.button_0_1 .setStyleSheet("background-color: cyan")
        self.button_0_1.setObjectName('0,1')
        self.button_0_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_1,0,1)
        self.allButtons[self.button_0_1] = '0,1'
        self.button_0_2 = QtGui.QPushButton()
        self.button_0_2 .setStyleSheet("background-color: cyan")
        self.button_0_2.setFixedSize(70,70)
        self.button_0_2.setObjectName('0,2')
        self.button_0_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_2,0,2)
        self.allButtons[self.button_0_2] = '0,2'
        self.button_0_3 = QtGui.QPushButton()
        self.button_0_3 .setStyleSheet("background-color: cyan")
        self.button_0_3.setFixedSize(70,70)
        self.button_0_3.setObjectName('0,3')
        self.button_0_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_3,0,3)
        self.allButtons[self.button_0_3] = '0,3'
        self.button_0_4 = QtGui.QPushButton()
        self.button_0_4 .setStyleSheet("background-color: cyan")
        self.button_0_4.setFixedSize(70,70)
        self.button_0_4.setObjectName('0,4')
        self.button_0_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_4,0,4)
        self.allButtons[self.button_0_4] = '0,4'
        self.button_0_5 = QtGui.QPushButton()
        self.button_0_5 .setStyleSheet("background-color: cyan")
        self.button_0_5.setFixedSize(70,70)
        self.button_0_5.setObjectName('0,5')
        self.button_0_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_0_5,0,5)
        self.allButtons[self.button_0_5] = '0,5'
        self.button_1_0 = QtGui.QPushButton()
        self.button_1_0 .setStyleSheet("background-color: cyan")
        self.button_1_0.setFixedSize(70,70)
        self.button_1_0.setObjectName('1,0')
        self.button_1_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_0,1,0)
        self.allButtons[self.button_1_0] = '1,0'
        self.button_1_1 = QtGui.QPushButton()
        self.button_1_1 .setStyleSheet("background-color: cyan")
        self.button_1_1.setFixedSize(70,70)
        self.button_1_1.setObjectName('1,1')
        self.button_1_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_1,1,1)
        self.allButtons[self.button_1_1] = '1,1'
        self.button_1_2 = QtGui.QPushButton()
        self.button_1_2 .setStyleSheet("background-color: cyan")
        self.button_1_2.setFixedSize(70,70)
        self.button_1_2.setObjectName('1,2')
        self.button_1_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_2,1,2)
        self.allButtons[self.button_1_2] = '1,2'
        self.button_1_3 = QtGui.QPushButton()
        self.button_1_3 .setStyleSheet("background-color: cyan")
        self.button_1_3.setFixedSize(70,70)
        self.button_1_3.setObjectName('1,3')
        self.button_1_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_3,1,3)
        self.allButtons[self.button_1_3] = '1,3'
        self.button_1_4 = QtGui.QPushButton()
        self.button_1_4 .setStyleSheet("background-color: cyan")
        self.button_1_4.setFixedSize(70,70)
        self.button_1_4.setObjectName('1,4')
        self.button_1_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_4,1,4)
        self.allButtons[self.button_1_4] = '1,4'
        self.button_1_5 = QtGui.QPushButton()
        self.button_1_5 .setStyleSheet("background-color: cyan")
        self.button_1_5.setFixedSize(70,70)
        self.button_1_5.setObjectName('1,5')
        self.button_1_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_1_5,1,5)
        self.allButtons[self.button_1_5] = '1,5'
        self.button_2_0 = QtGui.QPushButton()
        self.button_2_0 .setStyleSheet("background-color: cyan")
        self.button_2_0.setFixedSize(70,70)
        self.button_2_0.setObjectName('2,0')
        self.button_2_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_0,2,0)
        self.allButtons[self.button_2_0] = '2,0'
        self.button_2_1 = QtGui.QPushButton()
        self.button_2_1 .setStyleSheet("background-color: cyan")
        self.button_2_1.setFixedSize(70,70)
        self.button_2_1.setObjectName('2,1')
        self.button_2_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_1,2,1)
        self.allButtons[self.button_2_1] = '2,1'
        self.button_2_2 = QtGui.QPushButton()
        self.button_2_2 .setStyleSheet("background-color: cyan")
        self.button_2_2.setFixedSize(70,70)
        self.button_2_2.setObjectName('2,2')
        self.button_2_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_2,2,2)
        self.allButtons[self.button_2_2] = '2,2'
        self.button_2_3 = QtGui.QPushButton()
        self.button_2_3 .setStyleSheet("background-color: cyan")
        self.button_2_3.setFixedSize(70,70)
        self.button_2_3.setObjectName('2,3')
        self.button_2_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_3,2,3)
        self.allButtons[self.button_2_3] = '2,3'
        self.button_2_4 = QtGui.QPushButton()
        self.button_2_4 .setStyleSheet("background-color: cyan")
        self.button_2_4.setFixedSize(70,70)
        self.button_2_4.setObjectName('2,4')
        self.button_2_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_4,2,4)
        self.allButtons[self.button_2_4] = '2,4'
        self.button_2_5 = QtGui.QPushButton()
        self.button_2_5 .setStyleSheet("background-color: cyan")
        self.button_2_5.setFixedSize(70,70)
        self.button_2_5.setObjectName('2,5')
        self.button_2_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_2_5,2,5)
        self.allButtons[self.button_2_5] = '2,5'
        self.button_3_0 = QtGui.QPushButton()
        self.button_3_0 .setStyleSheet("background-color: cyan")
        self.button_3_0.setFixedSize(70,70)
        self.button_3_0.setObjectName('3,0')
        self.button_3_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_0,3,0)
        self.allButtons[self.button_3_0] = '3,0'
        self.button_3_1 = QtGui.QPushButton()
        self.button_3_1 .setStyleSheet("background-color: cyan")
        self.button_3_1.setFixedSize(70,70)
        self.button_3_1.setObjectName('3,1')
        self.button_3_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_1,3,1)
        self.allButtons[self.button_3_1] = '3,1'
        self.button_3_2 = QtGui.QPushButton()
        self.button_3_2 .setStyleSheet("background-color: cyan")
        self.button_3_2.setFixedSize(70,70)
        self.button_3_2.setObjectName('3,2')
        self.button_3_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_2,3,2)
        self.allButtons[self.button_3_2] = '3,2'
        self.button_3_3 = QtGui.QPushButton()
        self.button_3_3 .setStyleSheet("background-color: cyan")
        self.button_3_3.setFixedSize(70,70)
        self.button_3_3.setObjectName('3,3')
        self.button_3_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_3,3,3)
        self.allButtons[self.button_3_3] = '3,3'
        self.button_3_4 = QtGui.QPushButton()
        self.button_3_4 .setStyleSheet("background-color: cyan")
        self.button_3_4.setFixedSize(70,70)
        self.button_3_4.setObjectName('3,4')
        self.button_3_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_4,3,4)
        self.allButtons[self.button_3_4] = '3,4'
        self.button_3_5 = QtGui.QPushButton()
        self.button_3_5 .setStyleSheet("background-color: cyan")
        self.button_3_5.setFixedSize(70,70)
        self.button_3_5.setObjectName('3,5')
        self.button_3_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_3_5,3,5)
        self.allButtons[self.button_3_5] = '3,5'
        self.button_4_0 = QtGui.QPushButton()
        self.button_4_0 .setStyleSheet("background-color: cyan")
        self.button_4_0.setFixedSize(70,70)
        self.button_4_0.setObjectName('4,0')
        self.button_4_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_0,4,0)
        self.allButtons[self.button_4_0] = '4,0'
        self.button_4_1 = QtGui.QPushButton()
        self.button_4_1 .setStyleSheet("background-color: cyan")
        self.button_4_1.setFixedSize(70,70)
        self.button_4_1.setObjectName('4,1')
        self.button_4_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_1,4,1)
        self.allButtons[self.button_4_1] = '4,1'
        self.button_4_2 = QtGui.QPushButton()
        self.button_4_2 .setStyleSheet("background-color: cyan")
        self.button_4_2.setFixedSize(70,70)
        self.button_4_2.setObjectName('4,2')
        self.button_4_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_2,4,2)
        self.allButtons[self.button_4_2] = '4,2'
        self.button_4_3 = QtGui.QPushButton()
        self.button_4_3 .setStyleSheet("background-color: cyan")
        self.button_4_3.setFixedSize(70,70)
        self.button_4_3.setObjectName('4,3')
        self.button_4_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_3,4,3)
        self.allButtons[self.button_4_3] = '4,3'
        self.button_4_4 = QtGui.QPushButton()
        self.button_4_4 .setStyleSheet("background-color: cyan")
        self.button_4_4.setFixedSize(70,70)
        self.button_4_4.setObjectName('4,4')
        self.button_4_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_4,4,4)
        self.allButtons[self.button_4_4] = '4,4'
        self.button_4_5 = QtGui.QPushButton()
        self.button_4_5 .setStyleSheet("background-color: cyan")
        self.button_4_5.setFixedSize(70,70)
        self.button_4_5.setObjectName('4,5')
        self.button_4_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_4_5,4,5)
        self.allButtons[self.button_4_5] = '4,5'
        self.button_5_0 = QtGui.QPushButton()
        self.button_5_0 .setStyleSheet("background-color: cyan")
        self.button_5_0.setFixedSize(70,70)
        self.button_5_0.setObjectName('5,0')
        self.button_5_0.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_0,5,0)
        self.allButtons[self.button_5_0] = '5,0'
        self.button_5_1 = QtGui.QPushButton()
        self.button_5_1 .setStyleSheet("background-color: cyan")
        self.button_5_1.setFixedSize(70,70)
        self.button_5_1.setObjectName('5,1')
        self.button_5_1.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_1,5,1)
        self.allButtons[self.button_5_1] = '5,1'
        self.button_5_2 = QtGui.QPushButton()
        self.button_5_2 .setStyleSheet("background-color: cyan")
        self.button_5_2.setFixedSize(70,70)
        self.button_5_2.setObjectName('5,2')
        self.button_5_2.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_2,5,2)
        self.allButtons[self.button_5_2] = '5,2'
        self.button_5_3 = QtGui.QPushButton()
        self.button_5_3 .setStyleSheet("background-color: cyan")
        self.button_5_3.setFixedSize(70,70)
        self.button_5_3.setObjectName('5,3')
        self.button_5_3.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_3,5,3)
        self.allButtons[self.button_5_3] = '5,3'
        self.button_5_4 = QtGui.QPushButton()
        self.button_5_4 .setStyleSheet("background-color: cyan")
        self.button_5_4.setFixedSize(70,70)
        self.button_5_4.setObjectName('5,4')
        self.button_5_4.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_4,5,4)
        self.allButtons[self.button_5_4] = '5,4'
        self.button_5_5 = QtGui.QPushButton()
        self.button_5_5 .setStyleSheet("background-color: cyan")
        self.button_5_5.setFixedSize(70,70)
        self.button_5_5.setObjectName('5,5')
        self.button_5_5.clicked.connect(self.buttonNameSlot)
        self.buttonGrid.addWidget(self.button_5_5,5,5)
        self.allButtons[self.button_5_5] = '5,5'
        
        self.generalScore = 0
        self.captainScore = 0        
        
                            
                            
    def cancelbutton(self):
            self.close()      
            
    def closeEvent(self, event):
        quit_msg = "Are you sure you want to close the Game?"
        reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
    
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()    
   
class Battleship(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Battleship, self).__init__(parent)
        self.setWindowTitle('BattleShipGame Help')
        self.setFixedSize(300,400)
        
        self.exit = QtGui.QPushButton(".exit")

        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.append("GAME DESCRIPTION:" +"\n"+"\n"+"•Battleship game is a 6x6 grid/board game."+"\n"+"•Five boats are placed on the board randomly and can either be horizontal or vertical but the boats wil not be visible to both players and the aim is to sink all five boats. Each boat covers two blocks."+"\n"+"\n"+ "•The game requires two players(officers of the same army), each player is assigned a role of being either the Captain or the General of the ship. Both players are responsible for sinking oncoming enemy ships. "+"\n"+"\n"+"INSTRUCTIONS:"+"\n"+"\n"+"•Each player gets a chance to choose(click) a position on the board to fire a shot at sinking a boat. Only one player can play in each turn."+"\n"+"•One point is assigned to a player after choosing a position which hits and damages a boat the first time and two points are assigned to a player if the same boat is hit again and is sunk"+"\n"+"•The winner is the player to get the most hit points after all five boat are sunk."+"\n"+"\n"+"•Click 'Play Game' to start the game")

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.exit)
        
        self.exit.clicked.connect(self.exitButton)
    
    def exitButton(self):
        self.close()

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle('BattleShipGame')
        self.setGeometry(350, 400, 600, 400)
        self.setFixedSize(570,380)
        self.palette = QtGui.QPalette()
        self.palette.setBrush(QtGui.QPalette.Background,QBrush(QPixmap("a.jpg")))
        self.setPalette(self.palette) 
        
        #
        self.play = QtGui.QPushButton('Play Game')
        self.play.setFixedWidth(100)
        self.play.setFixedHeight(50)        
        self.help = QtGui.QPushButton('Help')
        self.help.setFixedWidth(100)
        self.help.setFixedHeight(50)        
        self.cancel = QtGui.QPushButton('Close')
        self.cancel.setFixedWidth(100)
        self.cancel.setFixedHeight(50)        
        
        
        grid = QtGui.QGridLayout()
        grid.addWidget(self.play,0,0)
        grid.addWidget(self.cancel,0,1)
        grid.addWidget(self.help,1,0)
        self.setLayout(grid)
        
        #
        self.dialogTextBrowser = Battleship(self)
        login_widget = GuiClient()
        #
        self.help.clicked.connect(self.PushButton)
        self.cancel.clicked.connect(self.cancelButton)
        self.play.clicked.connect(self.play_gameButton)

    def PushButton(self):
        self.dialogTextBrowser.exec_()
     
    def cancelButton(self):
        self.close()  
        
    def play_gameButton(self):
        self.login_widget = GuiClient()
        self.login_widget.show()
        
    def closeEvent(self, event):
        quit_msg = "Are you sure you want to close the program?"
        reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
    
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()      

def main():
    app = QtGui.QApplication(sys.argv) 
    battleship_game = MyWindow()
    battleship_game.show()
    sys.exit(app.exec_())
main()
                
