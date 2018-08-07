#TIC TAC TOE version 1.3
#author@ Rohan Prasad
#thing to work on : Implementation of gui and allowing the player to play first 
def main():
     board={'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
     turn='X'
     print("Do you want to start Y/N?")
     s=input()
     if(s=="N"):
        tic (board,turn,'comp')
     else:
       tic(board,turn,'player')
     
def chekSyntax(board,turn):
    for i in range(1,4):
        print('Please choose where you want to place')
        printBoard(board)
        loca=input()
        if loca in board:
            if board[str(loca)]==' ':
               return loca
            print('Coin already placed')
            i=i-1
        
def countCoint(board,turn):
    count=0
    for i in range(9):
        valt=str(i+1)
        if board[valt]!=' ':
            count=count+1
    return count
    
def tic (board,turn,toss):
        count=0
        if toss=='comp':
            print('comp plays')
            count=countCoint(board,turn)
            val=AI(board,turn,count,'comp')
            board[str(val)]='O'
            if chekWinner(board):
                loca=chekSyntax(board,turn)
                board[str(loca)]='X'
                tic(board,turn,toss)  

        else :
            loca=chekSyntax(board,turn)
            board[str(loca)]=turn
            count=countCoint(board,turn)
            val=AI(board,turn,count,'player')
            board[str(val)]='O'
            if chekWinner(board):
                tic(board,turn,toss)  
        if chekDraw(board):
            printBoard(board)
            print("Its a Draw")           
        else :
            printBoard(board)
            print("Computer wins")
            
            

def printBoard(board):
      print(board['1'] + '|' + board['2'] + '|' + board['3'])
      print('-+-+-')
      print(board['4'] + '|' + board['5'] + '|' + board['6'])
      print('-+-+-')
      print(board['7'] + '|' + board['8'] + '|' + board['9'])
      print('-+-+-')

def chekDraw(board):
    if chekWinner(board):
      for i in range(9):
        if board[str(i+1)]==' ':
            return False
      return True 
    return False

def chekWinner(board):
    if board['1']=='X' and board['2']=='X' and board['3']=='X' or board['1']=='O' and board['2']=='O' and board['3']=='O':
         return False
    elif board['4']=='X' and board['5']=='X' and board['6']=='X' or board['4']=='O' and board['5']=='O' and board['6']=='O':
         return False
    elif board['7']=='X' and board['8']=='X' and board['9']=='X' or board['7']=='O' and board['8']=='O' and board['9']=='O':
         return False
    elif board['1']=='X' and board['4']=='X' and board['7']=='X' or board['1']=='O' and board['4']=='O' and board['7']=='O':
         return False
    elif board['2']=='X' and board['5']=='X' and board['8']=='X' or board['2']=='O' and board['5']=='O' and board['8']=='O':
         return False
    elif board['3']=='X' and board['6']=='X' and board['9']=='X' or board['3']=='O' and board['6']=='O' and board['9']=='O':
         return False
    elif board['1']=='X' and board['5']=='X' and board['9']=='X' or board['1']=='O' and board['5']=='O' and board['9']=='O':
         return False
    elif board['3']=='X' and board['5']=='X' and board['7']=='X' or board['3']=='O' and board['5']=='O' and board['7']=='O':
         return False
    else:
         return True
        
def AI(board,turn,whoTurn,startTurn):
    play=0
    if startTurn=='comp':
        if whoTurn==0: play=randm(5)
        elif whoTurn==2:
            if board['5']==turn : play=giveDiagonal(findDiagonal(board,oppTurn(turn)))
            elif board['1']==turn or board['3']==turn or board['7']==turn or board['9']==turn:
                val=findDiagonal(board,oppTurn(turn))
                play=giveStraight(board,oppTurn(turn),val)
            else : play=5
        elif whoTurn==4 :
            count=countDiagonal(board,oppTurn(turn))
            winReslt=result(board,oppTurn(turn))
            reslt=result(board,turn)
            if(winReslt>0): return winReslt
            elif(reslt>0):  return reslt 
            if count==2 :
               play=giveTwoStaight(board,oppTurn(turn))   
            else :
               val=findDiagonal(board,oppTurn(turn))
               play=giveStraight(board,oppTurn(turn),val)
        else:
               winReslt=result(board,oppTurn(turn))
               reslt=result(board,turn)
               if(winReslt>0): return winReslt
               elif(reslt>0):  return reslt 
    else: 
        if whoTurn==1: 
            if board['5']==turn: play=randm(5)
            else : play=5
        elif whoTurn==3:
            if board['5']==turn:
                val=str(giveDiagonal(findDiagonal(board,oppTurn(turn))))
                if board[val]==turn: play=randm(1)
                else : return result(board,turn)
            else:
                val=str(giveDiagonal(findDiagonal(board,turn)))
                if board[val]==turn: play=randm(1)
                elif board['4']==turn: play=1
                elif board['8']==turn: play=9
                else : return result(board,turn)
        else :
            return result(board,turn)
    return play
        
def result(board,turn) :
    play=0
    rst=[chekDiagonal(board,turn),chekStraight(board,turn,'row'),chekStraight(board,turn,'col')]
    for i in range(3):
        if rst[i]!=0:
            play=rst[i]
            break  
    return play           
    
def oppTurn(turn):
    if turn=='X':
        return 'O'
    return 'X'


import random
def randm(num):
    if num==5:
        numb=[1,3,7,9]
        return random.choice(numb)

def findDiagonal(board,turn):
    for i in range(9):
        if board[str(i+1)]==turn:
           return i+1

def findSecondDiagonal(board,turn,valSkip):
     for i in range(9):
        if board[str(i+1)]==turn and i+1!=valSkip:
           return i+1

def giveDiagonal(num):
    if num==1:return 9
    if num==9:return 1
    if num==3:return 7
    if num==7:return 3
    return 0
   
def chekDiagonal(board,turn):
        if board['1']==turn and board['5']==turn and board['9']==' ': return 9
        elif board['1']==turn and board['9']==turn and board['5']==' ': return 5
        elif board['9']==turn and board['5']==turn and board['1']==' ': return 1
        elif board['3']==turn and board['5']==turn and board['7']==' ': return 7
        elif board['5']==turn and board['7']==turn and board['3']==' ': return 3
        elif board['3']==turn and board['7']==turn and board['5']==' ': return 5
        else: return 0
        
def chekStraight(board,turn,type):
    if type=='row':
        inc=3
        val=1
        rng=9
    else :
        val=3
        inc=1
        rng=3
    for i in range(0,rng,inc):
        x=i+1
        y=x+val
        z=y+val
        if board[str(x)]==turn and board[str(y)]==turn and board[str(z)]==' ':
            return z
        elif board[str(x)]==turn and board[str(z)]==turn and board[str(y)]==' ':
            return y
        elif board[str(y)]==turn and board[str(z)]==turn and board[str(x)]==' ':
            return x
    return 0
        
def giveStraight(board,turn,val):
    if val==9:
        if board[str(val-1)]==' ' and board[str(val-2)]==' ': return 7
        if board[str(val-3)]==' ' and board[str(val-6)]==' ': return 3
    elif val==7:
       if board[str(val+1)]==' ' and board[str(val+2)]==' ':  return 9
       if board[str(val-3)]==' ' and board[str(val-6)]==' ':  return 1
    elif val==3:
        if board[str(val-1)]==' ' and board[str(val-2)]==' ': return 1
        if board[str(val+3)]==' ' and board[str(val+6)]==' ': return 9
    elif val==1:
        if board[str(val+1)]==' ' and board[str(val+2)]==' ': return 3
        if board[str(val+3)]==' ' and board[str(val+6)]==' ': return 7
    return 0

def countDiagonal(board,turn):
    count=0
    if board['1']==turn: count=count+1
    if board['3']==turn: count=count+1
    if board['7']==turn: count=count+1
    if board['9']==turn: count=count+1
    return count 
          
def giveTwoStaight(board,turn):
     val=findDiagonal(board,turn)
     valOne=giveStraight(board,turn,val)
     val=findSecondDiagonal(board,turn,val)
     valTwo=giveStraight(board,turn,val)
     return max(valOne,valTwo)
 
main()


