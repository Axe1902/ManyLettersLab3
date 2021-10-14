import Graph

n = 5
graphA = []
line_data_A = []
graphB = []
line_data_B = []

Graph.generator_matrix(graphA, n)
Graph.print_matrix(graphA, 0, n)
Graph.generator_line(line_data_A, graphA, n)
print()

Graph.generator_matrix(graphB, n)
Graph.print_matrix(graphB, 0, n)
Graph.generator_line(line_data_B, graphB, n)
