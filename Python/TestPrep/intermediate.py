import random
import string
import scrabble
import time
import sys

lucky = random.randint(1,6)
print ('Your lucky number is: {}'.format(lucky))

def has_all_vowels(word):
    vowels = 'aeiou'
    for vowel in vowels:
        if vowel not in word:
            return False
    return True
# find out if there is any word that does not have a double letter
for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            exists = True
            # print (word)
            break
    if not exists:
        print ("double {} does not exists".format(letter))

for word in scrabble.wordlist:
    if has_all_vowels(word):
        print (word)

print ('\n\n\n')
isPalindrome = False
longest = ''
for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest):
        longest = word
        isPalindrome = True
if isPalindrome:
    print (longest)
longest = [word for word in scrabble.wordlist if word == word[::-1]]
# now sort the list by length of words
longest.sort(lambda x,y: cmp(len(x), len(y)))
# print last word
print (longest[-1])
# **** make a copy of a list
my_list = ["apple", "banana", "orange"]
copy_list = my_list[:]
print (copy_list)
reverse_value = my_list[::-1]
print (reverse_value)

start = time.time()
try:
    sonnet_wrd = [val.strip() for val in open("sonnet_words.txt",'r').readlines()]
    scrabble_wrd = [val.strip() for val in open("sowpods.txt", 'r').readlines()]

    sonnet_set = set(sonnet_wrd)
    scrabble_set = set(scrabble_wrd)
    for word in sonnet_set:
        if word not in scrabble_set:
            print (word.lower())
except Exception as err:
    print (str(err))
    sys.exit(1)
end = time.time()
print ("time is %.3f\n" % (end-start))
print('hello')