largest=0
for i in range(1000):
	if i%6==2:
		if ((i*i*i)%5==3):
			if i>largest:
				largest=i
print(largest)
