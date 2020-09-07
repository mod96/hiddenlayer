import sys
sys.setrecursionlimit(10000)
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data[0] < self.data[0]:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)  # tree is a recurrsive data structure
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

def solution(nodeinfo):
    node_dict = {(elt[0],elt[1]) : i+1 for i, elt in enumerate(nodeinfo)}
    nodeinfo.sort(reverse=True,key=lambda tup : (tup[1],-tup[0]))
    tree = build_tree(nodeinfo)
    preorder = [node_dict[(elt[0],elt[1])] for elt in tree.pre_order_traversal()]
    postorder = [node_dict[(elt[0], elt[1])] for elt in tree.post_order_traversal()]

    return [preorder,postorder]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	))