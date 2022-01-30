class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n==0:
            return 0
        if n==1:
             return 1
        pre,ppre=1,1#  pre,ppre前时刻，前2时刻
        for i in range(2,n+1):
            tmp = pre#tmp 用于pre ,与ppre 完成数值改变
            pre = pre + ppre#当前等于前面两步相加
            ppre = tmp#前一时刻变成前前时刻
        return pre

a=Solution()
n=3
print(a.climbStairs(n))