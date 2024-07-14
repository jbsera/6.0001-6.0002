# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:08:43 2021

@author: joyse
"""
import numpy
import time

# print(arr)
# print(len(arr))
# print(arr[len(arr)-1])
# def intbalanced(arr):
#     sum_dict={}
#     count=0
#     if len(arr)==0 or len(arr)==1 or len(arr)==2:
#         return -1
#     else: 
#         while count<
#         sum_dict['first']=arr[0]
#         sum_dict['last']=arr[len(arr)-1]
#         if sum
###This one works

def intbalanced_firstattempt(arr):
    time_start=time.perf_counter()
    if len(arr)==0 or len(arr)==1 or len(arr)==2: #return -1 for arrays too small to have an answer
        return -1
    else:
        for i in range(1, len(arr)-1):
            first_arr=arr[:i] #split the array before the ith element
            last_arr=arr[i+1:] #split the array after the ith element
            if sum(first_arr)==sum(last_arr): #see if the sum of each array is equal
                time_stop=time.perf_counter()
                print('time:', time_stop-time_start, 'seconds')
                return i #return the index if answer found
        return -1 #return -1 if no answer found
            
            
def intbalanced(arr):
    time_start=time.perf_counter()
    memo_sum={} #initialize empty dictionary
    if len(arr)==0 or len(arr)==1 or len(arr)==2: #return -1 for arrays too small in length to have an index answer
        return -1
    else:
        memo_sum['first']=arr[0] #'first' maps to the value of the first element in the array
        memo_sum['last']=sum(arr[2:]) #'last' maps to the sum of every element in the array after the 1st index
        if memo_sum['first']==memo_sum['last']: #if 'first'='last,' the answer is the 1st index since that's where the array was split in lines 46-47
            return 1
        else: #haven't found our answer yet
            for i in range(2, len(arr)-1): #try every index from 2 (since we already tried 1) to the second to last element in the array
                memo_sum['first']+=arr[i-1] #update the dict. value for "first" by adding the ith element to its sum
                memo_sum['last']-=arr[i] #update the dict. value for "last" by subtracting the ith element from it's sum
                print(i, memo_sum['first'], memo_sum['last'])
                if memo_sum['first']==memo_sum['last']: #check if the sum of elements before index i equals the sum of elements after i
                    time_stop=time.perf_counter()
                    print('time:', time_stop-time_start, 'seconds') #for checking execution time
                    return i #if we've found an answer, return the index
        return -1 #return -1 if no answer was found
            
my_arr=numpy.array([1]*101)
y_arr=numpy.array([-1,-1,2,-2, 2, -2])
print(intbalanced(y_arr))
# print('array size', len(my_arr))
# print('intbalanced method:')
# print('answer:', intbalanced(my_arr))
# print('first attempt method:')
# print('answer:', intbalanced_firstattempt(my_arr))
# print('---------------')
# my_arr=numpy.array([1]*10001)
# y_arr=numpy.array([1,2,2])
# print('array size', len(my_arr))
# print('intbalanced method:')
# print('answer:', intbalanced(my_arr))
# print('first attempt method:')
# print('answer:', intbalanced_firstattempt(my_arr))
# print('------------')
# my_arr=numpy.array([1]*100001)
# y_arr=numpy.array([1,2,2])
# print('array size', len(my_arr))
# print('intbalanced method:')
# print('answer:', intbalanced(my_arr))
# print('first attempt method:')
# print('answer:', intbalanced_firstattempt(my_arr))
# print('---------------')
# print('sum method', intbalanced_1(my_arr))