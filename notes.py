array.remove(1) #to search list for first matching value and remove
array.del(1) # to delete at index given
array.pop(1) #to delete value at index given and return the value

range(start, stop, step)

for thing in list:
    print 'does not allow you to modify the list'
for in range(len(list)):
    print 'possible to modify the list'


phrase = "A bird in the hand..."

# Use comma to keep printing on the same line
for char in phrase:
	if char == 'A' or char == 'a':
		print 'X',
	else:
		print char,

for index, item in enumerate(list)
    print index, item
# enumerate supplies a corresponding index to each element in teh list that you pass it.

# ZIP will create pairs of elements when passed two lists, and will stop at the end of the shorter list.

# reverse a string
def reverse(text):
  a = []
  b = []
  c = len(text)
  
  for i in text:
    a.append(i)
    
  for n in range(c):
    c -= 1
    b.append(a[c])
    
  print ''.join(b)

#censor text
def censor(text, word):
  arr = text.split()
  cens = '*' * len(word)
  b = []
  
  for i in range(len(arr)):
    if arr[i] == word:
      arr[i] = cens
    
  print ' '.join(arr)

censor('cat is nice', 'nice')

#get median of a list 
def median(listy):
  listy = sorted(listy)
  if len(listy) % 2 != 0:
    return listy[len(listy)/2]
  else:
    sum = listy[len(listy)/2] + listy[len(listy)/2 - 1]
    return float(sum) /2

# bitmask
def check_bit4(input):
    checker = input & 0b1000
    if checker == 8:
        print 'bit 4 on'
    else:
        print 'bit 4 off'

a = 0b110 #6
mask = 0b1 #1
desired = a | mask #0b111

## XOR checks for either 0 or 1, false if both 

a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1

# File Access
# w = write-only
# r = read-only
# r+ = read and write
# a = append
my_list = [ i ** 2 for i in range(1, 11)]
my_file = open('output.txt', 'r+')
for n in my_list:
    my_file.write(str(n) + '\n')
my_file.close() #required when a file is opened

with open('output.txt', 'w') as textfile:
    textfile.write('success')
# textfile is not a reserved word, it is the name of the variable assigned 

if my_file.closed == False:
  my_file.close()
