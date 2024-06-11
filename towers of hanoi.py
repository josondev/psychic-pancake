'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def towers(n,beg,aux,dest):
    
    if(n==1):
        print(f'move disk 1 from source {beg} to destination {dest}.')
        return
    towers(n-1,beg,dest,aux)
    print(f'move disk {n} from source {beg} to destination {dest}.')
    towers(n-1,aux,beg,dest)

towers(int(input('enter number of disks:')),'a','b','c')     




