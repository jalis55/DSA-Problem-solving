s='racecar'


dup=set()


for a in range(len(s)):
   if s[a] in s[a+1::]:
       print(s[a])
       dup.add(s[a])

print(dup)