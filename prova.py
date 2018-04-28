def primos():
    for i in range(2,1000):
        for x in range(2, i-1):
            if i % x == 0:
                break
        else:
            print('é primo: '+str(i))
primos()