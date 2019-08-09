zx=int(input())
if(zx>1):
	for i in range(2,zx):
		if(zx%i)==0:
			print("no")
			break
		else:
			print("yes")
else:
	print("no")
