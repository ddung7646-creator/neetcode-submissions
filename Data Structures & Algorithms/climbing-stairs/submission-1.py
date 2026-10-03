class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        cl = [0]* (n+1)
        cl[1]=1
        cl[2]=2
        for i in range(3,n+1):
            cl[i]= cl[i - 1] + cl[i - 2]
        return cl[n]
solution = Solution()
print(solution.climbStairs(3))