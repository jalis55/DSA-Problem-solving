sen="bacacbefaobeacee"


k=4

def count_vowel(lst):
    c=0
    for i in range(len(lst)):
        if lst[i] in 'aeiou':
            c +=1
    return c


total_vowel=count_vowel(sen[:k])
max_vowel_count=total_vowel

for i in range(len(sen)-k):
    if sen[i] in 'aeiou':
        total_vowel -=1
    if sen[i+k] in 'aeiou':
        total_vowel +=1
    max_vowel_count=max(total_vowel,max_vowel_count)

print(total_vowel)