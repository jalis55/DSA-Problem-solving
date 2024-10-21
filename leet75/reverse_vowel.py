s=list("IceCreAm")
l=0
r=len(s)-1


while l<r:
    if (s[l] in 'aeiouAEIOU') and (s[r] in 'aeiouAEIOU'):
        if s[l] !=s[r]:
            s[l],s[r]=s[r],s[l]
            l +=1
            r -=1
        else:
            l +=1
            r -=1
    elif (s[l] in 'aeiouAEIOU') and (s[r] not in 'aeiouAEIOU'):
        r -=1
    
    elif (s[l] not in 'aeiouAEIOU') and (s[r] in 'aeiouAEIOU'):
        l +=1
    else:
        l +=1
        r -=1


print("".join(s))

# AceCreIm
# AceCreIm