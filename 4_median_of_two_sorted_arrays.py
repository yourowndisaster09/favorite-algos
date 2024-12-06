from math import inf
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        total = m + n
        median = (total - 1) // 2

        if m >= n:
            numsX = nums1
            lenX = m
            numsY = nums2
            lenY = n
            a = 0
            b = n - 1
        else:
            numsX = nums2
            lenX = n
            numsY = nums1
            lenY = m
            a = 0
            b = m - 1

        while a <= b:
            midIdx = ((b - a) // 2) + a
            midVal = numsY[midIdx]
            fixedIdx = median - midIdx - 1
            if numsX[fixedIdx + 1] < midVal:
                b = midIdx - 1
            else:
                a = midIdx + 1

        lastY = b
        lastX = median - b - 1

        a = max(numsX[lastX] if lastX > -1 else -inf, numsY[lastY] if lastY > -1 else -inf)
        if total % 2 == 0:
            b = min(numsX[lastX + 1] if lastX < lenX - 1 else inf, numsY[lastY + 1] if lastY < lenY - 1 else inf)
            return (a + b) / 2
        else:
            return a



if __name__ == "__main__":
    s = Solution()
    assert(s.findMedianSortedArrays([1,3], [2]) == 2.0)
    assert(s.findMedianSortedArrays([1,2], [3,4]) == 2.5)
    assert(s.findMedianSortedArrays([1,3,5,6,7,8,9,15], [2,4,10,11,12,13,14]) == 8.0)