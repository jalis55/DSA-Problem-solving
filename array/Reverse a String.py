s = ["h","e","l","l","o"]

i,j=0,len(s)-1

<<<<<<< HEAD
print(i,j)
=======
left=0
right=len(s)-1

while left<right:
    s[left],s[right]=s[right],s[left]
    left +=1
    right -=1

print(s)
>>>>>>> eea8678fb93c70efe37ea5e519714b000661837f
