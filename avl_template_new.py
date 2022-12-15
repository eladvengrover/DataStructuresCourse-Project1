# username - graiver1
# id1      - 206363368
# name1    - Shahar Graiver
# id2      - 209008135
# name2    - Elad Vengrover


"""A class represnting a node in an AVL tree"""

INSERT = 1
DELETE = 2


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

    """sets the balance factor of the node

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
        return self.height == 0

    """set children to be virtual nodes """

    def add_virtual_children(self):
        self.setLeft(AVLNode(None))
        self.setRight(AVLNode(None))

    def calc_height(self):
        return max(self.getLeft().getHeight(), self.getRight().getHeight()) + 1

    def calc_size(self):
        return self.getLeft().getSize() + self.getRight().getSize() + 1


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
        self.first_node = None  # TODO - getters & setters
        self.last_node = None

    # add your fields here

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.size == 0

    """"retrieves the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length() 
    @param i: index in the list
    @rtype: AVLNode
    @returns: the i'th item in the list
    """

    def retrieve_node(self, i):
        def retrieve_rec(node, k):
            r = node.left.size + 1
            if r == k:
                return node
            elif r > k:
                return retrieve_rec(node.left, k)
            return retrieve_rec(node.right, k - r)

        return retrieve_rec(self.root, i + 1)

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        if 0 <= i <= self.size - 1:
            return self.retrieve_node(i).value
        return None

    """returns the predecessor of node in the list

    @type node: AVLNode
    @param node: node in the list
    @pre: retrieve(node) != None
    @rtype: AVLNode
    @returns: the predecessor of node in the list
    """
    def get_first_node(self, node):
        while node.getLeft().isRealNode():
            node = node.getLeft()
        return node
    def get_last_node(self, node):
        while node.getRight().isRealNode():
            node = node.getRight()
        return node
    @staticmethod
    def get_predecessor(node):
        if node.getLeft().isRealNode():
            node = node.getLeft()
            while node.getRight().isRealNode():
                node = node.getRight()
            return node
        parent_node = node.getParent()
        while parent_node is not None and node == parent_node.getLeft():
            node = parent_node
            parent_node = node.getParent()
        return parent_node

    """returns the successor of node in the list

    @type node: AVLNode
    @param node: node in the list
    @pre: retrieve(node) != None
    @rtype: AVLNode
    @returns: the successor of node in the list
    """

    @staticmethod
    def get_successor(node):
        if node.getRight().isRealNode():
            node = node.getRight()
            while node.getLeft().isRealNode():
                node = node.getLeft()
            return node
        parent_node = node.getParent()
        while parent_node is not None and node == parent_node.getRight():
            node = parent_node
            parent_node = node.getParent()
        return parent_node

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
        n = self.length()
        node = AVLNode(val)
        node.add_virtual_children()
        if n == 0:
            self.root = node
            self.first_node = node
            self.last_node = node
            self.size = 1
            return 0
        if i == n:
            self.last_node.setRight(node)
            self.last_node = node
        else:
            if i == 0:
                self.first_node = node  # Updating self.first
            prev_node = self.retrieve_node(i)
            if prev_node.getLeft().isRealNode() is False:  # Case 1: prev_node doesn't have left son
                prev_node.setLeft(node)
            else:  # Case 3: prev_node has left son
                node_predecessor = self.get_predecessor(prev_node)
                node_predecessor.setRight(node)

        return self.fix_the_tree(node, INSERT)

    """Rebalancing the tree after insertion/deletion

    @type starting_node: AVLNode
    @param starting_node: The node to be insert or physically deleted
    @type insert_or_delete: int
    @param insert_or_delete: 1 if rebalancing after insertion, 2 if rebalancing after deletion 
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def fix_the_tree(self, starting_node, insert_or_delete):
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
            rotations_count += self.perform_rotation(y)
            if insert_or_delete == 1:
                break
            y = y.getParent()
        self.fix_nodes_size(starting_node, insert_or_delete)
        return rotations_count

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
            self.root = node_b

        self.fix_node_height_and_size(node_a)
        self.fix_node_height_and_size(node_b)

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
            self.root = node_a

        self.fix_node_height_and_size(node_b)
        self.fix_node_height_and_size(node_a)

    def fix_node_height_and_size(self, node):
        node.setSize(node.calc_size())
        node.setHeight(node.calc_height())

    # TODO - maybe change to static method?
    def fix_nodes_size(self, starting_node, insert_or_delete):
        y = starting_node.getParent()
        node = starting_node
        if node.isRealNode():
            self.fix_node_height_and_size(node)
        while y is not None:
            self.fix_node_height_and_size(y)
            node = y
            y = y.getParent()
        if insert_or_delete == INSERT:
            self.root = node
        self.size = self.root.size

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
            self.root = None
            self.size = 0
            self.last_node = None
            self.first_node = None
            return 0
        node_to_delete = self.retrieve_node(i)
        physically_deleted_node = node_to_delete
        if i == 0:
            self.first_node = self.get_successor(node_to_delete)
        if i == self.length() - 1:
            self.last_node = self.get_predecessor(node_to_delete)
        if node_to_delete.isLeaf():  # Case 1: leaf
            self.replace_node(node_to_delete, AVLNode(None), False)
        elif node_to_delete.getRight().isRealNode() is False or node_to_delete.getLeft().isRealNode() is False:
            # Case 2: has only 1 child
            node_to_delete_son = node_to_delete.getRight() \
                if node_to_delete.getRight().isRealNode() else node_to_delete.getLeft()
            self.replace_node(node_to_delete, node_to_delete_son, False)
        else:  # Case 3: has 2 children
            node_to_delete_suc = self.get_successor(node_to_delete)
            node_to_delete_suc_parent = node_to_delete_suc.getParent()
            self.replace_node(node_to_delete_suc, node_to_delete_suc.getRight(), False)
            self.replace_node(node_to_delete, node_to_delete_suc, True)
            physically_deleted_node = node_to_delete_suc_parent.getLeft()
        return self.fix_the_tree(physically_deleted_node, DELETE)

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
            self.root = new_node
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
        return None if self.empty() else self.first_node.getValue()

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return None if self.empty() else self.last_node.getValue()

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
        return self.size

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
    type lst: List
    """
    @staticmethod
    def create_tree_from_list(lst):
        if len(lst) == 1:
            new_node = AVLNode(lst[0])
            new_node.add_virtual_children()
            return new_node
        if len(lst) == 0:
            return AVLNode(None)
        median = AVLNode(lst[len(lst) // 2])
        median.setLeft(AVLTreeList.create_tree_from_list(lst[:len(lst) // 2]))
        median.setRight(AVLTreeList.create_tree_from_list(lst[len(lst) // 2 + 1:]))
        median.setHeight(median.calc_height())
        median.setSize(median.calc_size())
        return median

    """sort the info values of the list

    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        tree_to_lst = self.listToArray()
        sorted_tree_to_lst = AVLTreeList.mergesort(tree_to_lst)
        sorted_nodes = AVLTreeList.create_tree_from_list(sorted_tree_to_lst)
        sorted_tree = AVLTreeList()
        sorted_tree.root = sorted_nodes
        sorted_tree.size = sorted_nodes.getSize()
        sorted_tree.first_node = sorted_tree.get_first_node(sorted_nodes)
        sorted_tree.last_node = sorted_tree.get_last_node(sorted_nodes)
        return sorted_tree


    """permute the info values of the list 

    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    def permutation(self):
        return None

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        return None

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

    def __repr__(self):
        return ','.join(self.listToArray())

    def append(self, val):
        return self.insert(self.length(), val)

    def getTreeHeight(self):
        return self.root.getHeight()
