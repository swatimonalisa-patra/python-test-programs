# Python3 program to convert 12
# hour to 24 hour format
def print24(s):
 
    # Get hours
    h1 = ord(s[1]) - ord('0')
    h2 = ord(s[0]) - ord('0')
    hh = (h2 * 10 + h1 % 10)
  
    # If time is in "AM"
    if (s[8] == 'A'):
        if (hh == 12):
            print('00', end = '')
             
            for i in range(2, 8):
                print(s[i], end = '')
 
        else:
            for i in range(0, 8):
                print(s[i], end = '')
  
    # If time is in "PM"
    else:
        if (hh == 12):
            print("12", end = '')
             
            for i in range(2, 8):
                print(s[i], end = '')
         
        else:
            hh = hh + 12;
            print(hh, end = '')
             
            for i in range(2, 8):
                print(s[i], end = '')
             
# Driver code          
if __name__=="__main__":
 
   s = "08:55:48PM"
    
   print24(s)
    
