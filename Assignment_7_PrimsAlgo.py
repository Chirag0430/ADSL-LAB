inf = 999999
N = int(input("Enter the number of vertices: "))

G = []

for i in range(N):
    row = list(map(int, input("Enter the row for vertex " + str(i) + ": ").split()))
    G.append(row)

visited_node = [0] * N
no_edge = 0

visited_node[0] = True
# print for edge and weight

while (no_edge < N - 1):

    minimum = inf
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
