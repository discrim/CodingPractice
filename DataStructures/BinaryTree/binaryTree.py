class BST:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
    
    def get_preorder(self):
        result = [self.root]
        if self.left:
            result += self.left.get_preorder()
        if self.right:
            result += self.right.get_preorder()
        return result
    
    def get_inorder(self):
        result = []
        if self.left:
            result += self.left.get_inorder()
        result.append(self.root)
        if self.right:
            result += self.right.get_inorder()
        return result
    
    def get_postorder(self):
        result = []
        if self.left:
            result += self.left.get_postorder()
        if self.right:
            result += self.right.get_postorder()
        result.append(self.root)
        return result
    
    def print_preorder():
        print(self.root)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()
    
    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.root)
        if self.right:
            self.right.print_inorder()
    
    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.root)
    
    def insert_node(self, x):
        """ Insert x (input value) to the appropriate position.
        
        If x is less than the root, put it on the left.
        Else, put it on the right.
        
        Args:
            x -- 1 -- int: Input value.
        """
        if x < self.root:
            if self.left == None:
                self.left = BST(x)
            else:
                self.left.insert_node(x)
        elif x > self.root:
            if self.right == None:
                self.right = BST(x)
            else:
                self.right.insert_node(x)
        else: # if x == self.root
            pass

if __name__ == "__main__":
    n1 = BST(6)
    n1.insert_node(2)
    n1.insert_node(1)
    n1.insert_node(4)
    n1.insert_node(3)
    n1.insert_node(5)
    n1.insert_node(7)
    n1.insert_node(9)
    n1.insert_node(8)
    
    print(n1.get_preorder())
    print(n1.get_inorder())
    print(n1.get_postorder())