def UniqueSubStr(s):
	suffix=[]
	for i in range(len(s)):
		suffix.append(s[i:])
	suffix.sort()
	print(suffix)
	LCP=[0]
	for i in range(len(suffix)-1):
		count=0
		s1=suffix[i]
		s2=suffix[i+1]
		j=0
		k=min(len(s1),len(s2))
		while j<k:
			if s1[j]!=s2[j]:
				break
			j+=1
			count+=1
		LCP.append(count)
	print(LCP)
	n=len(s)
	print("NO of Unique Substrings: ",((n*(n+1))/2)-sum(LCP))
				



UniqueSubStr(input("Enter String : "))