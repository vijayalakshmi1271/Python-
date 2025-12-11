class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        left = 0
        sum = 0
        for right in range(n):
            sum += arr[right]
            while sum > target and left <= right:
                sum -= arr[left]
                left += 1
            if sum == target:
                return [left + 1, right + 1]   
        return [-1]
