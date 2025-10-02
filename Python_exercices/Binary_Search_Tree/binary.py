# Create a binary search tree using only functions and recursion (no classes).
# The implementation should include the construction 
# of the tree and the preorder traversal.


def pre_order(tree,level=0):
   if tree == []:
       return
   print(f'level {level} -> {str(tree[0])}') # root
   pre_order(tree[1],level + 1) # left son
   pre_order(tree[2],level + 1) #right son

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