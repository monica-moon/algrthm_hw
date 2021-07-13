#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#the string 'aabcde' contains duplicate characters and should return False.

def check_unique_chars(string):
    if string is None:
        return False
    for char in string:
        if string.count(char)>1:
            return False
    return True
print (check_unique_chars('abcde'))
print(check_unique_chars('aabcde'))