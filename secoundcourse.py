#Use range() to print all the even numbers from 0 to 10.
st = 'Print only the words that start with s in this sentence'
for y in st.split():
    if y.startswith('s'):
        print(y)

#Use range() to print all the even numbers from 0 to 10.

for y in range(10):
    if (y % 2) == 0:
        print(f'the number {y} is a even number')
    else:
        print(f'the number {y} is a odd number')

# simpler
print(list(range(0,10,2)))



#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

list1 = [y for y in range(1,51) if y % 3 ==0]
print(f' Her er listen {list1} ')

#Go through the string below and if the length of a word is even print "even!"

st = 'Print every word ini this sentence that has iis an evenu number of letters'
for y in st.split():
    if y.count('is'):
        print(y)

# or maybe
for y in st.split():
    if len(y)%2 == 0:
        print(f'{y}<-- has an even lenght !')


#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for y in range(100):
    if y%3 ==0 and y%5==0:
        print(f'{y} are a fizzBuzz')
    elif y%3==0:
        print(f'{y} are a Fizz')
    elif y%5==0:
        print(f'{y}) are a Buzz')
    else:
        print(y)


#Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
print([x[0] for x in st.split()])

for x in st.split():
    print(x[0])
    print(x)