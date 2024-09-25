import sys

with open('E:/Python_Workbase/College/CS5115/assg1/english-words/words_alpha.txt') as f:
    words2 = f.read().splitlines()

print(len(words2))

sizewords = sys.getsizeof(words2)
print(sizewords)
