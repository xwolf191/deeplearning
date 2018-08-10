# coding=utf-8

# author: xwolf
# origin: https://leetcode.com/problems/rotate-array/description/
# date: 2018-08-10


class RoateArray(object):

    def __init__(self):
        pass

    @staticmethod
    def roate(nums, k):
        """
        :param nums:
        :param k:
        :return:
        """
        c = len(nums) - k
        a = nums[0:c]
        b = nums[c:len(nums)]
        nums[0:k] = b
        nums[k:] = a


if __name__ == '__main__':
    rate = RoateArray()
    a = [-1, -100, 3, 99]
    print(rate.roate(a, 2))
