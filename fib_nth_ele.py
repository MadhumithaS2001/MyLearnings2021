def fib(n,dp):
    if(n<=1):
        dp[n]=n
        return n
    else:
        if(dp[n-1]==-1):
            a=fib(n-1,dp)
        else:
            a=dp[n-1]
        if(dp[n-2]==-1):
            b=fib(n-2,dp)
        else:
            b=dp[n-2]
        dp[n]=a+b
        return dp[n]
n=int(input())
dp=[-1]*(n+1)
print(fib(n,dp))
