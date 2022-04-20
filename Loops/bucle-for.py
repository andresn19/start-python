for x in range(2,20,2):
  print("todos estos numeros son pares",x)
##########################
c=0
for i in range(7):
    c=c+1
    print ("hola mundo " + str(c))
    print ("hola mundo 2"  , c)

######################
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


index_count= 0
for letter in 'abcde':
  print('At index {} the letter is {}' .format(index_count,letter))
  index_count+=1

mylist1 = []

for x in [2,4,6]:
  for y in [1,10,1000]:
    mylist1.append(x*y)

print(mylist1)

from random import shuffle



    