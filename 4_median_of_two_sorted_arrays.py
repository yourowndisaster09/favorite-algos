class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        total = m + n
        median = (total - 1) // 2

        if m >= n:
            fixedNums = nums1
            fixedTotal = m
            searchedNums = nums2
            a = 0
            b = n - 1
        else:
            fixedNums = nums2
            fixedTotal = n
            searchedNums = nums1
            a = 0
            b = m - 1

        i = 0
        while a <= b:
            mid = ((b - a) // 2) + a
            i = median - mid - 1
            if i + 1 == fixedTotal or fixedNums[i + 1] >= searchedNums[mid]:
                a = mid + 1
            else:
                b = mid - 1

        searchedI = b
        fixedI = median - searchedI - 1
        if total % 2 == 0:

        else:
            if fixedI > -1 and searchedI > -1:
                return max(fixedNums[fixedI], searchedNums[searchedI])
            elif fixedI > -1:
                return fixedNums[fixedI]
            else:
                return searchedNums[searchedI]



if __name__ == "__main__":
    # assert(Solution().findMedianSortedArrays([1,3], [2]) == 2.0)
    # assert(Solution().findMedianSortedArrays([1,2], [3,4]) == 2.5)
    assert(Solution().findMedianSortedArrays([1,3,5,6,7,8,9,15], [2,4,10,11,12,13,14]) == 8.0)