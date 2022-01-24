def find_hcf(a,b):
    hcf = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
           hcf = i
    return hcf

input1 = int(input('enter first number: '))
input2 = int(input('enter second number: '))

print('hcf of %d and %d is %d' %(input1, input2, find_hcf(input1, input2)))

