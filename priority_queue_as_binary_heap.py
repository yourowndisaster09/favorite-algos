class MaxHeap:
    def __init__(self):
        self.arr = []

    def insert(self, num):
        self.arr.append(num)
        i = len(self.arr) - 1
        # Parent k has children 2k+1, 2k+2
        # Swap child with parent
        while i > 0 and self.arr[(i-1)//2] < self.arr[i]:
            temp = self.arr[(i-1)//2]
            self.arr[(i-1)//2] = self.arr[i]
            self.arr[i] = temp
            i = (i-1)//2

    def getMax(self):
        if not self.arr:
            return None

        # Swap max num (i=0) with last num (i=n-1)
        n = len(self.arr)
        maxVal = self.arr[0]
        self.arr[0] = self.arr[n-1]
        self.arr[n-1] = maxVal

        i = 0
        while True:
            nextI = 2*i+1
            if nextI >= n-1:
                break
            if nextI+1 < n-1 and self.arr[nextI+1] >= self.arr[nextI]:
                nextI += 1
            if self.arr[i] >= self.arr[nextI]:
                break

            temp = self.arr[i]
            self.arr[i] = self.arr[nextI]
            self.arr[nextI] = temp

            i = nextI

        return self.arr.pop()

    def __str__(self) -> str:
        return str(self.arr)

    @staticmethod
    def kthLargest(arr, k):
        heap = MaxHeap()
        [heap.insert(i) for i in arr]
        print(heap)
        ans = None
        for j in range(k):
            ans = heap.getMax()
            print(heap)
        return ans


# heap = MaxHeap()
# heap.insert(45)
# heap.insert(20)
# heap.insert(14)
# heap.insert(12)
# heap.insert(31)
# heap.insert(7)
# heap.insert(11)
# heap.insert(13)
# heap.insert(7)

# print(heap)
# print(heap.getMax())
# print(heap)

# print(MaxHeap.kthLargest([3,2,1,5,6,4], 2))
print(MaxHeap.kthLargest([3,2,3,1,2,4,5,5,6], 4))
# print(MaxHeap.kthLargest([-1,2,0], 2))
