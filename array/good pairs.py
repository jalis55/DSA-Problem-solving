lst=[1,1,1,1]

n=len(lst)
l=0
r=n-1
cnt=0

while(l !=n):
  if l==r:
    l +=1
    r=n-1
    continue
  if lst[l]==lst[r]:
    cnt +=1
    r -=1
  else:
    r -=1
print(cnt)