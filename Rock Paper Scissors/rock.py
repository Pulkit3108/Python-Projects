from random import randint
t=['Rock','Paper','Scissors']
def game(p):
    w=0
    com=t[randint(0,2)]
    if(p==com):
        print('Tie! Both Have Chosen',p)
        w=0
    elif(p=="Rock"):
        if(com=="Paper"):
            print("\nYou Lose...", com, "Covers", p)
            w=-1
        else:
            print("\nYou Win!", p, "Smashes", com)
            w=1
    elif(p=="Paper"):
        if(com=="Scissors"):
            print("\nYou Lose...", com, "Cut", p)
            w=-1
        else:
            print("\nYou Win!", p, "Covers", com)
            w=1
    elif(p=="Scissors"):
        if(com=="Rock"):
            print("\nYou Lose...", com, "Smashes", p)
            w=-1
        else:
            print("\nYou Win!", p, "Cut", com)
            w=1
    return(w)
def scoreboard(s):
    print("\t--------------------------------")
    print("\t           SCOREBOARD           ")
    print("\t--------------------------------")
    pw=list(s.keys())
    print("\t   ", pw[0], "\t    ", s[pw[0]])
    print("\t   ", pw[1], "\t    ", s[pw[1]])
    print("\t--------------------------------\n")
p=input('Enter Your Name : ')
print()
s={p:0,'Computer':0}
scoreboard(s)
while(True):
    print("Enter 1 for Rock")
    print("Enter 2 for Paper")
    print("Enter 3 for Scissors")
    print("Enter 4 for Quit")
    print("Enter your Choice : ",end='')
    c=int(input())
    print("--------------------------------")
    if(c==4):
        print("Final Scores : ")
        scoreboard(s)
        break
    elif(c!=1 and c!=2 and c!=3):
        print(c)
        print("\nWrong Choice! Try Again\n")
        continue
    w=game(t[c-1])
    if(w==-1):
        s['Computer']+=2
    elif(w==1):
        s[p]+=2
    else:
        s[p]+=1
        s['Computer']+=1
    scoreboard(s)

    
