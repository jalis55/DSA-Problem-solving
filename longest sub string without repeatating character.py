s="pwwkew"
test = ""
    # Result
maxLength = -1
     

for c in list(s):
    current = "".join(c)
         
        # If string already contains the character
        # Then substring after repeating character
    if (current in test):
        test = test[test.index(current) + 1:]
    test = test + "".join(c)
    maxLength = max(len(test), maxLength)
print(maxLength)
