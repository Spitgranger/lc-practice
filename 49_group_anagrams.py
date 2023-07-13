from collections import defaultdict


# The complexity of this solution is m*(nlogn) slow since every single string within the given list needs to be sorted
def group_anagrams(strs):
    word_dict = {}
    counter = 0
    group_anagrams_list = []
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in word_dict:
            group_anagrams_list[word_dict.get(sorted_word)].append(word)
        else:
            group_anagrams_list.append([word])
            word_dict.update({sorted_word: counter})
            counter += 1
    print(group_anagrams_list)

# Faster, the run time complexity is m*n*26 ~ m*n
def group_anagrams_faster(strs):
    word_dict = defaultdict(list)
    for word in strs:
        characters = [0]*26
        for char in word:
            characters[ord(char) - ord('a')] += 1
        word_dict[tuple(characters)].append(word)
    print(word_dict.values())
    return word_dict.values()

if __name__ == '__main__':
    group_anagrams(["eat","tea","tan","ate","nat","bat"])
    group_anagrams_faster(["eat","tea","tan","ate","nat","bat"])
