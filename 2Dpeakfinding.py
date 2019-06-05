# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:12:58 2019

@author: Ruchika
"""

#######################################################################################
############################## Function to find local 2D peak #########################
#######################################################################################

import numpy as np
def peakfinder2D(arr):
    mid_j = int(arr.shape[1]/2)
    temp_arr = arr[:,mid_j]
    maxx = peakfinder1D(temp_arr)
    i = np.where(temp_arr == maxx)    
    print("Array turned to \n" + str(arr))
    print("\n")
    
    if(arr.shape[1] == 1):# If length of columns is 1 then it has a peak at 0th element
        return arr[i,mid_j]
    
    elif (arr.shape[1] == 2):#If length of columns is 2 then do comparison with the column 0 element corresponding to row having maxx value
        if (arr[i,mid_j] > arr[i,0]):
            return arr[i,mid_j]
        else:
            return arr[i,0]
    else:
        #If length of columns is greater than 2, use divide and conquer approach
        #If middle element corresponding to ith row is greater than both of its neighboring elements
        if ((arr[i,mid_j] >= arr[i,mid_j+1]) & (arr[i,mid_j] >= arr[i,mid_j-1])):
            return arr[i,mid_j] 
    
        #If middle element corresponding to ith row is greater than its (i,left column) but smaller than (i,right column)
        elif (arr[i,mid_j]<arr[i,mid_j+1] & arr[i,mid_j]>arr[i,mid_j-1]):
            return peakfinder2D(arr[:,mid_j+1:])
    
        #If middle element corresponding to ith row is greater than its (i,right column) but smaller than (i,left column)
        elif (arr[i,mid_j]>arr[i,mid_j+1] & arr[i,mid_j]<arr[i,mid_j-1]):
            return peakfinder2D(arr[:,:mid_j])
    
        else:
            #If middle element corresponding to ith row is smaller than both of its neighboring elements
            if (arr[i,mid_j-1] > arr[i,mid_j+1]):
                return peakfinder2D(arr[:,:mid_j])
            else:
                return peakfinder2D(arr[:,mid_j+1:])



#######################################################################################
############################## Function to find local 1D peak #########################
#######################################################################################

# peakfinder1D will be used to find 2D peak
def peakfinder1D(arr):

        mid = int(len(arr)/2) #If list has multiple elements, peak needs to find using divide and conquer approach
        if (len(arr)==1):# If length of array is 1 then it has a peak at 0th element
            return arr[0]
        elif (len(arr) == 2):#If length of array is 2 then do comparison with the element at 0th index
            if arr[mid]>arr[0]:
                return arr[mid]
            else:
                return arr[0]
        else:
                #If length of array is greater than 2, use divide and conquer approach               
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
                     
#Let's check peakfinder2D function
mat = [x for x in range(25)]
mat = np.reshape(mat,(5,5))
print(peakfinder2D(mat))

