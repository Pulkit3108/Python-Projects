def board(v):
    print('\n')
    print('\t       |       |       ')
    print('\t   {}   |   {}   |   {}  '.format(v[0],v[1],v[2]))
    print('\t_______|_______|_______')
    print('\t       |       |       ')
    print('\t   {}   |   {}   |   {}  '.format(v[3],v[4],v[5]))
    print('\t_______|_______|_______')
    print('\t       |       |       ')
    print('\t   {}   |   {}   |   {}  '.format(v[6],v[7],v[8]))
    print('\t       |       |       ')
    print('\n')
def scoreboard(s):
    print("\t--------------------------------")
    print("\t           SCOREBOARD           ")
    print("\t--------------------------------")
    p=list(s.keys())
    print("\t   ", p[0], "\t    ", s[p[0]])
    print("\t   ", p[1], "\t    ", s[p[1]])
    print("\t--------------------------------\n")
def check(pos,o):
    sol=[[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]
    for i in sol:
        if(all([j in pos[o] for j in i])):
            return(True)
    return(False)
def check_d(pos):
    if(len(pos['X'])+len(pos['O'])==9):
        return(True)
    return(False)
def game(o,pc):
    v=[' ' for _ in range(9)]
    pos={'X':[],'O':[]}
    while(True):
        board(v)
        try:
            print("{}'s Turn".format(pc[o]))
            print("--------------------------------")
            print("Enter The Number of Cell : ", end="")
            m=int(input()) 
        except ValueError:
            print("Wrong Input! Try Again")
            continue
        if(m<1 or m>9):
            print("Wrong Input! Try Again")
            continue
        if(v[m-1]!=' '):
            print("Place Already Filled. Try again!")
            continue
        v[m-1]=o
        pos[o].append(m)
        if(check(pos,o)):
            board(v)
            print("Player ", o, " Has Won The Game!")     
            print("\n")
            return(o)
        if(check_d(pos)):
            board(v)
            print("Game Drawn!")
            print("\n")
            return('D')
        if(o=='X'):
            o='O'
        else:
            o='X'
p1=input("Enter The Name of Player 1 : ")
print()
p2=input("Enter The Name of Player 2 : ")
print()
s={p1:0,p2:0}
pc={'X':"",'O':""}
scoreboard(s)
cur=p1
while(True):
    print("{}'s Turn".format(cur))
    print("--------------------------------")
    print("Enter 1 for X")
    print("Enter 2 for O")
    print("Enter 3 to Quit")
    try:
        c=int(input())   
    except ValueError:
        print("Wrong Input! Try Again\n")
        continue
    o=''
    if(c==1):
        o='X'
        pc['X']=cur
        if(cur==p1):
            pc['O']=p2
        else:
            pc['O']=p1
    elif(c==2):
        o='O'
        pc['O']=cur
        if(cur==p1):
            pc['X']=p2
        else:
            pc['X']=p1
    elif(c==3):
        print("Final Scores : ")
        scoreboard(s)
        break
    else:
        print("Wrong Choice! Try Again\n")
    w=game(o,pc)
    if(w!='D'):
        pw=pc[w]
        s[pw]+=1
    scoreboard(s)
    if(cur==p1):
        cur=p2
    else:
        cur=p1
    
