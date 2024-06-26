
def permutation(n,r):
    if(r==0):
        return(1)
    elif(r==1):
        return(n)
    elif(r==n):
        return(factorial(n))
    else:
        return(factorial(n)//factorial(n-r))
        
def combination(n,r):
    if(r==0):
        return(1)
    elif(r==n):
        return(1)
    else:
        return(factorial(n)//(factorial(n-r)*factorial(r)))  
        
def factorial(n):
    fact=1
    if(n==0):
        return(1)
    elif(n==1):
        return(1)
    else:
        while(n>0):
            fact*=n
            n-=1
    return(fact) 
flag=1
while(flag):    
    word=input('enter either permutations or combinations:')
    a=int(input('enter total number of objects:'))
    b=int(input('enter sample objects:'))
    if(b>a):
        print('both permutations and combinations not possible.')
    else:
        
        if(word=='permutations'):
            result=permutation(a,b)
        else:
            result=combination(a,b)
        print(f'number of {word} possible are {result}.')   
    ans=input('do you want to continue:?')  
    if(ans=='no'):
        flag=0
    
        
    






