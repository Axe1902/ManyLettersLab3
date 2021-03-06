from MyQueue import Queue


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
        for j in range(n - same_peak, len(graph1)):
            if graph1[n - same_peak + i][j] == 0:
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


def depth_first_search_matrix(graph, visits, node):
    print(node+1)
    visits[node] = 1
    for j in range(len(graph)):
        if graph[node][j] == 1 and visits[j] == 0:
            depth_first_search_matrix(graph, visits, j)


def depth_first_search_line(graph, visits, node):
    print(node+1)
    visits[node] = 1
    for j in graph[node]:
        if visits[j[0]-1] == 0:
            depth_first_search_line(graph, visits, j[0]-1)


def depth_first_search_stack(graph, visits, node):
    stack = [node]
    while len(stack) > 0:
        item = stack.pop()
        if visits[item] == 0:
            visits[item] = 1
            print(item+1)
            for i in range(len(graph[item])-1, -1, -1):
                if graph[item][i] == 1:
                    stack.append(i)


def bfs_matrix(graph, visits, node):
    queue = [node]
    while len(queue) > 0:
        item = queue.pop(0)
        visits[item] = 1
        print(item+1)
        for i in range(len(graph)):
            if graph[item][i] == 1 and visits[i] == 0:
                queue.append(i)
                visits[i] = 1


def bfs_matrix_real(graph, visits, node):
    queue = Queue()
    queue.add(node)
    while queue.len != 0:
        item = queue.pop()
        visits[item] = 1
        print(item+1)
        for i in range(len(graph)):
            if graph[item][i] == 1 and visits[i] == 0:
                queue.add(i)
                visits[i] = 1


def bfs_line(graph, visits, node):
    queue = [node]
    while len(queue) > 0:
        item = queue.pop(0)
        visits[item] = 1
        print(item+1)
        for i in graph[item]:
            if visits[i[0]-1] == 0:
                queue.append(i[0]-1)
                visits[i[0]-1] = 1


def bfsd_matrix(graph, dist, node):
    queue = [node]
    while len(queue) > 0:
        item = queue.pop(0)
        dist[node] = 0
        print(item+1)
        for i in range(len(graph)):
            if graph[item][i] == 1 and dist[i] == -1:
                queue.append(i)
                dist[i] = dist[item] + 1
    print(dist)


def bfsd_matrix_real(graph, dist, node):
    queue = Queue()
    queue.add(node)
    while queue.len != 0:
        item = queue.pop()
        dist[node] = 0
        print(item+1)
        for i in range(len(graph)):
            if graph[item][i] != 0 and dist[i] > dist[item] + graph[item][i]:
                queue.add(i)
                dist[i] = dist[item] + graph[item][i]
    print(dist)


def bfsd_incMatrix_real(graph, edge, dist, node):
    queue = Queue()
    queue.add(node)
    while queue.len != 0:
        item = queue.pop()
        dist[node] = 0
        print(item+1)
        for i in range(len(edge)):
            if item != edge[i][1]:
                if graph[item][i] != 0 and dist[edge[i][1]] > dist[item] + graph[item][i]:
                    queue.add(edge[i][1])
                    dist[edge[i][1]] = dist[item] + graph[item][i]
            elif item == edge[i][1]:
                if graph[item][i] != 0 and dist[edge[i][0]] > dist[item] + graph[item][i]:
                    queue.add(edge[i][0])
                    dist[edge[i][0]] = dist[item] + graph[item][i]
    print(dist)


def bfsd_line(graph, dist, node):
    queue = [node]
    while len(queue) > 0:
        item = queue.pop(0)
        dist[node] = 0
        print(item+1)
        for i in graph[item]:
            if dist[i[0]-1] == -1:
                queue.append(i[0]-1)
                dist[i[0]-1] = dist[item] + 1
    print(dist)


def dfsd_matrix(graph, dist, node):
    stack = [node]
    dist[node] = 0
    while len(stack) > 0:
        item = stack.pop()
        print(item + 1)
        for i in range(len(graph[item]) - 1, -1, -1):
            if graph[item][i] == 1 and dist[i] == -1:
                dist[i] = dist[item] + 1
                stack.append(i)


def dfsd_line(graph, dist, node):
    stack = [node]
    while len(stack) > 0:
        item = stack.pop()
        dist[node] = 0
        print(item + 1)
        for i in range(len(graph[item]) - 1, -1, -1):
            if graph[item][i][1] == 1 and dist[graph[item][i][0]-1] == -1:
                dist[graph[item][i][0]-1] = dist[item] + 1
                stack.append(graph[item][i][0]-1)


def search_peripheral_or_central_node(eccentricity, property, massOfNode):
    for i in range(len(eccentricity)):
        if eccentricity[i] == property:
            massOfNode.append(i+1)


def degree_of_node(graph, degrees, n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                degrees[i] += 1
