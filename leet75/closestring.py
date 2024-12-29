def closeStrings(word1, word2):
    if len(word1) != len(word2):
        return False

    word1_frq = {}
    word2_frq = {}
    for i in range(len(word1)):
        word1_frq[word1[i]] = word1_frq.get(word1[i], 0) + 1
        word2_frq[word2[i]] = word2_frq.get(word2[i], 0) + 1

    # Check if both words have the same set of unique characters
    if word1_frq.keys() != word2_frq.keys():
        return False

    # Check if the frequency counts can be rearranged to match
    if sorted(word1_frq.values()) != sorted(word2_frq.values()):
        return False

    return True
