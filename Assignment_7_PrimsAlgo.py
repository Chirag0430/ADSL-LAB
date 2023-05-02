INF = 99

nodes = int(input("Enter the number of nodes: "))

graph = []
print("Enter the graph row wise :")
for i in range(nodes):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [0] * nodes
no_edge = 0
visited[0] = True

print("Edge : Weight\n")
while (no_edge < nodes - 1):
    minimum = INF
    a = 0
    b = 0
    for m in range(nodes):
        if visited[m]:
            for n in range(nodes):
                if ((not visited[n]) and graph[m][n]):

                    if minimum > graph[m][n]:
                        minimum = graph[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(graph[a][b]))
    visited[b] = True
    no_edge += 1
