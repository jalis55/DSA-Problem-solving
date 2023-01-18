s='abc'
lst=list()
for i in range(len(s)):
    lst.append(s[i])

    for j in range(i+1,len(s)):
        lst.append((s[i]+s[j]))

print(lst)
