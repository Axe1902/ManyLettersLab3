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
