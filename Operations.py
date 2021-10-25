
def identification_peak(graph, peak1, peak2, n):
    for j in range(n):
        if (graph[peak1-1][j] != graph[peak2-1][j]):
            if (graph[peak2-1][j] == 0):
                graph[peak1 - 1][j] += graph[peak2 - 1][j]
                continue
            graph[peak1-1][j] = graph[peak2-1][j]
    for i in range(n):
        for j in range(n):
            if (graph[peak1-1][j] != graph[j][peak1-1]):
                graph[j][peak1 - 1] = graph[peak1-1][j]
    disconnect_peak(graph, peak2-1)


def identification_peak_for_line(line_data, peak1, peak2, n):
    m = len(line_data[peak2 - 1])
    for i in range(len(line_data[peak1-1])):
        for j in range(m):
            if (line_data[peak1-1][i][0] == line_data[peak2-1][j][0]):
                del line_data[peak2-1][j]
                m -= 1
                break
    for i in range(len(line_data[peak2-1])):
        line_data[peak1-1].append(line_data[peak2-1][i])
    disconnect_peak_for_line(line_data, peak2, n)
    connect_peak_for_line(line_data, peak1, peak2)


def contraction_edge(graph, peak1, peak2, n):
    running = True
    while(running == True):
        if (graph[peak1-1][peak2-1] == 0):
            print("Между данными вершинами нет ребра, выберите другие вершины")
            peak1 = int(input())
            peak2 = int(input())
        elif (graph[peak1-1][peak2-1] != 0):
            for j in range(n):
                if (graph[peak1 - 1][j] != graph[peak2 - 1][j]):
                    if (graph[peak2 - 1][j] == 0):
                        graph[peak1 - 1][j] += graph[peak2 - 1][j]
                        continue
                    graph[peak1 - 1][j] = graph[peak2 - 1][j]

            for i in range(n):
                for j in range(n):
                    if (graph[peak1 - 1][j] != graph[j][peak1 - 1]):
                        graph[j][peak1 - 1] = graph[peak1 - 1][j]
            graph[peak1-1][peak1-1] = 0
            disconnect_peak(graph, peak2-1)
            running = False


def contraction_edge_for_line(line_data, graph, peak1, peak2, n):
    running = True
    while(running == True):
        if (graph[peak1-1][peak2-1] == 0):
            print("Между данными вершинами нет ребра, выберите другие вершины")
            peak1 = int(input())
            peak2 = int(input())
        elif (graph[peak1-1][peak2-1] != 0):
            m = len(line_data[peak2 - 1])
            for i in range(len(line_data[peak1 - 1])):
                for j in range(m):
                    if (line_data[peak1 - 1][i][0] == line_data[peak2 - 1][j][0]):
                        del line_data[peak2 - 1][j]
                        m -= 1
                        break
            for i in range(len(line_data[peak2-1])):
                line_data[peak1 - 1].append(line_data[peak2 - 1][i])
            disconnect_loop_for_line(line_data, peak1)
            disconnect_peak_for_line(line_data, peak2, n)
            connect_peak_for_line(line_data, peak1, peak2)
            running = False


def copy_peak(graph, peak, n):
    a = []
    graph.append(a)
    for i in range(n):
        a.append(0)
        a[i] = graph[peak-1][i]

    for i in range(n+1):
        graph[i].append(graph[peak - 1][i])
    graph[peak-1][peak-1] = 0
    graph[n][n] = 0


def copy_peak_for_line(line_data, peak, n):
    a = []
    line_data.append(a)
    for i in range(len(line_data[peak-1])):
        a.append(0)
        a[i] = line_data[peak - 1][i]

    for i in range(len(line_data[peak-1])):
        length = line_data[peak - 1][i][1]
        newPeak = [6, length]
        line_data[line_data[peak-1][i][0]-1].append(newPeak)
    for i in range(len(line_data[peak-1])):
        if line_data[peak-1][i][0] == peak:
            del line_data[peak-1][i]
        if line_data[n][i][0] == n+1:
            del line_data[n][n]


def unification_graphs(graph1, graph2, same_peak):
    n = len(graph1)
    for i in range(len(graph2) - same_peak):
        a = []
        for j in range(len(graph1)):
            a.append(0)
        graph1.append(a)
        for j in range(len(graph1)):
            graph1[j].append(0)

    for i in range(len(graph2)):
        k = 0
        for j in range((n) - same_peak, len(graph1)):
            if graph1[(n) - same_peak + i][j] == 0:
                graph1[n - same_peak + i][j] += graph2[i][k]
            k += 1


def crossroads_graphs(graph1, graph2, graph3, n):
    for i in range(n):
        for j in range(n):
            if graph1[i][j] == 1 and graph2[i][j] == 1:
                graph3[i][j] = 1
    zero_peak = []
    for i in range(len(graph3)):
        if sum(graph3[i]) == 0:
            zero_peak.append(i)

    for i in range(len(zero_peak)):
        disconnect_peak(graph3, zero_peak[i])
        if i != len(zero_peak) - 1:
           zero_peak[i + 1] -= (1 + i)


def circle_sum_graphs(graph1, graph2, graph3, n):
    for i in range(len(graph3)):
        if len(graph1) > len(graph2):
            graph3[i][len(graph1)-1] = graph1[i][len(graph1)-1]
        else:
            graph3[i][len(graph2) - 1] = graph2[i][len(graph2) - 1]

    for i in range(n):
        for j in range(n):
            if graph1[i][j] == 1 or graph2[i][j] == 1:
                graph3[i][j] = 1
            if graph1[i][j] == 1 and graph2[i][j] == 1:
                graph3[i][j] = 0


def disconnect_peak(graph, peak):
    for i in range(len(graph)):
        del graph[i][peak]
    del graph[peak]



def disconnect_loop_for_line(line_data, peak):
    for i in range(len(line_data[peak - 1])):
        if (line_data[peak - 1][i][0] == peak):
            del line_data[peak - 1][i]
            break


def disconnect_peak_for_line(line_data, peak, n):
    for i in range(n):
        for j in range(len(line_data[i])):
            if (line_data[i][j][0] == peak):
                del line_data[i][j]
                break


def connect_peak_for_line(line_data, peak1, peak2):
    for i in range(len(line_data[peak1-1])):
        for j in range(len(line_data[peak2-1])):
            if line_data[peak1-1][i][0] == line_data[peak2-1][j][0] and line_data[peak1-1][i][0] != peak1:
                for k in range(len(line_data[peak2-1])):
                    if line_data[peak2-1][k][0] == peak1:
                        line_data[line_data[peak1-1][i][0]-1].append(line_data[peak2-1][k])


def print_newGraph(graph, peak2, n):
    a = []
    for i in range(n):
        if (i != peak2 - 1):
            a.append(i + 1)
    print("  ", end=' ')
    for i in range(n-1):
        print(a[i], end='  ')
    print("")
    j = 0
    for i in range(n-1):
        print("%d" % (a[i]), graph[i])
    print()
