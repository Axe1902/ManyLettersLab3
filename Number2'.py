import Graph
import Operations

n = 5
graphA = []
line_data = []

Graph.generator_matrix(graphA, n)
Graph.print_matrix(graphA, 0, n)
Graph.generator_line(line_data, graphA, n)


print("Выберете какие две вершины вы хотите отождествить: ")
peak1 = int(input())
peak2 = int(input())

Operations.identification_peak_for_line(line_data, peak1, peak2, n)

for i in range(n):
    if (i == peak2-1):
        continue
    print("Вершина №%d " % (i + 1), (line_data[i]))


graphB = []
line_data_B = []

Graph.generator_matrix(graphB, n)
Graph.print_matrix(graphB, 0, n)
Graph.generator_line(line_data_B, graphB, n)

print("Выберете между какими двумя вершинами вы хотите стянуть ребро: ")
peak1 = int(input())
peak2 = int(input())

Operations.contraction_edge_for_line(line_data_B, graphB, peak1, peak2, n)

for i in range(n):
    if (i == peak2-1):
        continue
    print("Вершина №%d " % (i + 1), (line_data_B[i]))


graphC = []
line_data_C = []

Graph.generator_matrix(graphC, n)
Graph.print_matrix(graphC, 0, n)
Graph.generator_line(line_data_C, graphC, n)

print("Выберете какую вершину расщепить: ")
peak = int(input())

Operations.copy_peak_for_line(line_data_C, peak, n)
for i in range(n+1):
    print("Вершина №%d " % (i + 1), (line_data_C[i]))
