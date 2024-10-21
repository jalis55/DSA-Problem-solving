# Input: s = "the sky is blue"
# Output: "blue is sky the"

# s = "the sky is blue"
s="  hello world  "

s=list(s.split())
print(s)

f=0
l=len(s)-1

while f<l:
    s[f],s[l]=s[l],s[f]

    f +=1
    l -=1
print(s)
print(" ".join(s))