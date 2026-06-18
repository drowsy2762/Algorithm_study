class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        curr = self.root
        while True:
            if data < curr.data:
                if curr.left is None:
                    curr.left = Node(data)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(data)
                    break
                curr = curr.right

    def delete(self, data):
        def _delete(node, val):
            if not node:
                return node

            if val < node.data:
                node.left = _delete(node.left, val)
            elif val > node.data:
                node.right = _delete(node.right, val)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                temp = node.right
                while temp.left:
                    temp = temp.left
                node.data = temp.data
                node.right = _delete(node.right, temp.data)
            return node

        self.root = _delete(self.root, data)

    def search(self, data):
        curr = self.root
        while curr:
            if data == curr.data:
                return True
            elif data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False


def search_matrix(matrix, target, row, col):
    left = 0
    right = row * col - 1
    while left <= right:
        mid = (left + right) // 2
        r = mid // col
        c = mid % col
        mid_val = matrix[r][c]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    row = 3
    col = 4
    if search_matrix(matrix, target, row, col):
        print("Exist")
    else:
        print("Not exist")
    # Exist

    if search_matrix(matrix, 13, row, col):
        print("Exist")
    else:
        print("Not exist")
    # Not exist


if __name__ == "__main__":
    main()
