arr=[2,2,-5,28]

def maxminavg(arr)
    max=
    sum=
    min=
    for i in arr:
            sum=sum+i
            if i>max:
                max=i
            if i<min:
                min=i
    avg=sum/len(arr)
    print avg
    print max
    print min

