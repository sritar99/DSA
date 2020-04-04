Tabulation Bottom Up Approach
def getFibo(n):
	dp=[0,1]
	for i in range(2,n+1):
		dp.append(dp[i-1]+dp[i-2])

	return dp[-1]


print(getFibo(9))

Memoization top down Approach 
dp=[-1]*500
def getFibo(n):
	if n==0 or n==1:
		return n
	if dp[n]==-1:
		dp[n]=getFibo(n-1)+getFibo(n-2)

	return dp[n]


print(getFibo(9))