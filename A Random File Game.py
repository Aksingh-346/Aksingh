def listcheck():
    global isplayer1turn
    print("\n",lst)
    print("\n","P1 ->",P1,"\t","P2 ->",P2)
    if len(lst) == 0:
        isplayerturn = 0
        print("Game over")
        if P1 > P2:
            print("PLAYER 1 WINS")
        elif P1 < P2:
            print("PLAYER 2 WINS")
        elif P1 == P2:
            print("DRAW")
        
    elif isplayer1turn == 'j':
        isplayer1turn = 0
        
    elif isplayer1turn == 0:
        isplayer1turn = 'j'
        


def calc(x,y):
    if isplayer1turn == 'j':
        if y == 1:
            global P1
            global P2
            P1 += x
            listcheck()
        elif y == 2:
            P2 += x
            listcheck()
    elif isplayer1turn == 0:
        if y == 2:
            P2 += x
            listcheck()
        elif y == 1:
            P1 += x
            listcheck() 

def inpt():
    if isplayer1turn == 'j':
        print("\nPlayer 1 turn")
    elif isplayer1turn == 0:
        print("\nPlayer 2 turn")
    inp1 = int(input("Pick a no.: "))
    if inp1 in lst:
        lst.pop(lst.index(inp1))
    else:
        print("Choose a no. from the list given")
        inpt()
    print("1. Player (1)\n2. Player (2)")
    inp2 = int(input("(1)/(2): "))
    calc(inp1,inp2)
   

lst = [-1,2,4,-9,10]
print("A RANDOM FILE GAME")
print("1. Start")
print("2. Exit")
input1 = int(input("Enter your choice: "))

if input1 == 1:
    print("\n",lst)
    P1 = 0
    P2 = 0
    isplayer1turn = 'j'
    for i in range(len(lst)):
        inpt()
    
else:
    print("Logging out...")
    print("")
    
