import Graph
import Operations
import sys


if __name__ == '__main__':
    print(sys.argv)
    n = int(input("Введите размер матрицы: "))
    if int(sys.argv[1]) == 1:  # Взвешенный
        if int(sys.argv[2]) == 1:  # Ориентированный
            graph = []
            Graph.generator_w_orientation_matrix(graph, n, 3)
            Graph.print_matrix(graph, 0, n)

            Dist = [1000 for _ in range(n)]
            node = int(input("Введите номер вершины: "))
            Operations.bfsd_matrix_real(graph, Dist, node - 1)
            print()

        elif int(sys.argv[2]) == 2:  # Неориентированный
            graph = []
            Graph.generator_w_matrix(graph, n, 3)
            Graph.print_matrix(graph, 0, n)

            Dist = [1000 for _ in range(n)]
            node = int(input("Введите номер вершины: "))
            Operations.bfsd_matrix_real(graph, Dist, node - 1)
            print()

    elif int(sys.argv[1]) == 2:  # Невзвешенный
        if int(sys.argv[2]) == 1:
            graph = []
            Graph.generator_w_orientation_matrix(graph, n, 1)
            Graph.print_matrix(graph, 0, n)

            Dist = [1000 for _ in range(n)]
            node = int(input("Введите номер вершины: "))
            Operations.bfsd_matrix_real(graph, Dist, node - 1)
            print()

        elif int(sys.argv[2]) == 2:
            graph = []
            Graph.generator_w_matrix(graph, n, 1)
            Graph.print_matrix(graph, 0, n)

            Dist = [1000 for _ in range(n)]
            node = int(input("Введите номер вершины: "))
            Operations.bfsd_matrix_real(graph, Dist, node - 1)
            print()
