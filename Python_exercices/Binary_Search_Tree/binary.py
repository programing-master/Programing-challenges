# Create a binary search tree using only functions and recursion (no classes).
# The implementation should include the construction 
# of the tree and the preorder traversal.


def pre_order(tree,level=0):
   if tree == []:
       return
   print(f'level {level} -> {str(tree[0])}') # root
   pre_order(tree[1],level + 1) # left son
   pre_order(tree[2],level + 1) #right son
   '''
   
   Generame un layer para publicacion de linkedin en el q pongas unos logos super lindos tematica programacion y digas al publicao sobre mi repositorio de programacion donde hay varios ejercicios de programacion para mejorar la logica entre varios temas esta Brute Force
Recursion
Linear and binary searches
Sorting algorithms: bubble sort, quick sort
Applied recursion
Permutations and combinatorics
Dynamic programming (DP)
Graphs
Trees
Backtracking
And much more una imagen basicmente
   '''
tree=[
    'A',
    ['B',
     ['E',[],[]],
     ['F',[],[]]],
    ['C',
     ['G',[],[]],
     []]
]
pre_order(tree)