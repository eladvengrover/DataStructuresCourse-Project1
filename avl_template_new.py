# username - graiver1
# id1      - 206363368
# name1    - Shahar Graiver
# id2      - 209008135
# name2    - Elad Vengrover


"""A class represnting a node in an AVL tree"""


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
        self.height = -1
        self.isReal = False if value is None else True
        self.size = 1 if self.isReal else 0

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        return self.left if self.left.isReal else None

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right if self.right.isReal else None

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent if self.parent.isReal else None

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value if self.isReal else None

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height if self.isReal else -1

    """returns the size

    @rtype: int
    @returns: the size of self, 0 if the node is virtual
    """

    def getSize(self):
        return self.size

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node
        node.setParent(self)

    """sets right child

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

    # add your fields here

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.size == 0

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

    def get_predecessor(self, node):
        if node.getLeft() is not None:
            node_tree = AVLTreeList()
            node_tree.insert(0, node.getLeft())
            return node_tree.get_max()
        parent_node = node.getParent()
        while parent_node is not None and node == parent_node.getLeft():
            node = parent_node
            parent_node = node.getParent()
        return parent_node

    def get_min(self):
        if self.root is None:
            return None
        node = self.root
        left = node.left
        while left.isRealNode():
            node = left
            left = node.left
        return node

    def get_max(self):
        if self.root is None:
            return None
        node = self.root
        right = node.right
        while right.isRealNode():
            node = right
            right = node.right
        return node

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        n = self.length()
        node = AVLNode(val)
        if i == n:
            self.get_max().setRight(node)
        else:
            prev_node = self.retrieve_node(i)
            if prev_node.getLeft() is None:
                prev_node.setLeft(node)
            else:
                self.get_predecessor(prev_node).setRight(node)
        # fix the tree - update size and height of each node to root

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        return -1

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return self.get_min().value

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return self.get_max().value

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        return None

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return self.size

    """sort the info values of the list

    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        return None

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
        return None

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root
