class Solution:
    def helper(self, candidates, ans, res, s, target):

        if s == target:
            ans.append(res)  # if sum == target add it to the answer
            return
        if s > target:
            return
        if candidates == []:
            return
        for i in range(len(candidates)):
            self.helper(candidates[i:], ans, res + [candidates[i]], s + candidates[i], target)
            # backtracking


    def combinationSum(self, candidates, target):
        if candidates == []:
            return []
        ans = []
        self.helper(candidates, ans, [], 0, target)
        return ans
obj = Solution()
print(obj.combinationSum([2,3,5], 8))