#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    nums = list_of_integers
    start = 0
    end = len(nums)-1

    if nums[start] > nums[start+1]:
        return nums[start]
    if nums[end] > nums[end-1]:
        return nums[end]

    mid = (start+end)//2
    if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
        return nums[mid]
    if nums[mid] < nums[mid-1]:
        return find_peak(nums[start:mid+1])
    elif nums[mid] < nums[mid+1]:
        return find_peak(nums[mid:end+1])
    else:
        return nums[start]
