from itertools import permutations
from english_words import english_words_set

str = input('Enter a string : ')

print('Searching for possible anagram....')
l = []
for j in list(permutations(str)):
    l.append(''.join(j))

for i in l:
    if i in english_words_set:
        print(i)
