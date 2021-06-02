def splitString(str):

    loweralpha = ""
    upperalpha = ""
    evennum =""
    oddnum = ""
    space = ""
    special= ""
    for i in range(len(str)):
        if (str[i].isdigit()):
            if((str[i]%2)==0):
                evennum = evennum+str[i]
            elif((str[i]%2)!=0):
                oddnum = oddnum+str[i]
        elif(str[i] >= 'A' and str[i] <= 'Z'):
            upperalpha += str[i]
        elif(str[i] >= 'a' and str[i] <= 'z'):
            loweralpha += str[i]
        
        else:
            special += str[i]
            
    print(special)
    print(loweralpha)
    print(upperalpha)
    print(oddnum)
    print(evennum)
    print(space)

# Driver Code
if __name__ == "__main__":

    str = "131/265 is where I and Sam Live"
    splitString(str)
    
                
