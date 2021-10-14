import Graph
import Operations

n = 5
graphA = []

Graph.generator_matrix(graphA, n)
Graph.print_matrix(graphA, 0, n)


print("Выберете какие две вершины вы хотите отождествить: ")
peak1 = int(input())
peak2 = int(input())

Operations.identification_peak(graphA, peak1, peak2, n)
Operations.print_newGraph(graphA, peak2, n)


graphB = []

Graph.generator_matrix(graphB, n)
Graph.print_matrix(graphB, 0, n)

print("Выберете между какими двумя вершинами вы хотите стянуть ребро: ")
peak1 = int(input())
peak2 = int(input())

Operations.contraction_edge(graphB, peak1, peak2, n)
Operations.print_newGraph(graphB, peak2, n)


graphC = []

Graph.generator_matrix(graphC, n)
Graph.print_matrix(graphC, 0, n)

print("Выберете какую вершину расщепить: ")
peak = int(input())

Operations.copy_peak(graphC, peak, n)
Graph.print_matrix(graphC, 0, n+1)
