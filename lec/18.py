# Class Based Implementation
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(1)]), Tree(4)])
    >>> t1 = Tree(5, [Tree(6)])
    >>> t.children[0].children.append(t1)
    >>> len(t.children[0].children)
    2
    >>> t.entry
    3
    >>> t.children[0].entry
    2
    >>> t.children[1].is_leaf()
    True
    """
    def __init__(self, entry, children=[]):
        for c in children:
            assert isinstance(c, Tree)

        self.entry = entry
        self.children = children

    def is_leaf(self):
        """
        >>> t = Tree(3, [Tree(2, [Tree(1)]), Tree(4)])
        >>> t.children[1].is_leaf()
        True
        """
        return not self.children

    def __contains__(self, e):
        """
        >>> t = Tree(3, [Tree(2, [Tree(1)]), Tree(4)])
        >>> 8 in t
        False
        >>> 2 in t
        True
        >>> -2 in t
        False
        >>> 3 in t
        True
        >>> 1 in t
        True
        >>> t1 = Tree(5, [Tree(6)])
        >>> t.children[0].children.append(t1)
        >>> 6 in t
        True
        >>> 1 in t
        True
        >>> 81 in t
        False
        >>> t1 = Tree(7, [Tree(3, [Tree(2), Tree(5)]), Tree(13, [Tree(11), Tree(17)])])
        >>> 11 in t1
        True
        """
        if self.entry == e:
            return True
        for c in self.children:
            if e in c:
                return True
        return False

def tree_map(t, fn):
    """
    >>> square = lambda x: x * x
    >>> t = Tree(3, [Tree(2, [Tree(1)]), Tree(4)])
    >>> tree_map(t, square)
    >>> t.entry
    9
    >>> t.children[0].entry
    4
    >>> t.children[0].children[0].entry
    1
    >>> t.children[1].entry
    16
    >>> t.children[0].children[0].is_leaf()
    True
    >>> t.children[1].is_leaf()
    True
    """
    t.entry = fn(t.entry)
    for c in t.children:
        tree_map(c, fn)

# ADT Based Implementation
def tree(entry, children=[]):
    """
    >>> t_class = Tree(3, [Tree(2, [Tree(1)]), Tree(4)])
    >>> t_adt = tree(3, [tree(2, [tree(1)]), tree(4)])
    >>> t_class.entry == entry(t_adt)
    True
    >>> t_class.entry = 5
    >>> entry(t_adt) = 5
    Traceback (most recent call last):
    ...
    SyntaxError: can't assign to function call
    >>> t_class.entry == entry(t_adt)
    False
    """
    return [entry, children]

def entry(tree):
    return tree[0]

def children(tree):
    return tree[1]

# Binary Search Tree (BST) Class
class BST:
    empty = ()
    def __init__(self, entry, left=empty, right=empty):
        assert left is BST.empty or isinstance(left, BST)
        assert right is BST.empty or isinstance(right, BST)

        self.entry = entry
        self.left, self.right = left, right

        if left is not BST.empty: 
            assert left.max <= entry
        if right is not BST.empty: 
            assert entry < right.min

    @property
    def max(self): # Returns the maximum element in the tree
        if self.right is BST.empty:
            return self.entry
        return self.right.max

    @property
    def min(self): # Returns the minimum element in the tree
        if self.left is BST.empty:
            return self.entry
        return self.left.min

    def __contains__(self, e):
        """
        >>> bst = BST(7, BST(3, BST(2), BST(5)), BST(13, BST(11), BST(17)))
        >>> 11 in bst
        True
        >>> 19 in bst
        False
        """
        if self.entry == e:
            return True
        elif e < self.entry and self.left is not BST.empty:
            return e in self.left
        elif e > self.entry and self.right is not BST.empty:
            return e in self.right
        return False

