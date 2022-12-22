# username - graiver1
# id1      - 206363368
# name1    - Shahar Graiver
# id2      - 209008135
# name2    - Elad Vengrover


"""A class representing a node in an AVL tree"""
import random


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1 if value is None else 0
        self.isReal = False if value is None else True
        self.size = 1 if self.isReal else 0

    """returns the left child
    
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height if self.isRealNode() else -1

    """returns the balance factor
    
    @pre: self.isRealNode() is True   
    @rtype: int
    @returns: the balance factor of self
    """
    def getBalanceFactor(self):
        return self.getLeft().getHeight() - self.getRight().getHeight()

    """returns the size

    @rtype: int
    @returns: the size of self, 0 if the node is virtual
    """

    def getSize(self):
        return self.size

    """sets left child and sets node's parent accordingly.
    
    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node
        node.setParent(self)

    """sets right child and sets node's parent accordingly.
    
    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node
        node.setParent(self)

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value

    """sets the height  of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h

    """sets the size of the node

        @type s: int
        @param s: the size
        """

    def setSize(self, s):
        self.size = s

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.isReal

    """returns whether self is a leaf 

        @rtype: bool
        @returns: True if self is a leaf, False otherwise.
        """
    def isLeaf(self):
        return self.getHeight() == 0

    """set children to be virtual nodes """
    def add_virtual_children(self):
        self.setLeft(AVLNode(None))
        self.setRight(AVLNode(None))

    """calculates self's height according to its children
    @pre: self.isRealNode() is True
    @rtype: int
    @returns: the height of self
    """
    def calc_height(self):
        return max(self.getLeft().getHeight(), self.getRight().getHeight()) + 1

    """calculates self's size according to its children
    
    @pre: self.isRealNode() is True
    @rtype: int
    @returns: the size of self
    """
    def calc_size(self):
        return self.getLeft().getSize() + self.getRight().getSize() + 1

    """sets height and size of self according to its children
    
    @pre: self.isRealNode() is True
    """
    def fix_node_height_and_size(self):
        self.setSize(self.calc_size())
        self.setHeight(self.calc_height())

    """returns the predecessor of node in the list

    @type node: AVLNode
    @param node: node in the list
    @rtype: AVLNode
    @returns: the predecessor of node in the list
    """
    def get_predecessor(self):
        if self.getLeft().isRealNode():
            return self.getLeft().get_last_node()
        node = self
        parent_node = node.getParent()
        while parent_node is not None and node == parent_node.getLeft():  # node is Parent_node left child
            node = parent_node
            parent_node = node.getParent()
        return parent_node

    """returns the successor of node in the list

    @type node: AVLNode
    @param node: node in the list
    @rtype: AVLNode
    @returns: the successor of node in the list
    """

    def get_successor(self):
        if self.getRight().isRealNode():
            return self.getRight().get_first_node()
        node = self
        parent_node = node.getParent()
        while parent_node is not None and node == parent_node.getRight():  # node is Parent_node right child
            node = parent_node
            parent_node = node.getParent()
        return parent_node

    """returns the first node in the sub-tree rooted with self

    @rtype: AVLNode
    @returns: the first node in the sub-tree rooted with self
    """
    def get_first_node(self):
        node = self
        while node.getLeft().isRealNode():
            node = node.getLeft()
        return node

    """returns the last node in the sub-tree rooted with self

     @rtype: AVLNode
     @returns: the last node in the sub-tree rooted with self
     """
    def get_last_node(self):
        node = self
        while node.getRight().isRealNode():
            node = node.getRight()
        return node

    """update self fields and fixes its height and size accordingly

     @type: AVLNode
     @param: a node represents the new right child of self
     @type: AVLNode
     @param: a node represents the new left child of self
     @type: AVLNode
     @param: a node represents the new parent of self
     """
    def update_node_fields(self, right_child, left_child, parent):
        self.setRight(right_child)
        self.setLeft(left_child)
        self.setParent(parent)
        self.fix_node_height_and_size()


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.size = 0
        self.root = None
        self.first_node = None
        self.last_node = None

    """update self fields

    @type root: AVLNode 
    @param root: a node represents the new root of self
    @type first_node: AVLNode
    @param first_node: a node represents the new first_node of self
    @type last_node: AVLNode
    @param last_node: a node represents the new last_node of self
    """
    def update_tree_fields(self, root, first_node, last_node):
        self.set_root(root)
        self.set_size(0 if root is None else root.getSize())
        self.set_first_node(first_node)
        self.set_last_node(last_node)

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.getSize() == 0

    """"retrieves the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length() 
    @param i: index in the list
    @rtype: AVLNode
    @returns: the i'th item in the list
    """

    def retrieve_node(self, i):
        def retrieve_rec(node, k):
            r = node.getLeft().getSize() + 1
            if r == k:
                return node
            elif r > k:
                return retrieve_rec(node.left, k)
            return retrieve_rec(node.right, k - r)

        return retrieve_rec(self.getRoot(), i + 1)

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        if 0 <= i <= self.size - 1:
            return self.retrieve_node(i).getValue()
        return None

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        node = AVLNode(val)
        node.add_virtual_children()
        if self.empty():
            self.update_tree_fields(node, node, node)
            return 0
        if i == self.length():
            self.get_last_node().setRight(node)
            self.set_last_node(node)
        else:
            if i == 0:
                self.set_first_node(node)  # Updating self.first
            prev_i_node = self.retrieve_node(i)
            if prev_i_node.getLeft().isRealNode() is False:  # Case 1: prev_node doesn't have left son
                prev_i_node.setLeft(node)
            else:  # Case 2: prev_node has left son
                node_predecessor = prev_i_node.get_predecessor()
                node_predecessor.setRight(node)

        return self.fix_the_tree(node, False)

    """Rebalancing the tree after insertion/deletion

    @type starting_node: AVLNode
    @param starting_node: The node to be insert or physically deleted
    @type insert_or_delete: int
    @param insert_or_delete: 1 if rebalancing after insertion, 2 if rebalancing after deletion 
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def fix_the_tree(self, starting_node, fix_to_the_root):
        rotations_count = 0
        y = starting_node.getParent()
        while y is not None:
            y_old_height = y.getHeight()
            y.setHeight(y.calc_height())
            balance_factor = y.getBalanceFactor()
            if abs(balance_factor) < 2 and y.getHeight() == y_old_height:
                break
            elif abs(balance_factor) < 2 and y.getHeight() != y_old_height:
                y = y.getParent()
                continue
            y_parent = y.getParent()
            rotations_count += self.perform_rotation(y)
            if fix_to_the_root is False:
                break
            y = y_parent
        self.fix_tree_nodes_height_and_sizes(starting_node)
        return rotations_count

    """performs rotation on bf_criminal according to its and its child's BF 

    @type bf_criminal: AVLNode
    @param bf_criminal: the node to be rotate
    """
    def perform_rotation(self, bf_criminal):
        if bf_criminal.getBalanceFactor() == 2:
            if bf_criminal.getLeft().getBalanceFactor() == -1:
                self.left_rotation(bf_criminal.getLeft())
                self.right_rotation(bf_criminal)
                return 2
            self.right_rotation(bf_criminal)
            return 1
        if bf_criminal.getRight().getBalanceFactor() == 1:
            self.right_rotation(bf_criminal.getRight())
            self.left_rotation(bf_criminal)
            return 2
        self.left_rotation(bf_criminal)
        return 1

    """performs left rotation on node_b and its right child and fixes its size and height 

    @type node_a: AVLNode
    @param node_a: the node to be rotate with his child
    """
    def left_rotation(self, node_a):
        node_b = node_a.getRight()
        node_a_parent = node_a.getParent()
        node_a.setRight(node_b.getLeft())
        node_b.setLeft(node_a)
        if node_a_parent is not None:
            if node_a_parent.getRight() == node_a:
                node_a_parent.setRight(node_b)
            else:
                node_a_parent.setLeft(node_b)
        else:
            node_b.setParent(None)
            self.set_root(node_b)

        node_a.fix_node_height_and_size()
        node_b.fix_node_height_and_size()

    """performs right rotation on node_b and its left child and fixes its size and height 

    @type node_b: AVLNode
    @param node_b: the node to be rotate with his child
    """
    def right_rotation(self, node_b):
        node_a = node_b.getLeft()
        node_b_parent = node_b.getParent()
        node_b.setLeft(node_a.getRight())
        node_a.setRight(node_b)
        if node_b_parent is not None:
            if node_b_parent.getRight() == node_b:
                node_b_parent.setRight(node_a)
            else:
                node_b_parent.setLeft(node_a)
        else:
            node_a.setParent(None)
            self.set_root(node_a)

        node_b.fix_node_height_and_size()
        node_a.fix_node_height_and_size()

    """fixes all nodes height and size from starting_node all the way to the root

    @type starting_node: AVLNode
    @param starting_node: the first node to fix its height and size
    """
    def fix_tree_nodes_height_and_sizes(self, starting_node):
        y = starting_node.getParent()
        node = starting_node
        if node.isRealNode():
            node.fix_node_height_and_size()
        while y is not None:
            y.fix_node_height_and_size()
            y = y.getParent()
        self.set_size(self.getRoot().getSize())

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """
    def delete(self, i):
        if self.empty():
            return -1
        if self.length() == 1:
            self.update_tree_fields(None, None, None)
            return 0
        node_to_delete = self.retrieve_node(i)
        physically_deleted_node = node_to_delete
        if i == 0:
            self.set_first_node(node_to_delete.get_successor())
        if i == self.length() - 1:
            self.set_last_node(node_to_delete.get_predecessor())
        if node_to_delete.isLeaf():  # Case 1: leaf
            self.replace_node(node_to_delete, AVLNode(None), False)
        elif node_to_delete.getRight().isRealNode() is False or node_to_delete.getLeft().isRealNode() is False:
            # Case 2: has only 1 child
            node_to_delete_son = node_to_delete.getRight() \
                if node_to_delete.getRight().isRealNode() else node_to_delete.getLeft()
            self.replace_node(node_to_delete, node_to_delete_son, False)
        else:  # Case 3: has 2 children
            node_to_delete_suc = node_to_delete.get_successor()
            node_to_delete_suc_parent = node_to_delete_suc.getParent()
            self.replace_node(node_to_delete_suc, node_to_delete_suc.getRight(), False)
            self.replace_node(node_to_delete, node_to_delete_suc, True)
            physically_deleted_node = node_to_delete_suc_parent.getLeft()
        return self.fix_the_tree(physically_deleted_node, True)

    """replace node_to_be_replaced with new_node

        @type node_to_be_replaced: AVLNode
        @param node_to_be_replaced: the node that will be replaced
        @type new_node: AVLNode
        @param new_node: the node that will replace node_to_be_replaced 
        @type has_two_children: bool
        @param has_two_children: True if node_to_be_replaced has 2 children, False otherwise
        """

    def replace_node(self, node_to_be_replaced, new_node, has_two_children):
        if node_to_be_replaced == self.root:
            self.set_root(new_node)
            new_node.setParent(None)
        elif node_to_be_replaced.getParent().getRight() == node_to_be_replaced:
            node_to_be_replaced.getParent().setRight(new_node)
        else:
            node_to_be_replaced.getParent().setLeft(new_node)
        if has_two_children:
            new_node.setRight(node_to_be_replaced.getRight())
            new_node.setLeft(node_to_be_replaced.getLeft())

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return None if self.empty() else self.get_first_node().getValue()

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return None if self.empty() else self.get_last_node().getValue()

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        def list_to_array_rec(node, lst):
            if node.isRealNode() is False:
                return
            list_to_array_rec(node.getLeft(), lst)
            lst.append(node.getValue())
            list_to_array_rec(node.getRight(), lst)
            return lst

        return [] if self.empty() else list_to_array_rec(self.root, [])

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return self.getSize()

    """
    @type A: list
    @pre: A is a sorted list
    @param A: the first list 
    @type B: list
    @pre: B is a sorted list
    @param B: the second list 
    @rtype: List
    @returns: sorted list contained A & B elements
    """

    @staticmethod
    def merge(A, B):
        n = len(A)
        m = len(B)
        C = [None for i in range(n + m)]
        a = b = c = 0
        while a < n and b < m:
            if A[a] < B[b]:
                C[c] = A[a]
                a += 1
            else:
                C[c] = B[b]
                b += 1
            c += 1
        if a == n:
            while b < m:
                C[c] = B[b]
                b += 1
                c += 1
        else:
            while a < n:
                C[c] = A[a]
                a += 1
                c += 1
        return C

    """
    @type lst: list
    @param lst: the list to be sorted
    @rtype: List
    @returns: sorted list contained lst elements
    """

    @staticmethod
    def mergesort(lst):
        n = len(lst)
        if n <= 1:
            return lst
        else:
            lst1 = AVLTreeList.mergesort(lst[:n // 2])
            lst2 = AVLTreeList.mergesort(lst[n // 2:])
        return AVLTreeList.merge(lst1, lst2)

    """
    @type lst: List
    @param lst: list of AVLNode
    @rtype: AVLNode
    @returns: AVLNode represents the root of a tree,
    which linked to all other lst elements represented as AVLNodes 
    """
    @staticmethod
    def create_tree_from_list(lst, begin_index, end_index):
        if end_index - begin_index == 1:
            new_node = AVLNode(lst[begin_index])
            new_node.add_virtual_children()
            return new_node
        if end_index == begin_index:
            return AVLNode(None)
        median_index = begin_index + ((end_index - begin_index) // 2)
        median_node = AVLNode(lst[median_index])
        median_node.setLeft(AVLTreeList.create_tree_from_list(lst, begin_index, median_index))
        median_node.setRight(AVLTreeList.create_tree_from_list(lst, median_index + 1, end_index))
        median_node.fix_node_height_and_size()
        return median_node

    """sort the info values of the list

    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        lst_tree = self.listToArray()
        sorted_lst_tree = AVLTreeList.mergesort(lst_tree)
        sorted_tree_root = AVLTreeList.create_tree_from_list(sorted_lst_tree, 0, len(sorted_lst_tree))
        sorted_tree = AVLTreeList()
        first_node = sorted_tree_root.get_first_node()
        last_node = sorted_tree_root.get_last_node()
        sorted_tree.update_tree_fields(sorted_tree_root, first_node, last_node)
        return sorted_tree

    """permute the info values of the list 

    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    def permutation(self):
        lst_tree = self.listToArray()
        for i in range(len(lst_tree) - 1, 0, -1):
            random_element_index = random.randint(0, i)
            lst_tree[i], lst_tree[random_element_index] = lst_tree[random_element_index], lst_tree[i]
        shuffled_tree_root = AVLTreeList.create_tree_from_list(lst_tree, 0, len(lst_tree))
        shuffled_tree = AVLTreeList()
        first_node = shuffled_tree_root.get_first_node()
        last_node = shuffled_tree_root.get_last_node()
        shuffled_tree.update_tree_fields(shuffled_tree_root, first_node, last_node)
        return shuffled_tree

    """concatenates lower_tree to higher_tree if self_is_bigger is True.
    otherwise, concatenates higher_tree to lower_tree 
    
    @type higher_tree: AVLTreeList
    @param higher_tree: a list 
    @type lower_tree: AVLTreeList
    @param lower_tree: a list
    @type lower_tree_height: int
    @param lower_tree_height: lower_tree root's height
    @type self_is_bigger: bool
    @param self_is_bigger: True if higher_tree is self, False otherwise
    @type mid_node: AVLNode
    @param mid_node: a node that going to be in the middle of the concatenated list

    @rtype: AVLNode
    @returns: the first node in the concatenated list that is BF criminal suspect
    """
    def concat_helper(self, higher_tree, lower_tree, lower_tree_height, self_is_bigger, mid_node):
        node = higher_tree.getRoot()
        while node.getHeight() > lower_tree_height:
            node = node.getRight() if self_is_bigger else node.getLeft()
        node_parent = node.getParent()
        if self_is_bigger:
            node_parent.setRight(mid_node)
            mid_node.setRight(lower_tree.getRoot())
            mid_node.setLeft(node)
            higher_tree.set_last_node(lower_tree.last_node)
        else:
            node_parent.setLeft(mid_node)
            mid_node.setLeft(lower_tree.getRoot())
            mid_node.setRight(node)
            lower_tree.update_tree_fields(higher_tree.getRoot(), lower_tree.first_node, higher_tree.last_node)
        return node

    """concatenates lst to self when one/two of them is empty

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """
    def concat_empty_trees(self, lst):
        if self.empty() and lst.empty():
            return 0
        if self.empty():
            self.update_tree_fields(lst.getRoot(), lst.first_node,  lst.last_node)
        return self.getRoot().getHeight() + 1

    """concatenates lst to self when one/two of them has one element

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    """
    def concat_trees_with_one_element(self, lst):
        if lst.size == 1:
            self.get_last_node().setRight(lst.getRoot())
            self.set_last_node(lst.getRoot())
            self.fix_the_tree(self.last_node, False)
        elif self.getSize() == 1:  # lst.length() > 1
            lst_first = lst.get_first_node()
            lst.delete(0)
            node = self.concat_helper(lst, self, 0, False, lst_first)
            self.fix_the_tree(node, True)

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """
    def concat(self, lst):
        self_last = self.get_last_node()
        if self.empty() or lst.empty():  # Case 1: one of the lists is empty
            return self.concat_empty_trees(lst)
        return_val = abs(lst.getRoot().getHeight() - self.getRoot().getHeight())
        if lst.getSize() == 1 or self.getSize() == 1:  # Case 2: one of the lists has only one element
            self.concat_trees_with_one_element(lst)
            return return_val
        #  Case 3: both lists has more than one element
        self.delete(self.length() - 1)
        lst_height = lst.getRoot().getHeight()
        self_height = self.getRoot().getHeight()
        if abs(self_height - lst_height) < 2:  # Case 3.1: |height difference| <= 1
            self_last.update_node_fields(lst.getRoot(), self.getRoot(), None)
            self.update_tree_fields(self_last, self.first_node, lst.last_node)
            return return_val
        elif self_height > lst_height:  # Case 3.2: self is higher than lst
            node = self.concat_helper(self, lst, lst_height, True, self_last)
        else:  # Case 3.3: lst is higher than self
            node = self.concat_helper(lst, self, self_height, False, self_last)
        self.fix_the_tree(node, True)
        return return_val

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        tree_as_lst = self.listToArray()
        for i in range(len(tree_as_lst)):
            if tree_as_lst[i] == val:
                return i
        return -1

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root

    """set root to be the new root of self

    @type root: AVLNode
    @param root: new root to be set
    """
    def set_root(self, root):
        self.root = root

    """returns the size of the tree representing the list

    @rtype: int
    @returns: the size of the tree
    """
    def getSize(self):
        return self.size

    """set size to be the new size of self

    @type size: int
    @param size: new size of self
    """
    def set_size(self, size):
        self.size = size

    """returns the first node of the tree representing the list

    @rtype: AVLNode
    @returns: the first node of the tree
    """
    def get_first_node(self):
        return self.first_node

    """set first_node to be the new first_node of self

    @type first_node: AVLNode
    @param first_node: new first_node of self
    """
    def set_first_node(self, first_node):
        self.first_node = first_node

    """returns the last node of the tree representing the list

    @rtype: AVLNode
    @returns: the last node of the tree
    """
    def get_last_node(self):
        return self.last_node

    """set last_node to be the new last_node of self

    @type last_node: AVLNode
    @param last_node: new last_node of self
    """
    def set_last_node(self, last_node):
        self.last_node = last_node

    def __repr__(self):
        return ','.join(self.listToArray())

    def append(self, val):
        return self.insert(self.length(), val)

    def getTreeHeight(self):
        return self.root.getHeight()
