
class TreeNode:

        def __init__(self, data, left = None, right = None) -> None:
        
            self.data = data
            self.right = right
            self.left = left
    
        def __str__(self):
            return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'
# left <
# right >
class BinarySearchTree:

    def __init__(self, three_data) -> None:

        self.root = None
        for value in three_data:
            self.insert(value)
   
    def insert(self, data):

        if not self.root:
            self.root = TreeNode(data)
        else:
            self.recursive_insertion(self.root, data)

    def recursive_insertion(self, node, data):

        if int(data) <= int(node.data):
            if not node.left:
                node.left = TreeNode(data)
            else:
                self.recursive_insertion(node.left, data)
        else:
            if not node.right:
                node.right = TreeNode(data)
            else:
                self.recursive_insertion(node.right, data)
    
    @classmethod
    def inorder(cls, node):

        if node != None:
            yield from cls.inorder(node.left)
            yield node.data
            yield from cls.inorder(node.right)

    def data(self):

        return self.root

    def sorted_data(self):

        return list(self.inorder(self.root))
    
    def __iter__(self):

        return ((node.data for node in self.inorder(self.root)))
    
    
        


