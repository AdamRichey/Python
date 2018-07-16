for count in range (1,1000):
	if count%2 <> 0:
		print count

for count in range(1,1000000):
	if count%5 == 0:
		print count

sum=0
list=[1,2,5,10,255,3]

for val in list:
	sum=val+sum
print sum

sum=0
list=[1,2,3]

for val in list:
	sum=sum+val

avg=sum/len(list)

print avg