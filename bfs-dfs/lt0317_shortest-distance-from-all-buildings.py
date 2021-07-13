"""
bfs solution, to check if some land can be reached by all buildings,
then find the minimal distance for these lands to reach all buildings

Time complexity: O( #buildings * # lands)
Space complexity: O(#buildings * # lands). can be shrink to O(# lands)
"""
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        buildings = list()
        land = defaultdict(lambda: list())
        num_land = 0
        for r_idx, row in enumerate(grid):
            for c_idx, col in enumerate(row):
                if col == 1:
                    buildings.append( (r_idx, c_idx))
                elif col == 0:
                    num_land += 1
        def bfs(r_idx, c_idx):
            visited = set()
            moves = [0, 1, 0 , -1, 0]
            cur = { (r_idx, c_idx)}
            dis = 1
            while cur:
                new_cur = set()
                #visited.update(cur)
                for r, c in cur:
                    for i in range(4):
                        new_r, new_c = r + moves[i], c + moves[i + 1]
                        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 0 and (new_r, new_c) not in visited:
                            new_cur.add( (new_r, new_c))
                for r, c in new_cur:
                    land[(r, c)].append(dis)
                visited.update(new_cur)
                dis += 1
                cur = new_cur
            return len(visited)

        for r_idx, c_idx in buildings:
            bfs(r_idx, c_idx)
        ret = float('INF')
        for k, v in land.items():
            if len(v) == len(buildings):
                ret = min(sum(v), ret)
        return ret if ret != float('INF') else -1
