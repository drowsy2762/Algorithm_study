class TreeNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


class DecisionTreeModel:
    def __init__(self):
        self.root = None

    def search(self, current_node, prune_target):
        if current_node is None or current_node.node_id == prune_target:
            return 0

        valid_children = []
        for child in current_node.children:
            if child.node_id != prune_target:
                valid_children.append(child)

        if not valid_children:
            return 1

        total_leaves = 0
        for child in valid_children:
            total_leaves += self.search(child, prune_target)

        return total_leaves

    def count_terminal_nodes(self, n, parents, prune_target):
        nodes = [TreeNode(i) for i in range(n)]
        root_node = None

        for i in range(n):
            p = parents[i]
            if p == -1:
                root_node = nodes[i]
            else:
                nodes[p].children.append(nodes[i])

        if root_node is None or root_node.node_id == prune_target:
            result = 0
        else:
            result = self.search(root_node, prune_target)

        self.print_result(result)


def main():
    model = DecisionTreeModel()
    model.count_terminal_nodes(5, [-1, 0, 0, 1, 1], 1)  # Remaining terminal nodes: 1
    model.count_terminal_nodes(5, [-1, 0, 0, 1, 1], 2)  # Remaining terminal nodes: 2


if __name__ == "__main__":
    main()
