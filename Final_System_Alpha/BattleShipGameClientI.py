import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import*

from GameLoop import *

class GuiClient(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('BattleShipGame')
        
        mainGrid = QtGui.QGridLayout()
        
        self.box = QtGui.QGroupBox('b')
        buttonGrid = QtGui.QGridLayout()
    
        
        self.palette = QtGui.QPalette()
        self.palette.setBrush(QtGui.QPalette.Background,QBrush(QPixmap("b.jpg")))
        self.setPalette(self.palette)
        
        
         # creating variables
        self.ipAdress = ""
        self.received_message = ""
        
    
        # Creating text edits
        self.msg_edit = QtGui.QTextEdit()
        self.role_edit = QtGui.QTextEdit()
        score_edit = QtGui.QTextEdit()
        
        #Creating Buttons
        new_game = QtGui.QPushButton("new Game")
        exit = QtGui.QPushButton("Exit")        
        self.button_0_0 = QtGui.QPushButton()
        self.button_0_1 = QtGui.QPushButton()
        self.button_0_2 = QtGui.QPushButton()
        self.button_0_3 = QtGui.QPushButton()
        self.button_0_4 = QtGui.QPushButton()
        self.button_0_5 = QtGui.QPushButton()
        self.button_1_0 = QtGui.QPushButton()
        self.button_1_1 = QtGui.QPushButton()
        self.button_1_2 = QtGui.QPushButton()
        self.button_1_3 = QtGui.QPushButton()
        self.button_1_4 = QtGui.QPushButton()
        self.button_1_5 = QtGui.QPushButton()
        self.button_2_0 = QtGui.QPushButton()
        self.button_2_1 = QtGui.QPushButton()
        self.button_2_2 = QtGui.QPushButton()
        self.button_2_3 = QtGui.QPushButton()
        self.button_2_4 = QtGui.QPushButton()
        self.button_2_5 = QtGui.QPushButton()
        self.button_3_0 = QtGui.QPushButton()
        self.button_3_1 = QtGui.QPushButton()
        self.button_3_2 = QtGui.QPushButton()
        self.button_3_3 = QtGui.QPushButton()
        self.button_3_4 = QtGui.QPushButton()
        self.button_3_5 = QtGui.QPushButton()
        self.button_4_0 = QtGui.QPushButton()
        self.button_4_1 = QtGui.QPushButton()
        self.button_4_2 = QtGui.QPushButton()
        self.button_4_3 = QtGui.QPushButton()
        self.button_4_4 = QtGui.QPushButton()
        self.button_4_5 = QtGui.QPushButton()
        self.button_5_0 = QtGui.QPushButton()
        self.button_5_1 = QtGui.QPushButton()
        self.button_5_2 = QtGui.QPushButton()
        self.button_5_3 = QtGui.QPushButton()
        self.button_5_4 = QtGui.QPushButton()
        self.button_5_5 = QtGui.QPushButton()
        #
        
        self.button_0_0.setFixedWidth(110)
        self.button_0_0.setFixedHeight(70)
        self.button_0_1.setFixedWidth(110)
        self.button_0_1.setFixedHeight(70)
        self.button_0_2.setFixedWidth(110)
        self.button_0_2.setFixedHeight(70)
        self.button_0_3.setFixedWidth(110)
        self.button_0_3.setFixedHeight(70)
        self.button_0_4.setFixedWidth(110)
        self.button_0_4.setFixedHeight(70)
        self.button_0_5.setFixedWidth(110)
        self.button_0_5.setFixedHeight(70)
        self.button_1_0.setFixedWidth(110)
        self.button_1_0.setFixedHeight(70)
        self.button_1_1.setFixedWidth(110)
        self.button_1_1.setFixedHeight(70)
        self.button_1_2.setFixedWidth(110)
        self.button_1_2.setFixedHeight(70)
        self.button_1_3.setFixedWidth(110)
        self.button_1_3.setFixedHeight(70)
        self.button_1_4.setFixedWidth(110)
        self.button_1_4.setFixedHeight(70)
        self.button_1_5.setFixedWidth(110)
        self.button_1_5.setFixedHeight(70)
        self.button_2_0.setFixedWidth(110)
        self.button_2_0.setFixedHeight(70)
        self.button_2_1.setFixedWidth(110)
        self.button_2_1.setFixedHeight(70)
        self.button_2_2.setFixedWidth(110)
        self.button_2_2.setFixedHeight(70)
        self.button_2_3.setFixedWidth(110)
        self.button_2_3.setFixedHeight(70)
        self.button_2_4.setFixedWidth(110)
        self.button_2_4.setFixedHeight(70)
        self.button_2_5.setFixedWidth(110)
        self.button_2_5.setFixedHeight(70)
        self.button_3_0.setFixedWidth(110)
        self.button_3_0.setFixedHeight(70)
        self.button_3_1.setFixedWidth(110)
        self.button_3_1.setFixedHeight(70)
        self.button_3_2.setFixedWidth(110)
        self.button_3_2.setFixedHeight(70)
        self.button_3_3.setFixedWidth(110)
        self.button_3_3.setFixedHeight(70)
        self.button_3_4.setFixedWidth(110)
        self.button_3_4.setFixedHeight(70)
        self.button_3_5.setFixedWidth(110)
        self.button_3_5.setFixedHeight(70)
        self.button_4_0.setFixedWidth(110)
        self.button_4_0.setFixedHeight(70)
        self.button_4_1.setFixedWidth(110)
        self.button_4_1.setFixedHeight(70)
        self.button_4_2.setFixedWidth(110)
        self.button_4_2.setFixedHeight(70)
        self.button_4_3.setFixedWidth(110)
        self.button_4_3.setFixedHeight(70)
        self.button_4_4.setFixedWidth(110)
        self.button_4_4.setFixedHeight(70)
        self.button_4_5.setFixedWidth(110)
        self.button_4_5.setFixedHeight(70)
        self.button_5_0.setFixedWidth(110)
        self.button_5_0.setFixedHeight(70)
        self.button_5_1.setFixedWidth(110)
        self.button_5_1.setFixedHeight(70)
        self.button_5_2.setFixedWidth(110)
        self.button_5_2.setFixedHeight(70)
        self.button_5_3.setFixedWidth(110)
        self.button_5_3.setFixedHeight(70)
        self.button_5_4.setFixedWidth(110)
        self.button_5_4.setFixedHeight(70)
        self.button_5_5.setFixedWidth(110)
        self.button_5_5.setFixedHeight(70)
                
        #creating labels      
        label1 = QtGui.QLabel('Enter Server:',self)
        label1.setFont(QtGui.QFont('times',20))
        label2 = QtGui.QLabel('Role/Player:',self)
        label2.setFont(QtGui.QFont('times',20))
        label3 = QtGui.QLabel('Game:',self)
        label3.setFont(QtGui.QFont('times',20))
        self.label4 = QtGui.QLabel('Message from server:',self)
        self.label4.setFont(QtGui.QFont('times',20))
        label5 = QtGui.QLabel('Scores:',self) 
        label5.setFont(QtGui.QFont('times',20))
        label6 = QtGui.QLabel('##BATTLESHIP GAME##',self)
        label6.setFont(QtGui.QFont('Courier',40,20))
        #
        self.server = QtGui.QLineEdit()
        self.connected = QtGui.QPushButton("Connect")
             
        mainGrid.addWidget(self.server,0,2)
        mainGrid.addWidget(self.connected,0,3)
        mainGrid.addWidget(label6,1,2)
        mainGrid.addWidget(label1,0,1)
        mainGrid.addWidget(self.label4,8,0)
        mainGrid.addWidget(self.msg_edit,9,0,1,2)
        mainGrid.addWidget(label5,5,0)
        mainGrid.addWidget(score_edit,6,0,2,2)
        mainGrid.addWidget(label3,4,4)
        mainGrid.addWidget(label2,2,4)
        mainGrid.addWidget(self.role_edit,4,4,1,1)
   
        mainGrid.addLayout(buttonGrid,7,2,3,3)
        mainGrid.addWidget(new_game,11,0)
        mainGrid.addWidget(exit,11,1)        

        self.setLayout(mainGrid)                
        # Inserting buttons into the grid
        
        buttonGrid.addWidget(self.button_0_0,0,0)
        buttonGrid.addWidget(self.button_0_1,0,1)
        buttonGrid.addWidget(self.button_0_2,0,2)
        buttonGrid.addWidget(self.button_0_3,0,3)
        buttonGrid.addWidget(self.button_0_4,0,4)
        buttonGrid.addWidget(self.button_0_5,0,5)
        buttonGrid.addWidget(self.button_1_0,1,0)
        buttonGrid.addWidget(self.button_1_1,1,1)
        buttonGrid.addWidget(self.button_1_2,1,2)
        buttonGrid.addWidget(self.button_1_3,1,3)
        buttonGrid.addWidget(self.button_1_4,1,4)
        buttonGrid.addWidget(self.button_1_5,1,5)
        buttonGrid.addWidget(self.button_2_0,2,0)
        buttonGrid.addWidget(self.button_2_1,2,1)
        buttonGrid.addWidget(self.button_2_2,2,2)
        buttonGrid.addWidget(self.button_2_3,2,3)
        buttonGrid.addWidget(self.button_2_4,2,4)
        buttonGrid.addWidget(self.button_2_5,2,5)
        buttonGrid.addWidget(self.button_3_0,3,0)
        buttonGrid.addWidget(self.button_3_1,3,1)
        buttonGrid.addWidget(self.button_3_2,3,2)
        buttonGrid.addWidget(self.button_3_3,3,3)
        buttonGrid.addWidget(self.button_3_4,3,4)
        buttonGrid.addWidget(self.button_3_5,3,5)
        buttonGrid.addWidget(self.button_4_0,4,0)
        buttonGrid.addWidget(self.button_4_1,4,1)
        buttonGrid.addWidget(self.button_4_2,4,2)
        buttonGrid.addWidget(self.button_4_3,4,3)
        buttonGrid.addWidget(self.button_4_4,4,4)
        buttonGrid.addWidget(self.button_4_5,4,5)
        buttonGrid.addWidget(self.button_5_0,5,0)
        buttonGrid.addWidget(self.button_5_1,5,1)
        buttonGrid.addWidget(self.button_5_2,5,2)
        buttonGrid.addWidget(self.button_5_3,5,3)
        buttonGrid.addWidget(self.button_5_4,5,4)
        buttonGrid.addWidget(self.button_5_5,5,5)
        self.box.setLayout(buttonGrid)
        self.myGameLoop = GameLoop()
        
        #Loop connections(receiving message from the client text in order to set label text in to the buttons)
       
        self.myGameLoop.updateButtonMessageSignal.connect(self.connectSlot)
       
        #Actions when buttons clicked
        
        self.button_0_0.clicked.connect(self.button_0_0_Clicked)
        self.button_0_1.clicked.connect(self.button_0_1_Clicked)
        self.button_0_2.clicked.connect(self.button_0_2_Clicked)
        self.button_0_3.clicked.connect(self.button_0_3_Clicked)
        self.button_0_4.clicked.connect(self.button_0_4_Clicked)
        self.button_0_5.clicked.connect(self.button_0_5_Clicked)
        self.button_1_0.clicked.connect(self.button_1_0_Clicked)
        self.button_1_1.clicked.connect(self.button_1_1_Clicked)
        self.button_1_2.clicked.connect(self.button_1_2_Clicked)
        self.button_1_3.clicked.connect(self.button_1_3_Clicked)
        self.button_1_4.clicked.connect(self.button_1_4_Clicked)
        self.button_1_5.clicked.connect(self.button_1_5_Clicked)
        self.button_2_0.clicked.connect(self.button_2_0_Clicked)
        self.button_2_1.clicked.connect(self.button_2_1_Clicked)
        self.button_2_2.clicked.connect(self.button_2_2_Clicked)
        self.button_2_3.clicked.connect(self.button_2_3_Clicked)
        self.button_2_4.clicked.connect(self.button_2_4_Clicked)
        self.button_2_5.clicked.connect(self.button_2_5_Clicked)
        self.button_3_0.clicked.connect(self.button_3_0_Clicked)
        self.button_3_1.clicked.connect(self.button_3_1_Clicked)
        self.button_3_2.clicked.connect(self.button_3_2_Clicked)
        self.button_3_3.clicked.connect(self.button_3_3_Clicked)
        self.button_3_4.clicked.connect(self.button_3_4_Clicked)
        self.button_3_5.clicked.connect(self.button_3_5_Clicked)
        self.button_4_0.clicked.connect(self.button_4_0_Clicked)
        self.button_4_1.clicked.connect(self.button_4_1_Clicked)
        self.button_4_2.clicked.connect(self.button_4_2_Clicked)
        self.button_4_3.clicked.connect(self.button_4_3_Clicked)
        self.button_4_4.clicked.connect(self.button_4_4_Clicked)
        self.button_4_5.clicked.connect(self.button_4_5_Clicked)
        self.button_5_0.clicked.connect(self.button_5_0_Clicked)
        self.button_5_1.clicked.connect(self.button_5_1_Clicked)
        self.button_5_2.clicked.connect(self.button_5_2_Clicked)
        self.button_5_3.clicked.connect(self.button_5_3_Clicked)
        self.button_5_4.clicked.connect(self.button_5_4_Clicked)
        self.button_5_5.clicked.connect(self.button_5_5_Clicked)
        self.connected.clicked.connect(self.connect_clicked)
    
        
        #Defined functions for connecting
    def button_0_0_Clicked(self):
        self.myGameLoop.start()
    def button_0_1_Clicked(self):
        self.myGameLoop.start()
    def button_0_2_Clicked(self):
        self.myGameLoop.start()
    def button_0_3_Clicked(self):
        self.myGameLoop.start()
    def button_0_4_Clicked(self):
        self.myGameLoop.start()
    def button_0_5_Clicked(self):
        self.myGameLoop.start()
    def button_1_0_Clicked(self):
        self.myGameLoop.start()
    def button_1_1_Clicked(self):
        self.myGameLoop.start()
    def button_1_2_Clicked(self):
        self.myGameLoop.start()
    def button_1_3_Clicked(self):
        self.myGameLoop.start()
    def button_1_4_Clicked(self):
        self.myGameLoop.start()
    def button_1_5_Clicked(self):
        self.myGameLoop.start()
    def button_2_0_Clicked(self):
        self.myGameLoop.start()
    def button_2_1_Clicked(self):
        self.myGameLoop.start()
    def button_2_2_Clicked(self):
        self.myGameLoop.start()
    def button_2_3_Clicked(self):
        self.myGameLoop.start()
    def button_2_4_Clicked(self):
        self.myGameLoop.start()
    def button_2_5_Clicked(self):
        self.myGameLoop.start()
    def button_3_0_Clicked(self):
        self.myGameLoop.start()
    def button_3_1_Clicked(self):
        self.myGameLoop.start()
    def button_3_2_Clicked(self):
        self.myGameLoop.start()
    def button_3_3_Clicked(self):
        self.myGameLoop.start()
    def button_3_4_Clicked(self):
        self.myGameLoop.start()
    def button_3_5_Clicked(self):
        self.myGameLoop.start()
    def button_4_0_Clicked(self):
        self.myGameLoop.start()
    def button_4_1_Clicked(self):
        self.myGameLoop.start()
    def button_4_2_Clicked(self):
        self.myGameLoop.start()
    def button_4_3_Clicked(self):
        self.myGameLoop.start()
    def button_4_4_Clicked(self):
        self.myGameLoop.start()
    def button_4_5_Clicked(self):
        self.myGameLoop.start()
    def button_5_0_Clicked(self):
        self.myGameLoop.start()
    def button_5_1_Clicked(self):
        self.myGameLoop.start()
    def button_5_2_Clicked(self):
        self.myGameLoop.start()
    def button_5_3_Clicked(self):
        self.myGameLoop.start()
    def button_5_4_Clicked(self):
        self.myGameLoop.start()
    def button_5_5_Clicked(self):
        self.myGameLoop.start()  
        
    def connect_clicked(self):
        self.ipAdress = self.server.displayText()
        self.myGameLoop.receiveIPAdress(self.ipAdress)
        self.myGameLoop.start()
        
        
    # The LoopThreadSlot for buttons
    def connectSlot(self,ms):
        s = ms
        self.msg_edit.setText(str(s)+"\n")
        myMs = ms.split(",")
        if myMs[0] == "new game":
            self.msg_edit.setText(myMs[0]+"\n")
            if myMs[1]=="C":
                
                self.role_edit.setText(myMs[1]+"---> Captain")
            else:
                self.role_edit.setText(myMs[1]+"---> General")
                
        #connecting button signals
    def button_0_0_LoopThreadSlot(self,msg):
        button_0_0.setText(msg)
    def button_0_1_LoopThreadSlot(self,msg):
        button_0_1.setText(msg)
    def button_0_2_LoopThreadSlot(self,msg):
        button_0_2.setText(msg)
    def button_0_3_LoopThreadSlot(self,msg):
        button_0_3.setText(msg)
    def button_0_4_LoopThreadSlot(self,msg):
        button_0_4.setText(msg)
    def button_0_5_LoopThreadSlot(self,msg):
        button_0_5.setText(msg)
    def button_1_0_LoopThreadSlot(self,msg):
        button_1_0.setText(msg)
    def button_1_1_LoopThreadSlot(self,msg):
        button_1_1.setText(msg)
    def button_1_2_LoopThreadSlot(self,msg):
        button_1_2.setText(msg)
    def button_1_3_LoopThreadSlot(self,msg):
        button_1_3.setText(msg)
    def button_1_4_LoopThreadSlot(self,msg):
        button_1_4.setText(msg)
    def button_1_5_LoopThreadSlot(self,msg):
        button_1_5.setText(msg)
    def button_2_0_LoopThreadSlot(self,msg):
        button_2_0.setText(msg)
    def button_2_1_LoopThreadSlot(self,msg):
        button_2_1.setText(msg)
    def button_2_2_LoopThreadSlot(self,msg):
        button_2_2.setText(msg)
    def button_2_3_LoopThreadSlot(self,msg):
        button_2_3.setText(msg)
    def button_2_4_LoopThreadSlot(self,msg):
        button_2_4.setText(msg)
    def button_2_5_LoopThreadSlot(self,msg):
        button_2_5.setText(msg)
    def button_3_0_LoopThreadSlot(self,msg):
        button_3_0.setText(msg)
    def button_3_1_LoopThreadSlot(self,msg):
        button_3_1.setText(msg)
    def button_3_2_LoopThreadSlot(self,msg):
        button_3_2.setText(msg)
    def button_3_3_LoopThreadSlot(self,msg):
        button_3_3.setText(msg)
    def button_3_4_LoopThreadSlot(self,msg):
        button_3_4.setText(msg)
    def button_3_5_LoopThreadSlot(self,msg):
        button_3_5.setText(msg)
    def button_4_0_LoopThreadSlot(self,msg):
        button_4_0.setText(msg)
    def button_4_1_LoopThreadSlot(self,msg):
        button_4_1.setText(msg)
    def button_4_2_LoopThreadSlot(self,msg):
        button_4_2.setText(msg)
    def button_4_3_LoopThreadSlot(self,msg):
        button_4_3.setText(msg)
    def button_4_4_LoopThreadSlot(self,msg):
        button_4_4.setText(msg)
    def button_4_5_LoopThreadSlot(self,msg):
        button_4_5.setText(msg)
    def button_5_0_LoopThreadSlot(self,msg):
        button_5_0.setText(msg)
    def button_5_1_LoopThreadSlot(self,msg):
        button_5_1.setText(msg)
    def button_5_2_LoopThreadSlot(self,msg):
        button_5_2.setText(msg)
    def button_5_3_LoopThreadSlot(self,msg):
        button_5_3.setText(msg)
    def button_5_4_LoopThreadSlot(self,msg):
        button_5_4.setText(msg)
    def button_5_5_LoopThreadSlot(self,msg):
        button_5_5.setText(msg)        
    
def main():
    app = QtGui.QApplication(sys.argv)
    login_widget = GuiClient()
    login_widget.show()
    sys.exit(app.exec_())

main()
        
