import requests
import sys
import json

try:
    if len(sys.argv) == 2:
        number = float(sys.argv[1])
    else:
        sys.exit("Missing command-line argument")
        
except ValueError:
    sys.exit("Command-line argument is not a number")



try:
    #get the data from API and load it to variable
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    # load the json model into a varible 
    o = response.json()
    # dumps the json object into an element
    l = json.dumps(o , indent = 2)

    # load the json to a string    
    json_string = json.loads(l)

    # go through the data of dict to get the value
    bpi = json_string["bpi"]

    USD = bpi["USD"]

    #get the rate and remove the , in rate to make it float 
    #otherwise it will be error as string cant br converted to float
    rate = float(USD["rate"].replace(",", ""))

    amount = number * rate 

    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit()