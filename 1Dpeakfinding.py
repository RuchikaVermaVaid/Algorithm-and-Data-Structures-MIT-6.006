# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:00:03 2019

@author: Ruchika
"""

#######################################################################################
############################## Function to find local 1D peak #########################
#######################################################################################

#Function to find local peak in 1D array
def peakfinder1D(arr):

        mid = int(len(arr)/2) #If list has multiple elements, peak needs to find using divide and conquer approach
        print(arr)
#         print('Middle')
        print("Middle elements is "+str(arr[mid]))
        if (len(arr)>=3):#If length array>=3 then divide and conquer approach is required
                #If middle element is greater than both of its neighboring elements
                if ((arr[mid] > arr[mid+1]) & (arr[mid] > arr[mid-1])):
                    return arr[mid] 
                #If middle element is greater than its left element but smaller then its right element
                elif ((arr[mid] < arr[mid+1]) & (arr[mid] > arr[mid-1])):
                    return peakfinder1D(arr[mid:])
                #If middle element is greater than its right element but smaller then its left element
                elif ((arr[mid] < arr[mid-1]) & (arr[mid] > arr[mid+1])):
                    return peakfinder1D(arr[:mid])
                #If middle element is smaller than both of its neighboring elements
                else:
                    if (arr[mid-1] > arr[mid+1]):
                        return peakfinder1D(arr[:mid])
                    else:
                        return peakfinder1D(arr[mid:])
                
        print('1D peak found')           
        return arr[mid]
    

array = [1,155,100,25,58,100,104]
print("Given array is " + str(array))
print("Local peak in 1D array is " + str(peakfinder1D(array))) 
    