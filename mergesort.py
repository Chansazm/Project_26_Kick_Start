def mergesort(array):
    #get the length and divide into two
    length = len(array) - 1
    low = 0
    right = length
    
    #if array has one item sorted
    if length == 1:
        return
    
    #call mergesort recursively on left and right
    if length > 1:
        mergesort(array)
    
    
    #Merge the left and right




array = [3,5,7,2,1,-1]

#Driver function
print(mergesort(array))
# array = [-1,1,2,3,5,7]