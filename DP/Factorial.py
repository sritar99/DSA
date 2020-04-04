Tabulation Bottom Up Approach
def getFactorial(n):
	dp=[0,1]
	for i in range(2,n+1):
		dp.append(dp[i-1]*i)
	return dp[-1]

print(getFactorial(5))


Memoization top down Approach 

dp=[-1]*500
def getFactorial(n):
	if n==0:
		return 1

	if dp[n]!=-1:
		return dp[n]
	dp[n] = (n*getFactorial(n-1))
	return dp[n]

print(getFactorial(6))