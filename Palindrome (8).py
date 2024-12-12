#Palindrome :

def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        print(f"The string '{string}' is a palindrome")
    else:
        print(f"The string '{string}' is not a palindrome")

s = input("Enter a String:")
is_palindrome(s)
