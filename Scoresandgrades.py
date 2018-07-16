import random
score =random.random()*100
 
def scoregrade(score):
    if score>89 and score<100:
        print "Score: " + str(score) + "; Your grade is A"
    elif score>79 and score<90:
        print "Score: " + str(score) + "; Your grade is B"
    elif score>69 and score<80:
        print "Score: " + str(score) + "; Your grade is C"
    elif score>59 and score<70:
        print "Score: " + str(score) + "; Your grade is D"
    else:
        print "Score: " + str(score) + "; See teacher"

scoregrade(score)