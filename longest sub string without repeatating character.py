# s="aab"
# s="dvdf"
s="pwwkew"
tracker=""

maxLength = -1

i=0

while i<len(s):
    if s[i] not in tracker:
        tracker +=s[i]
        maxLength=max(maxLength,len(tracker))
        maxLength=maxLength if maxLength>len(tracker) else len(tracker)
        i +=1

    else:
        tracker=tracker[1:]
    
    

print(tracker)
print(maxLength)
