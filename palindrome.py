'''
is_palindrome("Step on no pets!")
True
is_palindrome("'Tis not a palindrome")
False
is_palindrome("Hi, I am Mai Ih")
True
'''

def remove(input_str): 
    return input_str.replace(" ","") 

def is_palindrome(input_str): 
    remove(input_str)
    return input_str.lower() == input_str[::-1].lower()

print(is_palindrome("Hello"))
print(is_palindrome("Racecar"))
