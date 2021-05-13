"""
bfs solution, construct a adj dict with values first, then based on queries, find possible path

time complexity: O(n (V + E))
space complexity: O(E)

"""
from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):

        relations = defaultdict(lambda: dict())
        for e, v in zip(equations, values):
            x, y = e[0], e[1]
            relations[x][y] = v
            relations[y][x] = 1 / v

        def bfs(s,  t):

            q = deque()
            q.append((s, 1))
            visited = set()
            while q:
                n, v = q.popleft()
                visited.add(n)
                if n not in relations:
                    return -1
                for r, d in relations[n].items():
                    if r == t:
                        return d*v
                    if r in visited:
                        continue
                    q.append((r, d*v))
            return -1
        return [bfs(q[0], q[1])  for q in queries]
