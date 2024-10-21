# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""


def gcdOfStrings(str1: str, str2: str) -> str:
    new_str=""
    match_counter=0
    str2_idx=0

    
    for i in range(len(str1)):
        if str2_idx==len(str2):
            str2_idx=0
        if str1[i]==str2[str2_idx]:
            print(str2[str2_idx])
            new_str +=str1[i]
            str2_idx +=1

    return new_str==str1


str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1,str2))