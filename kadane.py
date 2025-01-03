def maxSubArray(nums):
    n = len(nums)
    subArraySum = nums[0]
    maxSum = nums[0]

    for i in range(1, n):
        subArraySum = max(nums[i], subArraySum + nums[i])
        maxSum = max(maxSum, subArraySum)

    return maxSum


assert(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)