def balanced(word):
    flag=1
    #for _ in range(len(word)):
    if(word.count('(')!=word.count(')') or word.count('[')!=word.count(']') or word.count('{')!=word.count('}')):
        flag=0
    for i in range(len(word)-1):
        if(word[i]=='(' and word[i+1] in [']','}'] or word[i]=='[' and word[i+1] in [')','}'] or word[i]=='{' and word[i+1] in [')',']']):
            flag=0
            #break
    if(word[0:len(word)//2]==word[-1:-len(word)//2]):
        flag=0
    if(flag):
        return(True)
    else:
        return(False)#P
        

print(balanced('([{}])'))        
    
            
        
            
    
            
        
       
