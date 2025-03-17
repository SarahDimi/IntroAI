from BaseAI_3 import BaseAI
from Grid_3 import Grid

class PlayerAI(BaseAI):
    H=[[65536,32768,16384,8192],[512,1024,2048,4096],[256,128,64,32],[2,4,8,16]]
    def getMove(self, stage):
        self.initialStage=stage
        self.ALPHA=-999999999
        self.BETA=999999999
        self.deep=0
        move=self.SELECT()
        return move

    def SELECT(self):
        maxV=-999999999
        selectedMove=None
        nextStage=None
        for move in self.initialStage.getAvailableMoves():
            nextStage=self.initialStage.clone()
            nextStage.move(move)
            value=self.MIN(nextStage)
            if maxV < value:
                maxV=value 
                selectedMove=move
        return selectedMove

    def MAX(self, stage):
        self.deep=self.deep+1
        moves=stage.getAvailableMoves()
        nextStage=None
        if not moves or self.deep>6:
            self.deep=self.deep-1
            return self.CALCULATE(stage)
        average=-999999999
        for move in moves:
            nextStage=stage.clone()
            nextStage.move(move)
            average=max(average,self.MIN(nextStage))
            if(average>=self.BETA):
                self.deep=self.deep-1
                return average
            self.ALPHA=max(self.ALPHA,average)
        self.deep=self.deep-1
        return average

    def MIN(self, stage):
        self.deep=self.deep+1
        moves=stage.getAvailableCells()
        nextStage=None
        if not moves or self.deep>6:
            self.deep=self.deep-1
            return self.CALCULATE(stage)
        average = 999999999
        for move in moves:
            for value in range(2,5,2):
                nextStage=stage.clone()
                nextStage.setCellValue(move,value)
                nextV=self.MAX(nextStage)
                average=min(average,nextV)
                if(average<=nextV):
                    self.deep=self.deep-1
                    return average
        self.deep=self.deep-1
        return average

    def CALCULATE(self, stage):
        d=self.deep+1
        diff=0
        combine=0
        adding=0
        order=0
        for x in range(0,4,1):
            for y in range(0,4,1):
                adding=adding+stage.map[x][y]
                if stage.map[x][y]==0:
                    pass
                order=order+self.H[x][y]*stage.map[x][y]
                if((x==0)or(x==1)or(x==2)):
                    poss=x-1
                    diff=diff+(stage.map[x][y]-stage.map[poss][y])
                    if stage.map[x][y]==stage.map[poss][y]:
                        combine=combine+stage.map[x][y]
                if(x==4):
                    poss=x+1
                    diff=diff+(stage.map[x][y]-stage.map[poss][y])
                    if stage.map[x][y]==stage.map[poss][y]:
                        combine=combine+stage.map[x][y]        
                if((y==0)or(y==1)or(y==2)):
                    poss=y-1
                    diff=diff+(stage.map[x][y]-stage.map[x][poss])
                    if stage.map[x][y] == stage.map[x][poss]:
                        combine=combine+stage.map[x][y]
                if(y==4):
                    poss=y+1
                    diff=diff+(stage.map[x][y]-stage.map[x][poss])
                    if stage.map[x][y]==stage.map[x][poss]:
                        combine=combine+stage.map[x][y]               
        return 2*d*order+d*adding+d*diff+d*combine