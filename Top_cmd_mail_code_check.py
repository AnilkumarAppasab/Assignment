def check(str1, str2):
    if(sorted(str1) == sorted(str2)):
        print("strings are anagrmas")
    else:
        print("strings are not anagrams")
str1 = input("Enter the string1")
str2 = input("Enter the string2")
check(str1,str2)
