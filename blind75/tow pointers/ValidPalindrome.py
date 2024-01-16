# Input: s = "A man, a plan, a canal: Panama"
# Output: true
def isPalindrome(s):
        
    sen=""

    for i in s:
        if i.isalnum():
            sen +=i

    return sen.lower()==sen[::-1].lower()

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))


