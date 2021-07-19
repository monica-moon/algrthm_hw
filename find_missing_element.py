# #Consider an array of non-negative integers.
# # A second array is formed by shuffling the elements of the first array and deleting a random element.
# # Given these 2 arrays find which element is missing in the second array
# #Example of the input: The first array is shuffled and the number 5 is removed to construct the second array.
# #Input:
# # [1,2,3,4,5,6,7], [3,7,2,1,4,6]
# #
# #Output:
# # 5 is the missing number
#
# # 0(NlogN)
# def find_missing_number (arr1, arr2):
#     arr1.sort()
#     arr2.sort()
#
#     for num1, num2 in zip(arr1,arr2): # [(1-first value,1-second value) (2,2) (3,3)...
#       #!= #not equal num
#       if num1 != num2:
#           return num1
#     rerutn_arr1[-1]
# #print(find_missing_number([1,2,3,4,5,6,7], [3,7,2,1,4,6]))

import collections

def find_missing_number (arr1, arr2):
    d = collections.defaultdict(int)


    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -=1
print(find_missing_number( [1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]

#Given an array of of integers ( positive and negative) find the largest continuous sum.
#Input : [1,2,-1,3,4,10,10,-10,-1]
#Output: 29

def find_max_sum(arr):
    if len(arr) == 0:
        return 0

    if len(arr) ==1:
        return arr[0]

    max_sum = current_sum = srr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)

        max_sum = max(current_sum, max_sum)

        return max_sum

print(find_max_sum(1,2,-1,3,4,10,10,-10,-1])
