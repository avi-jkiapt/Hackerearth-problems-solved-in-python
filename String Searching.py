a=input()
b=input()
l=len(a)
count=0
for c in range(0,len(b)):
     if b[c:c+l]==a:
        count+=1
print(count)

        