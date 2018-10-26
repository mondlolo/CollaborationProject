from PyQt4 import QtCore

from PyQt4.QtGui import *
from GameClient import*
from time import*

class GameLoop(QtCore.QThread,GameClient):
    updateButtonMessageSignal = QtCore.pyqtSignal(str)

    def __init__(self):
        QtCore.QThread.__init__(self) 
        GameClient.__init__(self)
        self.response = ""
        #self.updateButtonMessageSignal = QtCore.pyqtSignal(str)
        
   
        
    def receiveIPAdress(self,ip):
        ipAdress = ip
        
        while True:
            try:
                self.connect_to_server(ipAdress)
                #self.response = 'Connected to server'
                #print(self.response)
                break
            except:
                self.response=  'Error connecting to server!'
                print('Error connecting to server!')
                break
        #self.play_loop()
        #input('Press enter to exit.') 
  
    def run(self):
        while True:
            
            msg = self.receive_message()
            #print(msg)
            sleep(5)
            if len(msg): self.updateButtonMessageSignal.emit(str(msg))
            else: break               