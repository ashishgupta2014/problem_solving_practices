from itertools import combinations

def subsets(nums):
    all_combinations = []
    for r in range(len(nums) + 1):
        combinations_object = combinations(nums, r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list
    return all_combinations
print(subsets([1,2,3]))