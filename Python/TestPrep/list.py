#!/usr/bin/python

# string compression
str1= 'aaabbbccc'
compressed = []
endcase = 1
count = 0
x = len(str1)
for i in range(x-1):
    char = str1[i]
    if str1[i] == str1[i+1]:
        count += 1
        if i+1 == len(str1):
            char = str1[i+1]
    else:
        compressed.append(char)
        compressed.append(count+1)
        count = 0
        if i+1 == x-1:
            endcase = 0
# end case
if endcase == 0:
    char = str1[x-1]
compressed.append(char)
compressed.append(count+1)

str1 = "change to something".replace(' ', '%20')

# matrix
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
matrix1 = [[row[i] for row in matrix] for i in range(4)]

print (len(matrix))
for row in matrix:
     print (row)


# two list member add up to 9
a = [1,3,7,4]
b = [2, 1, 6, 0]
x = 9
values = {}
# val = []
for i in a:
    d = 9 - i
    if d in b:
        values[i] = d

# anagram
a = 'god'
b = 'dog'
c = 'dogg'

a1 = sorted(list(a))
b1 = sorted(list(b))
if a1 == b1:
    print('anagram')



class Node:
    def __init__(self, data, next=[]):
        self.data = data
        self.next = []
        if next != []:
            next.next = self
    def setHead(self, root=[]):
        self.head = root
    def getHead(self):
        return self.head

l1 = Node(1)
l2 = Node(2, l1)
l3 = Node(3, l2)
print ('hi')


