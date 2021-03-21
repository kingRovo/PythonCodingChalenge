import random

board=['hi',1,2,3,4,5,6,7,8,9]
switch="p1"
j=9
print("\n\t\t\tTIK-TAK -Developed by KingRovo")
def print_board():
    print("\n\n")
    print("    |     |" )
    print("",board[1]," | ",board[2]," | ",board[3] )
    print("____|_____|____")
    print("    |     |" )
    print("",board[4]," | ",board[5]," | ",board[6] )
    print("____|_____|____")
    print("    |     |" )
    print("",board[7]," | ",board[8]," | ",board[9] )
    print("    |     |" )
def enter_number(p1_sign,p2_sign,p1N,p2N,nu_of_pl):

    li=[1,2,3,4,5,6,7,8,9]
    global switch
    global j
    k=9
    while(j):
        if k==0:
            break
        
        if switch=="p1":
            if(nu_of_pl==1):
                p1_input =    random.choice(li)
                li.remove(p1_input)
                
                print("\n",p1N,":- ",p1_input)
            else:
                print(p1N,end='')
                p1_input=int(input(" :- "))
                
            if p1_input<=0:
                print("chose number from given board")
            else:
                for e in range(1,10):
                    if board[e]==p1_input:
                        board[e]=p1_sign
                        print_board()
                        c=checkwin()
                        if c==1:
                            if(nu_of_pl==1):
                                print("ohh!!!..You Loss ")
                            else:
                                print("\n\n Congratulation !  ",p1N)
                            return
                        
                        
                        switch="p2"
                        j-=1
                        k-=1
                        if k==0:
                            print("\n\nGame is over")
                            break
                        
        if k==0:
            
            break
                   
        if switch=="p2":
            print(p2N,end='')
            p2_input=int(input(" :- "))
            li.remove(p2_input)
            
            if p2_input<=0:
                print("chose number from given board")
                
            else:
                for e in range(1,10):
                    if board[e]==p2_input:
                        board[e]=p2_sign
                        print_board()
                        w=checkwin()
                        if w==1:
                            print("\n\n Congratulation ! ",p2N,"You Win !")
                            return
                        
                        switch="p1"
                        j-=1
                        k-=1
                        
                    
def checkwin():
    if board[1]==board[2]==board[3]:
        
        return 1
    elif board[4]==board[5]==board[6]:
        
        return 1
    elif board[7]==board[8]==board[9]:
        
        return 1
    elif board[1]==board[4]==board[7]:
        
        return 1

    elif board[2]==board[5]==board[8]:
        
        return 1
    elif board[3]==board[6]==board[9]:
        
        return 1
    elif board[1]==board[5]==board[9]:
        
        return 1
    elif board[3]==board[5]==board[7]:
        
        return 1
    else:
        print("\n\nGame continue")
        
def play():
    
    print_board()
    n_o_p=int(input("How Many player 1 or 2 :-"))
    if(n_o_p==1):
        p1_sign=random.choice(['#','*','0','X'])
        print("\n\nComputer Sign = ",p1_sign)
        p2_sign=input("What's your Sign  = ")
        p1_name='Computer '
        p2_name=input("What's Your Name:- ")
        
    elif(n_o_p==2):
        p1_sign=input("\n\nplayer 1 What's your sign  = ")
        p2_sign=input("player 2 What's your sign  = ")
        p1_name=input("Player 1 Name:- ")
        p2_name=input("Player 2 Name:- ")
    else:
        print("Chose only 1 or 2 ")
    
    
    enter_number(p1_sign,p2_sign,p1_name,p2_name,n_o_p)

    print("\n\n\t\t\t\t|   |   |__         ")
    print("\t\t\t\t|   |   |__|        ")
    print("\t\t\t\t|___| * |           ")
    
play()
    



