# ref: https://discuss.leetcode.com/topic/32976/9-line-python-solution-with-1-
#              line-to-handle-duplication-beat-99-of-others


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n:
                        break
            ans = new_ans
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.permute([1, 1, 2])
