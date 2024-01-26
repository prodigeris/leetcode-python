import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}
        q = collections.deque()
        q.append(node)
        while q:
            n = q.popleft()
            if not n:
                break
            nodes[n.val] = Node(n.val)
            for neighbor in n.neighbors:
                if neighbor.val not in nodes:
                    q.append(neighbor)
        q.append(node)

        visited = []
        while q:
            n = q.popleft()
            if not n or n.val in visited:
                continue
            for neighbor in n.neighbors:
                nodes[n.val].neighbors.append(nodes[neighbor.val])
                q.append(neighbor)
            visited.append(n.val)
        if not node:
            return None
        return nodes[node.val]



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

