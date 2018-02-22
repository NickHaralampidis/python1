import random
p=["A","B","C","D","E","F","G","H","I","G","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
a= [[0 for x in range(100)] for y in range(100)] 
b= [[0 for x in range(100)] for y in range(100)]
for i in range (0,100):
	
	for j in range (0,99):
	    a[i][j]=random.choice(p);
	    print a[i][j],
	a[i][99]=random.choice(p);
	print a[i][99]
for i in range (0,100):
	for j in range (0,100):
		b[i][j]=a[j][i]
file = open("ex.txt","r")
for line in file:
	c1=0
	
	c=101-len(line)
	word=list(line)
	d=len(line)
	for i in range (0,100):
		for j in range (0,c):
			
			if ((a[i][j:(j+d)])==word):
				c1=1
	for i in range (0,100):
		for j in range (0,c):
			
			if (b[i][j:(j+d)])==word:
				c1=1
	if c1==1:
		print line
	
				
		
			

