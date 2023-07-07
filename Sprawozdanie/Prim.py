
G = [[0,1,0,0,4,8,0,0],
     [1,0,2,0,0,6,6,0],
     [0,2,0,3,0,0,2,0],
     [0,0,3,0,0,0,1,4],
     [4,0,0,0,0,5,0,0],
     [8,6,0,0,5,0,1,0],
     [0,6,2,1,0,1,0,1],
     [0,0,0,4,0,0,1,0]]
Q=[]
n=len(G)
visited=[False]*n
T=["null"]*(n-1)
element=0
u=0


visited[u]=True
while True:
    i=u
    for j in range(n):
        w=G[i][j]
        if w==0:  continue
        v=j
        if visited[v]==False:
            Q.append((u,v,w))


    Q=sorted(Q,key=lambda x: x[2])
    l=0
    while True:

        (u,v,w)=Q[l]
        l+=1
        if visited[v]==False:
            break

    T[element]=(u,v,w)
    element+=1
    visited[v]=True
    u=v
    del Q[l-1]
    if element==n-1: break
    i+=1
    

print(T)
    
