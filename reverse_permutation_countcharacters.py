# Reversing a statement
#Build an algorithm that will print the given statement in reverse.
#Example: Stay Loyal to your vision
#Reversed string = noisiv ruoy ot layoL yatS

string = "Stay Loyal to your vision"
reversed = string [::-1]
print(reversed)


#Permutations
#Write a solution that will print all permutations of a string.
#A permutation is an act of changing the arrangement of characters.
#Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}

def permutations(word):
    if len(word) == 1:
        return [word]
    perms = permutations(word[1:])
    char = word[0]
    result = []

    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result
print(permutations('ABC'))

#Count Characters
#Create a program that will count vowels and consonants in a string.
#Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}

string="Hello world"
vowel = set("aeiouAEIOU")
print(vowel)
v_count=0
c_count=0
for i in string:
    if i in vowel:
        v_count=v_count+1
    elif( (i>='a' and i<='z') or (i>='A' and i<='Z')):
        c_count = c_count + 1
print("Number of consonents in the sring:", c_count)
print("Number of vowels in the string:", v_count)