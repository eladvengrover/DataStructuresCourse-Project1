import avl_template_new

lst = avl_template_new.AVLTreeList()
lst.insert(0, "a")
lst.delete(0)
print(lst.getRoot())
lst.insert(1, "b")
lst.insert(2, "c")
lst.insert(3, "d")
lst.insert(4, "e")
lst.insert(5, "f")
lst.insert(6, "x")
lst.insert(2, "y")
lst.insert(4, "z")
print(lst)
lst.delete(0)
lst.delete(0)
lst.delete(1)
lst.delete(1)
lst.delete(2)
lst.delete(2)
print(lst)
print(lst.last_node.getValue())
print(lst.first_node.getValue())