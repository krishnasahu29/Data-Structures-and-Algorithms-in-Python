class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)

            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)

            else:
                self.right = BinarySearchTreeNode(data)

    def inorder_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.inorder_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data

        return self.right.find_max()

    def find_min(self):
        if self.right is None:
            return self.data

        return self.right.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':

    nums = [17, 4, 1, 20, 9, 23, 18, 34]
    nums_tree = build_tree(nums)
    nums_tree.delete(20)
    print("After deleting 20: ", nums_tree.inorder_traversal())

    # countries = ['India', 'Pakistan', 'US', 'UK', 'Japan']
    # country_tree = build_tree(countries)
    # print("UK is in the list?", country_tree.search("UK"))
    # print("Sweden is in the list?", country_tree.search("Sweden"))
    # print(country_tree.inorder_traversal())
