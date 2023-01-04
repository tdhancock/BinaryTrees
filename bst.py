'''Implement a BST class'''

class BST:
    '''Binary search Tree'''
    def __init__(self):
        self.root = None
        self.nodes = []

    def is_empty(self):
        '''Return True if empty, False otherwise.'''
        if self.root:
            return False
        return True

    def size(self):
        '''Return size of tree'''
        if self.root:
            return self.root.size(self.root)
        return 0

    def height(self):
        '''Return height of tree'''
        if self.root:
            return self.root.get_height()
        return 0

    def add(self,data):
        '''Add item to its proper place in the tree. Return the modified tree.''' 
        if self.root:
            return self.root.insert(data)
        self.root = Node(data)
        return True

    def remove(self, data):
        '''Remove item from the tree. Return the modified tree. '''

        return self.root.delete_node(self.root, data)

    def find(self, data):
        '''Return the matched item. If item is not in the tree, raise a ValueError. '''
        if self.root:
            return self.root.find(data)
        raise ValueError

    def inorder(self):
        '''Return a list with the data items in order of inorder traversal. '''
        lyst = []
        self.root.inorder(lyst)
        return lyst

    def preorder(self):
        '''Return a list with the data items in order of preorder traversal. '''
        lyst = []
        self.root.preorder(lyst)
        return lyst

    def postorder(self):
        '''Return a list with the data items in order of postorder traversal. '''
        lyst = []
        self.root.postorder(lyst)
        return lyst

    def rebalance(self):
        '''rebalance the tree. Return the modified tree. '''
        self.store_nodes(self.root)
        self.root = self.rebuild_tree(self.nodes)
        return self.root

    def store_nodes(self, root):
        '''Store Nodes'''
        if root:
            if root.left:
                self.store_nodes(root.left)
            self.nodes.append(root.value)
            if root.right:
                self.store_nodes(root.right)

    def rebuild_tree(self, nodes):
        '''Rebuild Tree'''
        if not nodes:
            return None
        mid_val = len(nodes)//2
        root = Node(nodes[mid_val])
        root.left = self.rebuild_tree(nodes[0:mid_val])
        root.right = self.rebuild_tree(nodes[mid_val+1:])

        return root

class Node:
    '''Node class for BST'''
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
        '''Insert new Node'''
        if self.value.letter == data.letter:
            self.value.count += 1
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            self.left = Node(data)

        else:
            if self.right:
                return self.right.insert(data)
            self.right = Node(data)

    def find(self, data):
        '''Find New Node'''
        if (self.value == data):
            return True
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            return False
        else:
            if self.right:
                return self.right.find(data)
            return False

    def preorder(self, lyst):
        '''Return preorder'''
        if self:
            lyst.append(self.value)
            if self.left:
                self.left.preorder(lyst)
            if self.right:
                self.right.preorder(lyst)

    def postorder(self, lyst):
        '''Return postorder'''
        if self:
            if self.left:
                self.left.postorder(lyst)
            if self.right:
                self.right.postorder(lyst)
            lyst.append(self.value)

    def inorder(self, lyst):
        '''Return inorder'''
        if self:
            if self.left:
                self.left.inorder(lyst)
            lyst.append(self.value)
            if self.right:
                self.right.inorder(lyst)

    def size(self, value):
        '''Return Size'''
        if value is None:
            return 0
        return 1 + self.size(value.left) + self.size(value.right)

    def get_height(self):
        '''Return height'''
        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())
        elif self.left:
            return 1 + self.left.get_height()
        elif self.right:
            return 1 + self.right.get_height()
        else:
            return 1

    def delete_node(self, root, data):
        '''Delete Node'''
        if not root: 
            return None
        if root.value == data:
            if not root.left and not root.right: 
                return None
            if not root.left and root.right:
                return root.right
            if not root.right and root.left:
                return root.left

            pnt = root.right
            while pnt.left:
                pnt = pnt.left
            root.value = pnt.value
            root.right = self.delete_node(root.right, root.value)

        elif root.value > data:
            root.left = self.delete_node(root.left, data)

        else:
            root.right = self.delete_node(root.right, data)

        return root
