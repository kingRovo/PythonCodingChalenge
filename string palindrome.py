str1="MADAM"
str1=str1.casefold()
str_rv=reversed(str1)

if(list(str1)==list(str_rv)):
    print("String is palindrome")
else:
    print("String is not palindrome")




