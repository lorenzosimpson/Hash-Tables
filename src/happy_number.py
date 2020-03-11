class Solution:
    def isHappy(self, n: int) -> bool:
        arr = [d for d in str(n)]
        # base case: result == 1
        result = 0
        for i in range(len(arr)):
            result += int(arr[i]) * int(arr[i])
        if result == 1:
            return True
        return self.isHappy(result)
        

test = Solution()
print(test.isHappy(19))
