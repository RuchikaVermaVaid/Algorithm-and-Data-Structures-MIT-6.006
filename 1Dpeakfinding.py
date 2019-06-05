# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:00:03 2019

@author: Ruchika
"""

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

#Check how the function peakfinder1D works
array = [1,155,120,105,58,100,55,85]
print(peakfinder1D(array))
