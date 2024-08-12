#1. Two Sum
def two_sum(nums,target):
    for i in range(len(nums) - 1):
        # print(nums[i])
        for j in range(i+1,len(nums)):
            # print(nums[j])
            # print(nums[i],"+",nums[j],"=",nums[i]+nums[j])
            if (i != j and nums[i] + nums[j] == target):
                return i,j
    return False
# print(two_sum([7,44,2,6],8))