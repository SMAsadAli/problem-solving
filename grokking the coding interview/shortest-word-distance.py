# Given an array of strings words and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

def sol(words, w1, w2):
    ptr1 = -1
    ptr2 = -1
    min_dist = len(words)
    for index in range(len(words)):
        if words[index] == w1:
            ptr1 = index
        elif words[index] == w2:
            ptr2 = index
        if ptr1 != -1 and ptr2 != -1 and min_dist > abs(ptr2 - ptr1):
            min_dist = abs(ptr2 - ptr1)
    return min_dist


print(sol(["the", "quick", "brown", "fox", "jumps",
      "over", "the", "lazy", "dog"], 'fox', 'dog'))  # 5
print(sol(["a", "c", "d", "b", "a"], 'a', 'b'))  # 1
