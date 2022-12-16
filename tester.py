import avl_template_new

lst = avl_template_new.AVLTreeList()
lst.insert(0, "x")
lst.insert(1, "y")
lst.insert(2, "z")
lst.insert(3, "f")
lst.insert(4, "e")
lst.insert(5, "d")
lst.insert(6, "c")
lst.insert(7, "b")
lst.insert(8, "a")
x = lst.sort()
x_lst = x.listToArray()
print(x)
for i in range(10000):
    y = x.permutation()
    y_lst = y.listToArray()
    for k in y_lst:
        if k not in x_lst:
            print("ERROR!!!")







# lst.delete(0)
# lst.delete(0)
# lst.delete(1)
# lst.delete(1)
# lst.delete(2)
# lst.delete(2)
# print(lst)
# print(lst.last_node.getValue())
# print(lst.first_node.getValue())