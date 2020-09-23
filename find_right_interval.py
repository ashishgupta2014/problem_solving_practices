from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals):

        START, END = 0, 1

        # sort on pairs in ascending order
        # pair: ( START position of interval, original index)
        start_and_idx_pairs = sorted((interval[START], idx) for idx, interval in enumerate(intervals))

        result = []

        for interval in intervals:

            # get the index of first larger pair
            idx_of_first_larger_pair = bisect_left(start_and_idx_pairs, (interval[END],))

            # original index of right interval before sorting, initialized as -1
            idx_of_right_interval = -1

            if idx_of_first_larger_pair < len(intervals):
                # if the index of first larger pair exists, get original index before sorting
                idx_of_right_interval = start_and_idx_pairs[idx_of_first_larger_pair][1]

            result.append(idx_of_right_interval)

        return result
s = Solution()
print(s.findRightInterval([[3,4],[2,3],[1,2]]))