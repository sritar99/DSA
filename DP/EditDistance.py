def getEditDistance(str1,str2):
	table=[[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	for i in range(len(table)):
		table[i][0]=i
	for i in range(len(table[0])):
		table[0][i]=i
	

	for i in range(1,len(str1)+1):
		for j in range(1,len(str2)+1):
			if str1[i-1]==str2[j-1]:
				table[i][j]=table[i-1][j-1]
			else:
				table[i][j]=1+min(table[i-1][j-1],table[i][j-1],table[i-1][j])

	print(table)

	
	

getEditDistance("azced","abcdef")