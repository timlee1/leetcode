# ref: https://leetcode.com/discuss/79931/10-line-python-solution-104-ms
# ref: https://briangordon.github.io/2014/08/the-skyline-problem.html
import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = sorted([(L, -H, R) for L, R, H in buildings] + list(
            {(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[[0, 0]], [(0, float('inf'))]]  # (0, inf) is important
        for x, negH, R in events:
            while x >= hp[0][1]:  # remove buildings behind the 'scan line'
                heapq.heappop(hp)
            if negH:  # add a new building height to the heap
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]:  # add a point when the highest point so
                res += [x, -hp[0][0]],  # far changed
        return res[1:]

if __name__ == '__main__':
    sol = Solution()
    print sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10],
                          [19, 24, 8]])
