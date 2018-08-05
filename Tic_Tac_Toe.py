#TIC TAC TOE version 1.2
#author@ Rohan Prasad
#thing to work on : Implementation of gui and allowing the player to play first 
def main():
     board={'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
     turn='X'
     tic (board,turn,'comp')
     
def chekSyntax(board,turn,loca):
    if loca in board:
           if board[str(loca)]==' ':
               return True
           else :
               print('Coin already placed')
               return False
              
    else :
           return False
        
def tic (board,turn,toss):
        if toss=='comp':
            print('comp plays')
            count=0
            for i in range(9):
                valt=str(i+1)
                if board[valt]!=' ':
                    count=count+1

            val=AI(board,turn,count,'comp')
            board[str(val)]='O'
            printBoard(board)

            if chekDraw(board):
                print("Its a Draw")
                       
            elif chekWinner(board):
                print('Please choose where you want to place')
                loca=input()
                for i in range(1,4):
                    if chekSyntax(board,turn,loca):
                        board[str(loca)]='X'
                        break
                    else:
                       print('Please choose where you want to place')
                       printBoard(board)
                       loca=input()
                       i=i-1
                tic(board,turn,toss)
        
            else :
                  print("Computer wins")
        else:#need to implement when player starts
            return

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
               result=[chekDiagonal(board,turn),chekStraight(board,turn,'row'),chekStraight(board,turn,'col')]
               for i in range(3):
                  if result[i]!=0:
                     play=result[i]
                     return play
               winResult=[chekDiagonal(board,oppTurn(turn)),chekStraight(board,oppTurn(turn),'row'),chekStraight(board,oppTurn(turn),'col')]
               for i in range(3):
                      if winResult[i]!=0:
                        play=winResult[i]
                        return play
               if count==2 :
                   play=giveTwoStaight(board,oppTurn(turn))   
               else :
                   val=findDiagonal(board,oppTurn(turn))
                   play=giveStraight(board,oppTurn(turn),val)
          else:
                  winResult=[chekDiagonal(board,oppTurn(turn)),chekStraight(board,oppTurn(turn),'row'),chekStraight(board,oppTurn(turn),'col')]
                  for i in range(3):
                      if winResult[i]!=0:
                        play=winResult[i]
                  if play==0:                  
                      result=[chekDiagonal(board,turn),chekStraight(board,turn,'row'),chekStraight(board,turn,'col')]
                      for i in range(3):
                        if result[i]!=0:
                          play=result[i]

      
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
    if num==1:
        return 9
    if num==9:
        return 1
    if num==3:
        return 7
    if num==7:
        return 3
   
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
        if board[str(val-1)]==' ' and board[str(val-2)]==' ':
            return 7
        if board[str(val-3)]==' ' and board[str(val-6)]==' ':
            return 3
    elif val==7:
       if board[str(val+1)]==' ' and board[str(val+2)]==' ':
           return 9
       if board[str(val-3)]==' ' and board[str(val-6)]==' ':
           return 1
    elif val==3:
        if board[str(val-1)]==' ' and board[str(val-2)]==' ':
           return 1
        if board[str(val+3)]==' ' and board[str(val+6)]==' ':
           return 9
    elif val==1:
        if board[str(val+1)]==' ' and board[str(val+2)]==' ':
           return 3
        if board[str(val+3)]==' ' and board[str(val+6)]==' ':
           return 7
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


