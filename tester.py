import random

import avl_template_new

for i in range(1, 11):
    lst = avl_template_new.AVLTreeList()
    n = 1500 * (2 ** i)
    #n = 50 * i
    insert_count = 0
    delete_count = 0
    for j in range(n):
        random_position = random.randint(0, lst.length())
        insert_count += lst.insert(random_position, str(j))
    for j in range(n):
        random_position = random.randint(0, lst.length() - 1)
        delete_count += lst.delete(random_position)
    print("i = ", i, ", insert_count = ", insert_count, ", delete_count = ", delete_count)



# lst.delete(0)
# lst.delete(0)
# lst.delete(1)
# lst.delete(1)
# lst.delete(2)
# lst.delete(2)
# print(lst)
# print(lst.last_node.getValue())
# print(lst.first_node.getValue())