hr=int(input())
temp=hr
rev=0
while temp!=0:
    rev=(rev*10)+(temp%10)
    temp=temp//10
if hr==rev:
    print("yes")
else:
    print("no")
