import random
li=['stone','paper','scissor']
n=1
while(n==1):
    user1=random.choice(li)
    user2=input("Enter Your Choice: ")
    print("Computer Choice is: ",user1)
    print("Your choice is: ",user2)
    if(user1=='stone'):
              if(user2==scissor):
                   print("You loss")
              elif(user1==user2):
                  print("Tie")
              else:
                 print("You Win")
    elif(user1=='paper'):
              if(user1==user2):
                  print("Tie")
              elif(user2== "scissor"):
                  print("You Win")
              else:
                  print("You Loss")
    else:
        if(user1==user2):
              print("Tie")
        elif(user2=='paper'):
              print("You loss")
        else:
            print("You Win")
        print("Do You want To Continue")
        n=int(input("if yes press 1 otherwise press 0 :"))
              
