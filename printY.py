arr=[1,2,5,6,99]
y=7

def Y(arr,y):
     count=0
     for i in arr:
             if i>y:
                     count=count+1
     print count

print Y(arr,y)