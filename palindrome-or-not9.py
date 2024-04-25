# def checkPalindrome(str):
#     for i in range(0,len(str)):
#         if str[i]!=str[len(str)-i-1]:
#             return False
#     return True
# s= "loppol"
# print("palindrome") if checkPalindrome(s) else print("not palindrome")

'''       reverse = ''.join(reversed(str))
        if str == reverse:
                return True
        return False
s='kappak'
print(("Palindome")if checkPalindrome(s) else print("Not Palindrome"))'''

string="123321"
rev=""
for char in string:
    rev = char+rev
print("palindrome") if string == rev else print("Not Palindrome")
print("string :-" + str(string))
print("rev :- "+ str(rev))