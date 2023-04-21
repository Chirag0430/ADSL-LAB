INF=99

N=5

G=[[0,19,5,0,0],
   [19,0,5,9,2],
   [5,5,0,1,6],
   [0,9,1,0,1],
   [0,2,6,1,0]]

visited_node = [0,0,0,0,0]
no_edge=0
visited_node[0]= True

print("Edge : Weight\n")
while (no_edge < N - 1):
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if visited_node[m]:
            for n in range(N):
                if ((not visited_node[n]) and G[m][n]):

                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    visited_node[b] = True
    no_edge += 1
