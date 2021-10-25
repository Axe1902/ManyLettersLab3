import sys
import Operations
import Graph
#первое число номер задания, второе номер операции, последующие аргументы

if __name__ == '__main__':
    print(sys.argv)
    if int(sys.argv[1]) == 1:
        if int(sys.argv[2]) == 1:
            graph = []
            Graph.generator_matrix(graph, int(sys.argv[3]))
            Graph.print_matrix(graph, 0, int(sys.argv[3]))
            Operations.identification_peak(graph, int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[3]))
            Operations.print_newGraph(graph, int(sys.argv[5]), int(sys.argv[3]))
        elif int(sys.argv[2]) == 2:
            graph = []
            Graph.generator_matrix(graph, int(sys.argv[3]))
            Graph.print_matrix(graph, 0, int(sys.argv[3]))
            Operations.contraction_edge(graph, int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[3]))
            Operations.print_newGraph(graph, int(sys.argv[5]), int(sys.argv[3]))
        elif int(sys.argv[2]) == 3:
            graph = []
            Graph.generator_matrix(graph, int(sys.argv[3]))
            Graph.print_matrix(graph, 0, int(sys.argv[3]))
            Operations.copy_peak(graph, int(sys.argv[4]), int(sys.argv[3]))
            Graph.print_matrix(graph, 0, int(sys.argv[3]))

    elif int(sys.argv[1]) == 2:
        if int(sys.argv[2]) == 1:
            graph = []
            line_data = []
            Graph.generator_matrix(graph, int(sys.argv[3]))
            Graph.print_matrix(graph, 0, int(sys.argv[3]))
            Graph.generator_line(line_data, graph, int(sys.argv[3]))
            Operations.identification_peak_for_line(line_data, int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[3]))
            for i in range(int(sys.argv[3])):
                if (i == int(sys.argv[5]) - 1):
                    continue
                print("Вершина №%d " % (i + 1), (line_data[i]))
        elif int(sys.argv[2]) == 2:
            graph = []
            line_data = []
            Graph.generator_matrix(graph, int(sys.argv[3]))
            Graph.print_matrix(graph, 0, int(sys.argv[3]))
            Graph.generator_line(line_data, graph, int(sys.argv[3]))
            Operations.contraction_edge_for_line(line_data, graph, int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[3]))
            for i in range(int(sys.argv[3])):
                if (i == int(sys.argv[5]) - 1):
                    continue
                print("Вершина №%d " % (i + 1), (line_data[i]))

        elif int(sys.argv[2]) == 3:
            graph = []
            line_data = []
            Graph.generator_matrix(graph, int(sys.argv[3]))
            Graph.print_matrix(graph, 0, int(sys.argv[3]))
            Graph.generator_line(line_data, graph, int(sys.argv[3]))
            Operations.copy_peak_for_line(line_data, int(sys.argv[4]), int(sys.argv[3]))
            for i in range(int(sys.argv[3]) + 1):
                print("Вершина №%d " % (i + 1), (line_data[i]))

    elif int(sys.argv[1]) == 3:
        if int(sys.argv[2]) == 1:
            graph = []
            graph1 = []
            graph2 = []
            Graph.generator_matrix(graph1, int(sys.argv[3]))
            Graph.print_matrix(graph1, 0, int(sys.argv[3]))

            Graph.generator_matrix(graph2, int(sys.argv[4]))
            Graph.print_matrix(graph2, int(sys.argv[5]), int(sys.argv[6])) # 5 - мин.; 6 - макс

            Operations.unification_graphs(graph1, graph2, int(sys.argv[7])) # 7 - колво одинак вершин
            Graph.print_matrix(graph1, 0, int(sys.argv[6]))
        elif int(sys.argv[2]) == 2:
            graphA = []
            graphB = []

            Graph.generator_matrix(graphA, int(sys.argv[3]))
            Graph.print_matrix(graphA, 0, int(sys.argv[3]))
            print()

            Graph.generator_matrix(graphB, int(sys.argv[4]))
            Graph.print_matrix(graphB, 0, int(sys.argv[4]))
            print()

            graphC = []
            for i in range(int(sys.argv[3])):
                a = []
                for j in range(int(sys.argv[3])):
                    a.append(0)
                graphC.append(a)

            if int(sys.argv[3]) >= int(sys.argv[4]):
                sys.argv[3] = int(sys.argv[4])
            Operations.crossroads_graphs(graphA, graphB, graphC, int(sys.argv[3]))
            Graph.print_matrix(graphC, 0, len(graphC))
        elif int(sys.argv[2]) == 3:
            graphA = []
            graphB = []

            Graph.generator_matrix(graphA, int(sys.argv[3]))
            Graph.print_matrix(graphA, 0, int(sys.argv[3]))
            print()

            Graph.generator_matrix(graphB, int(sys.argv[4]))
            Graph.print_matrix(graphB, 0, int(sys.argv[4]))
            print()

            graphD = []
            for i in range(max(int(sys.argv[3]), int(sys.argv[4]))):
                a = []
                for j in range(max(int(sys.argv[3]), int(sys.argv[4]))):
                    a.append(0)
                graphD.append(a)

            if int(sys.argv[3]) >= int(sys.argv[4]):
                n = int(sys.argv[4])
            else:
                n = int(sys.argv[3])

            Operations.circle_sum_graphs(graphA, graphB, graphD, n)
            Graph.print_matrix(graphD, 0, len(graphD))
