"""
bfs solution, boundary would be the coordinates along with the num of obstacles breaks
keep tracking the visited point by maintaining a dictionary
if the new coordinates is reachable or is an obstacle but still has chances to eliminate, add it to boundary

pruning is the key here, since it's manhattan distance, it's easy to track the shortest path from any point to the end
when the shortest path is less then still available elimination chances,
simply return the current iterations and the manhattan distance between them

possible improvement: sometimes it will make eliminations but not moving forward too much,
probably we can further prune it by checking those situation

time complexity: O(kmn)
space complexity: O(kmn)
"""
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        start = [(0, 0, 0)]
        m = len(grid) - 1
        n = len(grid[0]) - 1
        if m == n == 0:
            return 0
        ret = 0
        visited = defaultdict(lambda: set())
        while start:
            boundary = set()
            ret += 1
            for p in start:
                r_idx, c_idx, obs_num = p
                visited[obs_num].add((r_idx, c_idx))

                """
                pruning
                """
                if m - r_idx + n - c_idx < k - obs_num:
                    return ret + min(k - obs_num, m - r_idx + n - c_idx - 1)
                if (r_idx + 1 == m and c_idx == n) or (r_idx == m and c_idx + 1 == n):
                    return ret

                if r_idx - 1 >= 0: # up
                    if grid[r_idx - 1][c_idx] == 0 and (r_idx - 1, c_idx) not in visited[obs_num]:
                        boundary.add((r_idx -1, c_idx, obs_num))
                    elif grid[r_idx - 1][c_idx] == 1 and obs_num + 1 <= k:
                        boundary.add((r_idx -1, c_idx, obs_num + 1))

                if r_idx + 1 < len(grid): # down
                    if grid[r_idx + 1][c_idx] == 0 and (r_idx + 1, c_idx) not in visited[obs_num]:
                        boundary.add((r_idx +1, c_idx, obs_num))
                    elif grid[r_idx + 1][c_idx] == 1 and obs_num + 1 <= k:
                        boundary.add((r_idx + 1, c_idx, obs_num + 1))

                if c_idx - 1 >= 0: # left
                    if grid[r_idx][c_idx - 1] == 0 and (r_idx , c_idx - 1) not in visited[obs_num]:
                        boundary.add((r_idx, c_idx - 1, obs_num))
                    elif grid[r_idx][c_idx - 1] == 1 and obs_num + 1 <= k:
                        boundary.add((r_idx, c_idx - 1, obs_num + 1))


                if c_idx + 1 < len(grid[0]): # right
                    if grid[r_idx][c_idx + 1] == 0 and (r_idx , c_idx + 1) not in visited[obs_num]:
                        boundary.add((r_idx, c_idx + 1, obs_num))
                    elif grid[r_idx][c_idx + 1] ==1 and obs_num + 1 <= k:
                        boundary.add((r_idx, c_idx + 1, obs_num + 1))

            start = boundary.copy()
        return -1