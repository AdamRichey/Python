arr=[1,2,5,99,10]

def max(arr):
     max=0
     for i in arr:
             if i>max:
                     max=i
     print max

print max(arr)