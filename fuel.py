def main():
    #promt the user for input through function
    i= get_int()
    
    #round the float to nearest int after mutiply the float with 100 to have two digit number
    z = round(i*100)
    

    if z <= 1:
        print("E")
    elif z >= 99:
        print("F")
    else:
        print(f"{z}%")

 
def get_int():
    while True:
        try:
            #use split function to get two values from user
            x,y = input("Fraction: ").split("/")
            x = int(x)
            y= int(y)

            #raise valueerror to prompt user 
            if x > y:
                raise ValueError
            z = x/y
            return z
            
            
        except (ValueError, ZeroDivisionError):
            pass
   

main()


    54