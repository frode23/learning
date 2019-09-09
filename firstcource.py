
#string
#a[-1]    # last item in the array
#a[-2:]   # last two items in the array
#a[:-2]   # everything except the last two items
#a[::-1]    # all items in the array, reversed
#a[1::-1]   # the first two items, reversed
#a[:-3:-1]  # the last two items, reversed
#a[-3::-1]  # everything except the last two items, reversed

s= 'hello'
print(s[1])
print(s[::-1])
print(s[-1])
print(s[4])

#List
l1 = [0]*3
print(l1)
list1 =[1,2,[3,4,'hello']]
print('list1')

list3 = [1,2,[3,4,'hello']]
print(list3)
list3[2][2] = 'goodbye'
print(list3)

list2 = [5,3,4,6,1]
list2.sort()
print(list2)

#Dictionares

d = {'key':'hello'}
print(d['key'])
c = {'a1':{'a2':'hello'}}
print(c['a1']['a2'])
b = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print()

#Tupels immutable


#Sets dont allow dublicates
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(list5)
list5S = set(list5)
print(list5S)

#Boolean
# istrue = True
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one)
print(l_two)

