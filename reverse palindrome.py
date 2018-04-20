# Program to check if a string
#  is palindrome or not

# change this value for a different output
str = 'kanak'


# reverse the string
rev_str = reversed(str)

# check if the string is equal to its reverse
if list(str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
