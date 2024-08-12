#1. Two Sum
def two_sum(nums,target):
    for i in range(len(nums) - 1):
        for j in range(i+1,len(nums)):
            if (i != j and nums[i] + nums[j] == target):
                return i,j
    return False
print(two_sum([2,7,6,44],8))