#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main.py: inversion counter algorithm implementation"""


# --- metadata ---
__author__ = "Travis Mann"
__version__ = "0.1"
__maintainer__ = "Travis Mann"
__email__ = "tmann.eng@gmail.com"
__status__ = "Development"


# --- imports ---
from typing import List, Tuple


# --- funcs ---
def merge_and_count_split_inv(array_1: List[int], array_2: List[int], total_length: int) -> Tuple[List[int], int]:
    """
    purpose: merge 2 arrays into one in sorted order and count the number of split inversions
    :param array_1: 1st array to merge
    :param array_2: 2nd array to merge
    :param total_length: total length of both arrays combined
    :return merged_array: array containing all elements from input arrays sorted
    :return split_inversion_count: count of split inversions between the 2 arrays
    """
    split_inversion_count = 0
    array_1_index = 0
    array_2_index = 0
    merged_array = []
    for merged_array_index in range(total_length):
        # ensure array_1 has elements and either array 2 is out of elements or next element in array 1 is smaller
        if not(array_1_index == len(array_1)) and (array_2_index == len(array_2) or array_1[array_1_index] < array_2[array_2_index]):
            merged_array.append(array_1[array_1_index])
            array_1_index += 1
        else:
            merged_array.append(array_2[array_2_index])
            # calculate number of split inversions with this element
            split_inversion_count += (len(array_1) - array_1_index)
            array_2_index += 1

    # output merged array and split count
    return merged_array, split_inversion_count


def sort_and_count(array: List[int], length: int) -> Tuple[List[int], int]:
    """
    purpose: count the number of inversions in the given array
    :param array: array of unique integers to count inversions from
    :param length: length of given array
    :return sorted_array: sorted array (ascending order)
    :return inversion_count: number of inversions in the given array
    """
    # base case
    if length == 1:
        return array, 0

    # count left, right and split inversions
    sorted_A_half_1, left_inversions = sort_and_count(array[0:length//2], len(array[0:length//2]))
    sorted_A_half_2, right_inversions = sort_and_count(array[length//2:], len(array[length//2:]))
    sorted_A, split_inversions = merge_and_count_split_inv(sorted_A_half_1, sorted_A_half_2, length)
    total_inversions = left_inversions + right_inversions + split_inversions
    return sorted_A, total_inversions


# --- main ---
if __name__ == "__main__":
    # extract list of ints as str from example file
    with open('IntegerArray.txt') as file:
        test_array = file.readlines()

    # convert strings to ints
    test_array = [int(number.replace('\n', '')) for number in test_array]

    # get inversion count
    sorted_array, inversion_count = sort_and_count(test_array, len(test_array))
    print(f'number of inversions: {inversion_count}')
