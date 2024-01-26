import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}

        def dfs(node):
            if node.val in nodes: return nodes[node.val]
            copy = Node(node.val)
            nodes[node.val] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None


example_1 = Node(val=1)
example_2 = Node(val=2)
example_3 = Node(val=3)
example_4 = Node(val=4)

example_1.neighbors.append(example_2)
example_1.neighbors.append(example_4)
example_2.neighbors.append(example_1)
example_2.neighbors.append(example_3)
example_3.neighbors.append(example_2)
example_3.neighbors.append(example_4)
example_4.neighbors.append(example_3)
example_4.neighbors.append(example_1)

graph = Solution().cloneGraph(node=example_3)
showed = []
q = collections.deque()
q.append(graph)

while q:
    n = q.popleft()
    if n.val in showed:
        continue
    showed.append(n.val)
    print("n", n.val, "->")
    for neighbor in n.neighbors:
        print(neighbor.val)
        q.append(neighbor)
