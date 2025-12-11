class Solution:
    def findDuplicates(self, arr):
        n = len(arr)
        res = []
        for i in range(n):
            index = abs(arr[i]) - 1
            if arr[index] < 0:
                res.append(abs(arr[i]))
            else:
                arr[index] = -arr[index]
        return res
