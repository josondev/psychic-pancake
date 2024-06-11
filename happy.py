'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#n=int(input('enter a number:')) 

def abundant(n):
    sum1=0
    for j in range(1,n):
        if(n%j==0):
            sum1+=j
    if(sum1>n):
        return(f'{n} is an abundant number.')
    else:
        return(f'{n} is not an abundant number.')

def happy(n):
    #final=n
    #temp=final
    if(len(str(n))==1 and int(n)==1):
        return(f'{t} is a happy number.')
    elif(n in [2,3,4,5,6,8,9]): 
        #return(elif(n in [2,3,4,5,6,8,9]):
        return(f'{t} is not a happy number.')
    else:
        l=str(n);
        sum1=0
        for i in range(len(l)):
            sum1+=int(l[i])**2
        if(sum1==1):
            return(f'{t} is a happy number.') 
        else:
            return(happy(sum1))
            
flag=1
while(1):
    n=int(input('enter a number to check:'))
    t=n
    print('1:abundant number')
    print('2:happy number')
    print('3:Exit')
    #while(flag):
    try:
        ans=int(input('enter your choice:'))
    except ValueError:
        ans=int(input('enter your choice,not string:'))
    while(ans not in [1,2,3]):
        ans=int(input('enter the correct choice:'))
        
    else:
        if(ans==1):
            print(abundant(n))
        elif(ans==2):
            print(happy(n))
        elif(ans==3):
            #flag=0
            break
        
 