import random


def generator_matrix(graph, n):
    for i in range(n):
        a = []
        for j in range(n):
            a.append(0)
        graph.append(a)

    for i in range(n):
        for j in range(n):
            if (graph[i][j] == 0) and (i != j):
                graph[i][j] = random.randint(0, 1)
                graph[j][i] = graph[i][j]


def generator_w_matrix(graph, n, maxNumber):
    for i in range(n):
        a = [0 for i in range(n)]
        graph.append(a)

    for i in range(n):
        for j in range(n):
            if (graph[i][j] == 0) and (i != j):
                graph[i][j] = random.randint(0, maxNumber)
                graph[j][i] = graph[i][j]


def generator_w_orientation_matrix(graph, n, maxNumber):
    for i in range(n):
        a = [0 for i in range(n)]
        graph.append(a)

    for i in range(n):
        for j in range(n):
            if (graph[i][j] == 0) and (i != j):
                graph[i][j] = random.randint(0, maxNumber)


def generator_incident_matrix(graph, edge, incGraph, visits, n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and i != j and visits[j] == 0:
                b = []
                b.append(i)
                b.append(j)
                edge.append(b)
        visits[i] = 1
    for i in range(n):
        a = [0 for _ in range(len(edge))]
        incGraph.append(a)
    print(edge)

    for j in range(len(edge)):
        incGraph[edge[j][0]][j] = graph[edge[j][0]][edge[j][1]]
        incGraph[edge[j][1]][j] = graph[edge[j][0]][edge[j][1]]
    for j in range(n):
        print(incGraph[j])
    print()


def generator_line(line_data, graph, n):
    for i in range(n):
        line = []
        for j in range(n):
            if (graph[i][j] != 0):
                a = []
                a.append(j+1)
                a.append(graph[i][j])
                line.append(a)
        print("Вершина №%d " % (i + 1), line)
        line_data.append(line)
    print()


def print_matrix(graph, min, n):
    a = []
    for i in range(min, n):
        a.append(i+1)
    print("  ", end=' ')
    for i in range(n - min):
        print(a[i], end='  ')
    print("")
    for i in range(n - min):
        print("%d" % (a[i]), graph[i])
    print()
