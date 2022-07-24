class Solution(object):
    def twoSum(self, nums, target):
        startj = 1
        for i in range (len(nums)):
            difference = target - nums[i]
            for j in range(startj, len(nums)):
                if nums[j] == difference:
                        return [i, j]
            startj += 1


    print(twoSum(0, [5,6,6,1], 12))

print(len([1,2]))

for i in range(0, 2):
    print(i)

#faster
class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            difference = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == difference:
                        return [i, j]


