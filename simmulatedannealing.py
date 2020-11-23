import random
import math
import copy
initial=[1,1,1,1]
T=1000
def heuristic(j):
    c=[0,0,0,0,0]
    e1=int(not j[0] or j[3])
    c.append(e1)
    e2=int(j[2] or j[1])
    c.append(e2)
    e3=int(not j[2] or not j[3])
    c.append(e3)
    e4=int(not j[3]or not j[1])
    c.append(e4)
    e5=int(not j[0]or not j[3])
    c.append(e5)
#     if(c.count(1)==5 and (j not in l)):
#         l.append(j)
    return c.count(1)

def movegen(i,t):
    index=random.randint(0,3)
    temp = copy.deepcopy(i)
    if temp[index]==0:
        temp[index]=1
    else:
        temp[index]=0
    print("At temperature ",t," state is ",temp) #printing child
    return temp

def prob(t,delta_e):
    value=(1/(1+math.exp(-delta_e/t)))
    return value
    
    
def funct(initial,T):
    l = []
    curr=initial
    while T>0:
        curr_h=heuristic(curr)
        nextstate=movegen(curr,T)
        next_h=heuristic(nextstate)
        delta_e=next_h-curr_h
        if (delta_e>0):
            #good move
            curr=nextstate
            #if next_h==5:
                #l.append(nextstate)
            
        else:
            #badmove
            g=random.uniform(0,1)
            if prob(T,delta_e)>g:
                #print(prob(nextstate,T,delta_e))
                #print(g)
                curr=nextstate
                
        if(heuristic(curr)==5):
            if(curr not in l):
                l = l + [curr]
                
        T=T-10
#     print(movegen(curr,0))
    
    if(T==0):
            movegen(curr,0)
            if heuristic(curr)==5 and movegen(curr,0) not in l:
                l.append(curr)            
    print("The possible solutions are: ",l)
    print(len(l))
funct(initial,T)
