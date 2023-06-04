from logguing import *
from index import *
class App:


    def __init__(self):
        pass

    def eject(self):
        key = iniciar()
        if(key==False):
            print("jaja")
            return 0
        else:
            index(key)
            return 1

    def conntrol(self):
        b = self.eject()
        while(b == 1):
             b = self.eject()


app = App()
app.conntrol()
