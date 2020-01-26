"""
1. Write a Python function that accepts a string and calculate the number of upper case 
letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12

2. Write a Python function to find the Max of three numbers

3. Write a Python function that takes a number as a parameter and check the number is prime or 
not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive 
divisors other than 1 and itself
"""
def countString(string):
    # to count the number of lower and upper case respectively
    lowercase_num = 0
    uppercase_num = 0
    # check and count them respectively
    for char in string:
        if char.isupper():
            uppercase_num +=1
        elif char.islower():
            lowercase_num +=1
    print(' String: ',string,'\n No. of Upper case character: ',uppercase_num,'\n No. of Lower case character: ',lowercase_num)
text = input(' Enter your Text: ')
countString(text)


# for maximim number
def maxNumber(a,b,c):
    print('The maximum number is: {}'.format(max(a,b,c)))

a,b,c = input('Please Enter Three Numbers eg: 1,2,3: ').split(',')
maxNumber(a,b,c)


# for prime number
num = int(input("Enter any number: "))

if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
else:
    print(num, "is not a prime number")