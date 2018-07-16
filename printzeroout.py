arr=[1,2,5,-2,-3,-5]

def zero(arr):
     for i in arr:
             if arr[i]<0:
                     arr[i]=0
     print arr

print zero(arr)