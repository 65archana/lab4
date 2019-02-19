length1=int(input("enter a length "))
length2=int(input("enter a length "))
x=[]
h=[]
for i in range (0,length1,1):
	a=int(input("enter the value:"))
	x.append(a)
for i in range (0,length2,1):
	a=int(input("enter the number:"))
	h.append(a)
import numpy as np
p=np.zeros(length1+length2-1)
for n in range (0,length1+length2-1):
	r=0
	for k in range (0,length1):
		if ((n-k)>=0 and (n-k)<length2):
			r=r+x[k]*h[n-k]
	p[n]=b
print (p)



