def function1 (ls):
    n = len(ls)
    for i in range (0, n):
        for j in range (1, n):
            if (ls[j-1] >= ls[j]):
                ls[j-1], ls[j] = ls[j], ls[j-1]
   
    print '[%s]' % ', '.join(map(str, ls)) 


def function2 (ls, element):
    n = len(ls)
    count = 0
    for i in range (0, n):
        if ( ls[i] == element):
            count = count + 1
    count = str(count)
    print (count)

def function3(n):
    ls = [1]
    temp = []
    print ls
    for i in range (0, n-1):
        ls2=[]
        ls2.append(1)
        for j in range (1,len(ls)):
            ls2.append(ls[j-1] + ls[j])
        ls2.append(1)
        ls = ls2
        print ls
