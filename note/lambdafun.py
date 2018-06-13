
# use lambda in map() function
print('use lambda in map() function')
'''
def double(x):
    return x * 2
'''

nums = [4, 3, 7, 6, 2, 1]
# nums2 = list(map(double, nums))

# use lambda
nums2 = list(map(lambda x : x *2 , nums))

print(nums2)

# use lambda in filter() function

print('use lambda in filter() function')

fnums = [4, -3, 9, 1, -2, -4, 5]
fnums2 = list(filter(lambda x : x >0, fnums))
print(fnums2)

