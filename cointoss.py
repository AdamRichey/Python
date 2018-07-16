import random

def coin():
    head=0
    tail=0
    for i in range (0,5001):
        x=random.random()
        xr = round (x)
        if xr == 0:
            head=head+1
            print "Attempt #"+str(i)+": Throwing a coin... It's a head! ... Got "+ str(head)+" head(s) so far and "+str(tail)+" tail(s) so far"
        else:
            tail=tail+1
            print "Attempt #"+str(i)+": Throwing a coin... It's a tail! ... Got "+ str(tail)+" tail(s) so far and "+str(head)+" head(s) so far"

print coin()
