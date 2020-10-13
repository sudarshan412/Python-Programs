# https://www.hackerearth.com/practice/algorithms/string-algorithm/manachars-algorithm/practice-problems/algorithm/easypalindrome-8671e4e3/

# EAsy Palindrome --- Python 3

n=int(input())
s=input()
def gets(s):
    x='@'
    for i in s:
        x+='#'+i
    x+='#&'
    c=0
    r=0
    p=[0 for i in range(len(x))]
    for i in range(1,len(x)-1):
        mirror=2*c-i
        if(r>i):
            p[i]=min(r-i,p[mirror])
        while(x[i+1+p[i]]==x[i-1-p[i]]):
            p[i]+=1
        if(i+p[i]>r):
            c=i
            r=i+p[i]
    m=0
    c=0
    for i in range(len(x)):
        if(p[i]>m):
            c=i
            m=p[i]
    return s[(c-1-m)//2:(c-1-m)//2+m]
ans=0
while(True):
    if(len(s)==1):
        break
    s=gets(s)
    if(len(s)==0):
        s=prev
        break
        
    if(len(s)==1 or len(s)%2==1):
        break
    else:
        s=s[:len(s)//2]
        prev=s[0]
        ans+=1
print(ans)
print(s)