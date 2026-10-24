
def dls(tree, node, goal, limit, path, order):
    order.append(node)

    if node == goal:
        return path

    if limit == 0:
        return None

    for child in tree.get(node, []):
        result = dls(
            tree, child, goal, limit - 1,
            path + [child], order
        )
        if result is not None:
            return result

    return None


def iddfs(tree, start, goal):
    max_depth = len(tree)

    for limit in range(max_depth + 1):
        order = []
        result = dls(tree, start, goal, limit, [start], order)

        print(f"Iteration {limit + 1} (Depth limit {limit})")
        print("Node visiting order:", " -> ".join(order))

        if result is not None:
            print("Goal found!")
            print("Solution path:", " -> ".join(result))
            return

    print("Goal not found.")


tree = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    children = input(
        f"Enter children of {node} (space-separated, or - if none): "
    ).split()

    tree[node] = [] if children == ["-"] else children

start = input("Enter start node: ")
goal = input("Enter goal node: ")

if start not in tree or goal not in tree:
    print("Invalid start or goal node.")
else:
    iddfs(tree, start, goal)
