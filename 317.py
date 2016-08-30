# ref: https://discuss.leetcode.com/topic/34702/python-solution-72ms-beats-100
#              -bfs-with-pruning
import collections


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        row, col, buildings = len(grid), len(grid[0]), sum(
            sum(i for i in row if i == 1) for row in grid)
        hit, distSum = [[0] * col for _ in xrange(row)], [[0] * col
                                                          for _ in xrange(row)]

        def bfs(start_i, start_j):
            visited = [[False] * col for _ in xrange(row)]
            visited[start_i][start_j], count1, queue = (
                True, 1, collections.deque([(start_i, start_j, 0)]))
            while queue:
                i, j, dist = queue.popleft()
                for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                    if 0 <= x < row and 0 <= y < col and not visited[x][y]:
                        visited[x][y] = True
                        if not grid[x][y]:
                            queue += (x, y, dist + 1),
                            hit[x][y] += 1
                            distSum[x][y] += dist + 1
                        elif grid[x][y] == 1:
                            count1 += 1
            return count1 == buildings
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == 1:
                    if not bfs(i, j):
                        return -1
        return min([distSum[i][j] for i in xrange(row) for j in xrange(col)
                    if hit[i][j] == buildings and not grid[i][j]] or [-1])

if __name__ == '__main__':
    sol = Solution()
    print sol.shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0]])
