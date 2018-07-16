word=['hello','world','my','name','is','Anna']
char='l'

def find(word,char):
    word2=[]
    for i in range (len(word)):
        if char in word[i]:
            word2.append(word[i])
    print word2

print find(word,char)

