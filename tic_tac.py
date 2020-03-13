initial=("X","O","X",
         "O"," ","O",
         "X"," "," ")
x_win=1
o_win=-1
draw=0

import math
infinity= math.inf
count=0
def printAll(A):
    d=0
    for i in A:
        if(depth_holder[A.index(i)]==d):
            print("\n<---------------Depth {}------------------>\n".format(depth_holder[A.index(i)]))
            d=d+1
        text=getText(i)
        print(" _______________________________")
        print("| "+i[0]+" | "+i[1]+" | "+i[2]+" |"+"        Node Value"+"|")
        print("|---|---|---|                  |")
        print("| "+i[3]+" | "+i[4]+" | "+i[5]+" |"+"            "+str(cost[A.index(i)])+"     |")
        print("|---|---|---|                  |")
        print("| "+i[6]+" | "+i[7]+" | "+i[8]+" |"+str(text)+"|")
        print("|___|___|___|__________________|")
       
def getText(Node):
    if isTerminal(Node)=="Draw":
        return "         Game Draw"
    elif isTerminal(Node)=="X":
        #count=count+1
        return "       Winner is X"
    elif isTerminal(Node)=="O":
        return "       Winner is O"
    else: return "                  "
def isTerminal(Node):
    winner=0
    if (Node[0]==Node[1]==Node[2] or  Node[0]==Node[3]==Node[6]):
        winner=Node[0]
    elif (Node[2]==Node[5]==Node[8] or Node[6]==Node[7]==Node[8]):
        winner=Node[8]
    elif(Node[3]==Node[4]==Node[5] or Node[1]==Node[4]==Node[7] or Node[2]==Node[4]==Node[6] or Node[0]==Node[4]==Node[8]):
        winner=Node[4]
    elif Node.count(" ")==0:winner="Draw"
    if winner==" ":winner=0
    
    return winner
def place(Node,index,turn):
    Node=list(Node)
    Node[index]=turn
    return Node
def findChilds(Node,turn):
    childs=[]
    for i in range(9):
        if Node[i]==" ":
            childs.append(place(Node,i,turn))
    return childs  
explored=[]
depth_holder=[]
terminals=[]
tu="O"
def minimax(start):
    start=list(start)
    queue = [start]
    depth=[0]
    while queue:
            node = queue.pop(0)
            d=depth.pop(0)
            explored.append(node)
            depth_holder.append(d)
            if d%2==0:tu="X"
            else: tu="O"
            if (isTerminal(node)==0):
                neighbours = findChilds(node,tu)
                for neighbour in neighbours:
                    queue.append(neighbour)
                    depth.append(d+1)
            else:
                terminals.append(node)
    return explored

def backtrack(Node):
    for i in range(de.index(Node)-1,-1,-1):
        if depth_holder[i]%2==0:tu="X"
        else: tu="O"
        if Node in findChilds(de[i],tu):
            if depth_holder[i]%2==0:
                cost[i]=max(cost[i],cost[de.index(Node)])
            else:
                cost[i]=min(cost[i],cost[de.index(Node)])
            backtrack(de[i])
cost=[]
def setCost(path):
    
    for i in range(len(path)):
        if(isTerminal(path[i])==0):
            if depth_holder[i]%2==0:
                cost.append(-infinity)
            else:
                cost.append(infinity)
        elif isTerminal(path[i])=="Draw":
           cost.append(draw)
        elif isTerminal(path[i])=="X":
           cost.append(x_win)
        else:
           cost.append(o_win)
de=minimax(initial)
setCost(de)
for t in terminals:
    backtrack(t)

printAll(de)
count=0
coi=0
dr=0
for t in terminals:
    if(isTerminal(t)=="X"):
        count=count+1
    elif (isTerminal(t)=="O"):
        coi=coi+1
    elif(isTerminal(t)=="Draw"):
        dr=dr+1
print("________________________________________________________")
print("No Of Ways X Win ", count)
print("No Of Ways X Loose ", coi)
print("No Of Draws ", dr)
