import avl_template_new

lst = avl_template_new.AVLTreeList()
lst.insert(0, "a")
lst.insert(1, "b")
lst.insert(2, "c")
lst.insert(3, "d")
lst.insert(4, "e")
lst.insert(5, "f")
print(lst)
lst.insert(2, "y")
print(lst)