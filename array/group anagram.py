def groupAnagrams(stars):
    map={}
        
    for s in strs:
        sorted_string=''.join(sorted(s))
            
        if sorted_string in map:
            map[sorted_string].append(s)
        else:
            map[sorted_string]=[s]
    return list(map.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))