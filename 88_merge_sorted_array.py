class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        js = 0
        je = 0
        while i < (m + n) - 1:
            while je < n and (nums2[je] <= nums1[i]):
                print(i,js,je,nums1,nums2)
                je = je + 1
            for j in range(js, je):
                nums1.insert(i, nums2[j])
                i = i + 1
            js = je
        if js < n - 1:
            print(i,js,je,nums1,nums2)
            for j in range(js, n):
                nums1.insert(i+1, nums2[j])
                i = i + 1
        del nums1[(m+n):]



if __name__ == "__main__":
    nums1 = [2,5,6,0,0,0]
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [1,2,3]
    nums2 = [2,5,6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)