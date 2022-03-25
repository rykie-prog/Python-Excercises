#  Is Palindrome
def isPalindrome():
    a=input("Enter a word:")
    b=a[::-1]
    if(a==b):
        print(True)
    else:
        print(False)
isPalindrome()

# Doubler
def doubler():
    list = [1,3,5]
    multiplied_list = [element * 2 for element in list]
    print(multiplied_list)
doubler()

# Fizz Buzz
def fizz_buzz(max):
    result = []

    for n in range (1, max):
        if (n % 4 == 0 or n % 6 == 0) and not (n % 4 == 0 and n % 6 == 0):
            result. Append(n)
    return result

print(fizz_buzz(20))


# Average of three
def average_of_three(a,b,c):
    avg = (a+b+c)/3
    print(avg)
average_of_three(2,4,6)

# Goodbye
def goodbye(name):
    print("Goodbye", name)
goodbye("Rando")