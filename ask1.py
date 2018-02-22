import random
sum=0
for j in range (0,1000):
	p=[]
	for x in range (1,81,1):
		p.append (x)
	t=[]
	k=[]
	for i in range (0,100):
		k=[]
		for s in range (0,5):
			k.append(random.choice(p))
			p.remove(k[s])
		t.append(k)
		p=p+k
	v=[]
	c=[0 for x in range (100)]
	for l in range (0,80):
		v.append(random.choice(p))
		p.remove(v[l])
		for m in range (0,100):
			for f in range (0,5):
			
				if t[m][f]==v[l]:
					c[m]=c[m]+1
				if c[m]==5:
					c[m]=l
				
					
	p=p+v
	min=80
	for z in range (0,100):
		if c[z]<min:
			min=c[z]
	sum=sum+min
av=sum/1000
print av

	
	
