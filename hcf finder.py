'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def factors(a):
    return([i for i in range(1,a+1) if(a%i==0)])

a=int(input('enter number1:'))
b=int(input('enter number2:'))

if(a%b==0 and a>b):
    print(f'the GCD of {a} and {b} is {b}.')
    
elif(a==0 or b==0):
    print(f'the GCD of {a} and {b} is 0.')
    
elif(a%b==0 and b>a):
    print(f'the GCD of {a} and {b} is {a}.')

elif(a<0 or b<0):
    
    if(a<0):
        print(f'the GCD of {a} and {b} is {max(list(set(factors(abs(a)))&set(factors(abs(b)))))}.')
        
    elif(b<0):
        print(f'the GCD of {a} and {b} is {max(list(set(factors(a))&set(factors(abs(b)))))}.')

elif(a<0 and b<0):
    print(f'the GCD of {a} and {b} is {max(list(set(factors(abs(a)))&set(factors(abs(b)))))}.')
    
    
else:
    print(f'the GCD of {a} and {b} is {max(list(set(factors(a))&set(factors(b))))}.')

