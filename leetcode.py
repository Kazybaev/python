# def one_list(one, two):
#     new = one + two
#     two = sorted(new)
#     return two
#
# print(one_list([1, 2, 4], [1, 3, 4]))





# Вход: список1 = [1,2,4], список2 = [1,3,4]
#  Выход: [1,1,2,3,4,4]



# def polin(x):
#     new_set = str(x)
#     new_list = []
#     if new_set[::-1] in new_set != new_list:
#         return True
#     else:
#         return False
#
#
# print(polin(555))


# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.rstrip().split()[-1])



# def world(s):
#     for i in s:
#         if i[::-1]:
#             print(i)
#
#
#
# print(world('Hello World'))




# nums1 = {4, 8, 3, 2}
# nums2 = {7, 3, 9, 2}
#
# num1 = nums1.union(nums2)
# num2 = sorted(num1, reverse=True)
# print(num2)



# def plus_one(digits):
#     for i in range(len(digits) - 1, -1, -1):
#         if digits[i] < 9:
#             digits[i] += 1
#             return digits
#         digits[i] = 0
#     return [1] + digits
# print(plus_one([1, 2, 3, 5, 9, 5]))


# def removeDuplicates(nums):
#     k = set(nums)
#     return sorted(list(k))
#
# print(removeDuplicates([1, 2, 2, 4, 4, 8, 8]))


# def removeDuplicates(nums):
#     k = 0
#     for num in nums:
#         if k == 0 or num != nums[k - 1]:
#             nums[k] = num
#             k += 1
#     return k
#
# print(removeDuplicates([1, 2, 2, 4, 4, 8, 8]))

#
# def isPalindrome(s):
#     for i in s:
#         if i[::-1]:
#             print(len(i))
#
#
# print(isPalindrome(['car', 'rr', 'rac']))








def mySqrt(x):
    for i in x:
        if 2 * 2 == x:
            print(i)


print(mySqrt([8]))