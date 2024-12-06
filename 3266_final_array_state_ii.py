import heapq

class Solution:
    def getFinalState(self, nums, k, multiplier):
        # if multiplier == 1:
        #     return nums

        n = len(nums)
        mod = 10**9 + 7

        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)
        currMax = max(nums)

        k_i = 0
        print(currMax)
        while True:
            minNum, i = heapq.heappop(heap)
            minMultiplied = (minNum * multiplier)
            if minMultiplied > currMax:
                break
            k_i += 1
            nums[i] = minMultiplied
            if k_i == k:
                return nums
            heapq.heappush(heap, (nums[i], i))

        numCycles = (k-(k_i)) // n
        remainderLastCycle = (k-(k_i)) % n

        nums = [(num * pow(multiplier, numCycles, mod)) for num in nums]

        print(numCycles, remainderLastCycle)
        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)
        while remainderLastCycle > 0:
            print(nums)
            minNum, i = heapq.heappop(heap)
            minMultiplied = (minNum * multiplier)
            nums[i] = minMultiplied
            heapq.heappush(heap, (nums[i], i))
            remainderLastCycle -= 1

        return [n % mod for n in nums]


nums = [1]
k = 1000000000
multiplier = 1

ans = Solution().getFinalState(nums, k, multiplier)
print(ans)