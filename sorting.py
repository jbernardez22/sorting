#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input which controls how the elements of the list should be compared against each other.
If cmp(a,b) returns -1, then a<b;
if cmp(a,b) returns  1, then a>b;
if cmp(a,b) returns  0, then a==b.
'''

import random

def cmp_standard(a,b):
    '''
    used for sorting from lowest to highest
    '''
    if a<b:
        return -1
    if b<a:
        return 1
    return 0


def cmp_reverse(a,b):
    '''
    used for sorting from highest to lowest
    '''
    if a<b:
        return 1
    if b<a:
        return -1
    return 0


def cmp_last_digit(a,b):
    '''
    used for sorting based on the last digit only
    '''
    return cmp_standard(a%10,b%10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    '''

    array_1 = xs
    array_2 = ys
    merged_array = [None] * (len(array_1) + len(array_2))
    i = 0
    j = 0
    k = 0

    while i<len(xs) and j<len(ys):
        if cmp(xs[i], ys[j]) == -1:
            merged_array[k] = array_1[i]
            i = i+1
        else:
            merged_array[k] = array_2[j]
            j = j+1
        k = k+1

    while i < len(xs):
        merged_array[k] = array_1[i]
        i = i+1
        k = k+1

    while j < len(ys):
        merged_array[k] = array_2[j]
        j = j+1
        k = k+1
    return merged_array


def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs
    '''
    lst = xs
    if len(xs) <= 1:
        return xs
    else:
        half = len(lst)//2 
        left =lst[0:half]
        right =lst[half:len(lst)]
        l = merge_sorted(left, cmp=cmp)
        r = merge_sorted(right, cmp=cmp)
        merged_list = _merged(l, r, cmp = cmp)
        return merged_list

def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected, 
    and the list is split into a "less than" sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)

    You should return a sorted version of the input list xs
    '''
    
    i = 0
    smaller_than = []
    larger_than = []
    pivot_counter = 0
    if len(xs) <=1:
        return xs
    else:
        pivot = random.choice(xs)
        for i in xs:
            if cmp(i, pivot) == -1:
                smaller_than.append(i)
            elif cmp(i, pivot)==1:
                larger_than.append(i)
            else:
                pivot_counter = pivot_counter + 1
        l = quick_sorted(smaller_than, cmp = cmp)
        r = quick_sorted(larger_than, cmp = cmp)
        pivot_list = [pivot] * pivot_counter
        return l + pivot_list + r

def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented in-place,
    i.e. with O(1) memory requirement.
    Merge sort, on the other hand, has an O(n) memory requirement.

    Follow the pseudocode of the Lomuto partition scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    You should directly modify the input xs variable instead of returning a copy of the list.
    '''
