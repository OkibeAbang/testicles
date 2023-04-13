from build.lib.Datastructures.trees.BST import BST, TNode
from build.lib.Datastructures.trees.AVL import AVL, TNode






print("\nTesting AVL...")

# create an AVL tree
#root_node = TNode(7)
avl_tree = AVL()

# insert some values
avl_tree.insert(5)
avl_tree.insert(3)
avl_tree.insert(7)
avl_tree.insert(1)
avl_tree.insert(9)

# print the tree in order
avl_tree.print_in_order()

# print the tree using breadth-first traversal
avl_tree.print_bf()

# test search function
test1 = avl_tree.search(9)  
test2 = avl_tree.search(3)  

if test1:
    print("Value found:", test1.val)
else:
    print("Value not found")

if test2:
    print("Value found:", test2.val)
else:
    print("Value not found")

# test delete function
avl_tree.delete(3)
avl_tree.delete(9)

# test search function again after deleting nodes
test3 = avl_tree.search(3)  
test4 = avl_tree.search(9)  

if test3:
    print("Value found:", test3.val)
else:
    print("Value not found")

if test4:
    print("Value found:", test4.val)
else:
    print("Value not found")








print("\nTesting BST...")

# create a new BST object
root_node = TNode(5)
bst = BST(root_node)

# insert some values
bst.insert(5)
bst.insert(3)
bst.insert(6)
bst.insert(1)
bst.insert(9)

# print the tree in order and breadth-first order
bst.print_in_order()
bst.print_bf()

# search for a value
result = bst.search(7)
if result:
    print("Value found:", result.val)
else:
    print("Value not found")

# delete a value
bst.delete(3)

# print the tree again
bst.print_in_order()
bst.print_bf()




