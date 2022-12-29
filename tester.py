import collections
import random
import time
import linked_list
import avl_template_new



for i in range(1, 11):
    lst = avl_template_new.AVLTreeList()
    # lst = collections.deque()
    # lst = list()
    n = 1500 * i
    insert_count = 0
    start = time.time()
    for j in range(n):
        # random_position = random.randint(0, len(lst))
        lst.insert(0, str(j))
        # lst.append(str(j))
    end = time.time()
    print((end - start) / n)

# lst = avl_template_new.AVLTreeList()
# lst.insert(0, None)
# lst.insert(0, "a")
# lst.insert(0, "b")
# lst.insert(0, "c")
# lst.insert(0, "d")
# lst.insert(0, None)
# lst.insert(0, None)
# lst.insert(0, None)
# lst.insert(0, None)
# print(lst.listToArray())
# print(lst.sort().listToArray())
#
# lst2 = [None, None]
# print(lst2)
# lst.delete(0)
# lst.delete(1)
# lst.delete(1)
# lst.delete(2)
# lst.delete(2)
# print(lst)
# print(lst.last_node.getValue())
# print(lst.first_node.getValue())