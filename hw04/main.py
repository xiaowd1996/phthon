21:53:48
我的手机 2017/10/15 21:53:48
for i in range(1,10):
    for k in range(1,i):
        print(end="       ")
    for j in range(i, 10):
        formula = '{0:1}x{1:1}={2:<2}'.format(i, j, i*j)
        print(formula, end=' ')
    print()
    
