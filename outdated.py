month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#x = monthep
#y = day
#z= year

while True:
    try:
        date= input("Date: ").strip()
        x,y,z = date.split("/")
        if x.isdigit() and y.isdigit() and z.isdigit():
            x = int(x)
            y = int(y)
            z = int(z)
        if 0 < int(x) < 13 and 0 < int(y) < 32:
            break
      

    except:
        try:
            x,y,z = date.split(" ")
            
            y = int(y.strip(","))
            z = int(z)
                                
            if x.title() in month and  0 < y < 32 :
                x = int(month.index(x.title())) + 1
                break
        except:
            pass
    

print(f"{z}-{x:02}-{y:02}")
