a=int(input())
while(a>0):
    b=input()
    if len(b)!=10 or b[0]=='0':
        print("NO")
    else:
        k=0
        for i in b:
            if ord(i) not in range(48,58):
                print("NO")
                k=1
                break
            else:
                k=0
        if(k==0):
            print("YES")
    a=a-1
    
