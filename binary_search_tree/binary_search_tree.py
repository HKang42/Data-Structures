"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the value to the root's value to determine which direction
        # we're gonna go in 
        # if the value < root's value 
        if value < self.value:
            # go left 
            # how do we go left?
            # we have to check if there is another node on the left side
            if self.left: 
                # then self.left is a Node 
                # now what?
                self.left.insert(value)
            else:
                # then we can park the value here
                self.left = BSTNode(value)
        # else the value >= root's value 
        else:
            # go right
            # how do we go right? 
            # we have to check if there is another node on the right side 
            if self.right:
                # then self.right is a Node 
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        # if target matches the node value, return true
        if target == self.value:
            return True

        # If target less than node value, return False if no left node.
        # Otherwise, run self.contrains on the left node.
        elif target < self.value:
            
            if self.left == None:
                return False
            
            else:
                return self.left.contains(target)
        
        else:
            if self.right == None:
                return False

            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value

        # If we can go right (larger node exists), execute get max on the right node
        if self.right:
            return self.right.get_max()
        
        # If there is no larger node, return max
        else:
            return max


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        # call function on value
        fn(self.value)

        # recursively call function for every left and right node
        # check for left and right at every node
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


"""
q = BSTNode(5)
q.insert(2)
q.insert(3)
q.insert(7)
print(q.contains(7))
print(q.contains(8))
"""