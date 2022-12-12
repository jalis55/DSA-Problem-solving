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
        print(tracker)
        i +=1

    else:
        if s[i]==s[i-1]:            
            tracker=s[i]
            i +=1
            # break
        else:
            tracker =s[i-1]
    
    

print(tracker)
print(maxLength)
