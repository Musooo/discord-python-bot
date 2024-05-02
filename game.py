import random

class Game:
    
    def __init__(self,userC):  
        self.userC=userC
        self.compC=random.randint(1,5)
        self.choiceL=["🤚","✊","✌️","🦎","🖖"]

    def result(self): # game logic implementation that return the result of the game
        if self.userC==self.compC:
            return "Tie"
        elif self.userC == 1 and (self.compC==3 or self.compC==4) or self.userC == 2 and (self.compC==1 or self.compC==5) or self.userC == 3 and (self.compC==2 or self.compC==5) or self.userC == 4 and (self.compC==2 or self.compC==3) or self.userC == 5 and (self.compC==1 or self.compC==4):
            return "you lose"
        else :
            return "you won"
    
    def printC(self): # return the choices of the user and the bot
        return f"you choose: {self.choiceL[self.userC-1]}\nthe bot choose: {self.choiceL[self.compC-1]}"
