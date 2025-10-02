# Represent an undirected and weighted graph.
# The graph representation will be as follows:
# Use a dictionary where keys are nodes and values are lists of tuples,
# each tuple containing an adjacent node and the edge weight.
#
# Now, display all nodes with their adjacencies and the weights of the edges.
#(number) -> nodes  [number] -> weight 
'''
     (1)
`[10]/``\[30]`
   (2)   (4)
`[20]\``/[10]`
      (3)
'''

def show_graph(graph):
    if len(graph) == 0:
        print('Graph is null')
        return
    for node,edges in graph.items():
         for dest,weight in edges:
             print(f'({node}) -> ({dest}) -> with weight {weight}')

graph={
    1:[(2,10),(4,30)],
    2:[(1,10),(3,20)],
    3:[(2,20),(4,10)],
    4:[(1,30),(3,10)],
}
show_graph(graph)